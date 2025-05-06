from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from djangoProject.forms import MedicalHistoryForm
from django.contrib.auth.decorators import login_required
from djangoProject.forms import CustomUserCreationForm
from .models import Symptoms, Specialization, Doctors, City, Hospital, Area
from django.http import JsonResponse
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import joblib
from .models import FinalResult
import pickle

model_path = 'C:/Users/LENOVO-H/PycharmProjects/trained_model_svc.pkl'
with open(model_path, 'rb') as file:
    model = pickle.load(file)

MODEL_PATH = 'C:/Users/LENOVO-H/PycharmProjects/model_components.pkl'
components = joblib.load(MODEL_PATH)

svc = components['svc']
vectorizer = components['vectorizer']
symptom_matrix = components['symptom_matrix']
vectorizer_binary = components['vectorizer_binary']
symptom_binary_matrix = components['symptom_binary_matrix']
content_similarity_matrix = components['content_similarity_matrix']
collab_similarity_matrix = components['collab_similarity_matrix']

def select_symptoms(request):
    symptoms =request.GET.get('search', '')
    print(symptoms)
    if symptoms:
        symptoms = Symptoms.objects.filter(Symptoms__contains=symptoms).values('Symptoms')
        return JsonResponse(list(symptoms), safe=False)
    all_symptoms = Symptoms.objects.all().values('Symptoms')
    return render(request, "events/diagnose.html", {"symptoms": all_symptoms})
    print(all_symptoms)
    #return JsonResponse(list(all_symptoms), safe=False)


def result(request):
    if request.method == "POST":
        selected_symptoms = request.POST.getlist('selected_symptoms')
        sample_symptoms_processed = " ".join(selected_symptoms)

        sample_vector = vectorizer.transform([sample_symptoms_processed])
        sample_symptom_binary_vector = vectorizer_binary.transform([sample_symptoms_processed]).toarray()

        sample_content_similarity = cosine_similarity(sample_vector, symptom_matrix)
        sample_collab_similarity = cosine_similarity(sample_symptom_binary_vector,symptom_binary_matrix)

        sample_features = np.hstack((sample_content_similarity, sample_collab_similarity))
        decision_scores = svc.decision_function(sample_features)
        top_3_indices = np.argsort(decision_scores[0])[-3:][::-1]
        top_3_diseases = [svc.classes_[idx] for idx in top_3_indices]
        print(f"Predicted Diseases: {top_3_diseases[0]}, {top_3_diseases[1]} , {top_3_diseases[2]}")

        d1 = top_3_diseases[0]
        d2 = top_3_diseases[1]
        d3 = top_3_diseases[2]

        disease1 = FinalResult.objects.get(Disease_ID=d1)
        disease2 = FinalResult.objects.get(Disease_ID=d2)
        disease3 = FinalResult.objects.get(Disease_ID=d3)
        print("disease1 = " , disease1)

        print(Specialization.objects.all())

        specialization1 = Specialization.objects.get(Specialization=disease1.Specialization)
        specialization2 = Specialization.objects.get(Specialization=disease2.Specialization)
        specialization3 = Specialization.objects.get(Specialization=disease3.Specialization)

        doctors1 = Doctors.objects.filter(Specialization_Id=specialization1.Specialization_Id)
        doctors2= Doctors.objects.filter(Specialization_Id=specialization2.Specialization_Id)
        doctors3= Doctors.objects.filter(Specialization_Id=specialization3.Specialization_Id)
        print("doctor3 = " , doctors3)

        return render(request, "events/result.html",
                      {"d1": disease1 , "d2":disease2, "d3":disease3 ,
                       "doc1":doctors1 , "doc2":doctors2 , "doc3":doctors3}
                      )

def find_doctor(request):
      return render(request, "events/find_doctor.html", {})
def hospitals(request):
    return render(request, 'events/find_hospitals.html',{})

def find_specs(request):
    specialty = request.GET.get('search', '')
    print(specialty)
    if specialty:
        specs = Specialization.objects.filter(Specialization__contains=specialty).values('Specialization')
        print("Specializations Found",specs)
        return JsonResponse(list(specs), safe=False)


def doctor_result(request): 
    if request.method == "POST":
        print("Method is get")
        print(request.POST.dict() )

        passed_spclty = request.POST.get('doctors_search')
        print("Passed Specialty ", passed_spclty)
        if passed_spclty == "":
            doctors = Doctors.objects.filter(Specialization_Id="-1")
        else:
           specialization = Specialization.objects.get(Specialization=passed_spclty)
           print(specialization.Specialization_Id)
           doctors = Doctors.objects.filter(Specialization_Id=specialization.Specialization_Id)

        for doctor in doctors:
            city = City.objects.get(City_Id=doctor.Cit_Id)  # Fetch the city by City_Id
            doctor.city_name = city.City_Name

        print("Doctors Found",doctors)

        return render(request, "events/doctors_result.html",
                      {"doctors": doctors }
                      )

    return render(request, "events/doctors_result.html")





def find_hospitals(request):
    area = request.GET.get('search','')
    print(area)
    if area:
        area = Area.objects.filter(Area_Name__contains=area).values('Area_Name')
        print("hospitals Found", area)
        return JsonResponse(list(area), safe=False)

    return JsonResponse({"error": "No hospital provided or found"}, status=400)



def hospital_result(request):
    if request.method == "GET":
        print("Method is post")

        passed_hospitals = request.GET.get('find_hospitals')
        print("Passed Specialty ", passed_hospitals)

        hospitals_found = Hospital.objects.filter(Hospital_Address__contains=passed_hospitals)
        print(hospitals_found)

        return render(request, "events/hopitals_result.html",{"hospitals": hospitals_found})





def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('medical_history')  # Redirect to login page after successful registration
    else:
        form = CustomUserCreationForm()
    return render(request, 'events/register.html', {'form': form})

def home(request):
    if request.user.is_authenticated:
        return redirect('logged_in')
    else:
        return render(request, 'events/home.html')

def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('logged_in')  # Redirect to home or another page after login
    else:
        form = AuthenticationForm()
    return render(request, 'events/login.html', {'form': form})



def logged_in(request):
    return render(request, 'events/logged_in.html')


def logout_user(request):
   logout(request)
   return redirect('home')

def diagnose(request):
    return render(request, 'events/diagnose.html')

def medical_history(request):
    if request.method == 'POST':
      form = MedicalHistoryForm (request.POST, request.FILES)
      print(request.FILES)
      if form.is_valid():
          form.save()
          return redirect('login')
      else :
          print(form.errors)
      #return redirect('home')
    return render(request, 'events/medical_history.html', {'form': MedicalHistoryForm})



@login_required
def profile(request):
    return render(request, 'events/profile.html')

def about(request):
    return render(request, 'events/about.html')


