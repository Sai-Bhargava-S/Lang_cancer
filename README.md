# Lung Cancer Prediction using Machine Learning
Project Overview
This project is a Lung Cancer Prediction System built using Machine Learning and Streamlit. It helps predict the likelihood of lung cancer based on user-input symptoms. The model is trained using Logistic Regression, achieving:

Training Accuracy: 93%
Testing Accuracy: 89%
Technologies Used
Python
Streamlit (for the web interface)
Logistic Regression (for model training)
Pandas, NumPy (for data handling)
Pickle (for saving the trained model)
Project Structure
nginx
Copy
Edit
Lung_Cancer_Prediction  
│── Multiple_Disease_prediction_Lung_Cancer.ipynb  # Jupyter Notebook for model training  
│── survey lung cancer.csv                        # Dataset used for training  
│── lung_cancer_model.sav                         # Trained Logistic Regression model  
│── Lang_Cancer.py                                # Streamlit application  
│── README.txt                                    # Project documentation  
How to Run the Project
1. Install Dependencies
Ensure you have Python 3.8+ installed. Then, install the required libraries:

nginx
Copy
Edit
pip install -r requirements.txt
(If requirements.txt is missing, install these manually:)

nginx
Copy
Edit
pip install streamlit pandas numpy scikit-learn pickle-mixin
2. Run the Streamlit App
arduino
Copy
Edit
streamlit run Lang_Cancer.py
Dataset
The dataset used (survey lung cancer.csv) contains symptoms and lifestyle factors that influence lung cancer.
The features include smoking habits, anxiety, fatigue, chest pain, wheezing, etc.
Model Performance
The Logistic Regression Model was trained on this dataset, achieving:

Training Accuracy: 93%
Testing Accuracy: 89%
Contribution
Feel free to contribute! Open a pull request if you improve the model or UI.

Developed by Sai Bhargava

You can save this as README.txt and upload it to your GitHub repository. Let me know if you need any modifications! 🚀
