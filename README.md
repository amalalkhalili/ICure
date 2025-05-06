# ICure
This project is a web-based health assistant developed as part of my graduation project using the Django framework. The system allows users to enter symptoms and receive a predicted disease using a hybrid machine learning model. It combines a clean, responsive frontend with a secure backend and predictive analytics to help users understand their symptoms better before seeking medical care.

🌐 Website Description
The Smart Health Diagnosis Web App aims to assist users in identifying potential health conditions based on their reported symptoms. It is designed with accessibility and usability in mind, offering both public and logged-in user experiences.

🔑 Key Functionalities:
Symptom-Based Diagnosis:
Users input symptoms via an intelligent search bar with autocomplete. The system suggests symptoms as users type and allows multi-selection.

Disease Prediction:
The selected symptoms are processed through a machine learning model to predict the most likely disease.

User Authentication:
The platform includes full authentication: registration, login, logout, and a protected dashboard.

Dynamic UI Elements:
After login, users are directed to a dashboard with two animated buttons (as images) that provide access to key services.

Navigation Bar:
Pages include: Home, About, Doctors, Register, Log In, and Help — offering users clear, intuitive access across the site.

⚙️ Technologies Used
💻 Frontend:
HTML5 & CSS3: For page structure and styling

JavaScript (vanilla): For interactivity, dynamic symptom suggestions

Bootstrap / Tailwind CSS (optional): For responsive design and styling enhancements

🧠 Backend:
Django: Main framework for routing, templating, and backend logic

SQLite: Default database for development and data storage

Django Forms & Templates: For dynamic user inputs and rendering pages

🤖 Machine Learning:
Pandas & NumPy: For data preprocessing

scikit-learn:

CountVectorizer for text vectorization

cosine_similarity for similarity metrics

LinearSVC for supervised disease classification

train_test_split, accuracy_score for model training and evaluation

Pickle: For saving and loading the trained SVM model

📂 Dataset

The project uses a custom dataset DData.csv that maps diseases to their associated symptoms.

The model combines content-based and collaborative filtering techniques to enhance prediction performance.

🧪 Output Example
Once a user selects symptoms and submits the form:

The backend fetches a prediction from the trained model.

The disease result is returned and displayed to the user on the interface.
