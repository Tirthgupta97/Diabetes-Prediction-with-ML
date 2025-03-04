import streamlit as st
# Set page config must be the first Streamlit command
st.set_page_config(
    page_title="Diabetes Prediction App",
    page_icon="🏥",
    layout="wide"
)

import pandas as pd
from components.data_loader import load_data
from components.data_preprocessor import DataPreprocessor
from components.data_visualizer import DataVisualizer
from models.classifier import DiabetesClassifier

st.title("🏥 Diabetes Prediction System")
st.markdown("""
This application predicts the likelihood of diabetes based on several health metrics.
Please use the sidebar to input patient information.
""")

# Load data and initialize components
df = load_data()
preprocessor = DataPreprocessor()
classifier = DiabetesClassifier()
visualizer = DataVisualizer()

if df is not None:
    st.sidebar.header("Patient Information")
    
    def get_user_input():
        pregnancies = st.sidebar.slider('Pregnancies', 0, 17, 3)
        glucose = st.sidebar.slider('Glucose', 0, 200, 120)
        blood_pressure = st.sidebar.slider('Blood Pressure', 0, 122, 70)
        skin_thickness = st.sidebar.slider('Skin Thickness', 0, 100, 20)
        insulin = st.sidebar.slider('Insulin', 0, 846, 79)
        bmi = st.sidebar.slider('BMI', 0.0, 67.1, 31.4)
        dpf = st.sidebar.slider('Diabetes Pedigree Function', 0.078, 2.42, 0.3725)
        age = st.sidebar.slider('Age', 21, 81, 29)
        
        data = {
            'Pregnancies': pregnancies,
            'Glucose': glucose,
            'BloodPressure': blood_pressure,
            'SkinThickness': skin_thickness,
            'Insulin': insulin,
            'BMI': bmi,
            'DiabetesPedigreeFunction': dpf,
            'Age': age
        }
        return pd.DataFrame(data, index=[0])

    user_input = get_user_input()
    X_train_scaled, X_test_scaled, y_train, y_test = preprocessor.preprocess_data(df)
    classifier.train(X_train_scaled, y_train)

    # Add prediction button
    if st.sidebar.button('Predict'):
        user_input_scaled = preprocessor.preprocess_input(user_input)
        prediction = classifier.predict(user_input_scaled)
        prediction_proba = classifier.predict_proba(user_input_scaled)

        col1, col2 = st.columns(2)

        with col1:
            st.subheader("Patient Data")
            st.write(user_input)
            
            st.subheader("Prediction Results")
            outcome_labels = ['Non-Diabetic', 'Diabetic']
            
            # Style the prediction result
            if prediction[0] == 0:
                st.success(f"The patient is predicted to be: **{outcome_labels[prediction[0]]}**")
            else:
                st.error(f"The patient is predicted to be: **{outcome_labels[prediction[0]]}**")
            
            st.write("Prediction Probability:")
            st.write(f"- Non-Diabetic: {prediction_proba[0][0]:.2%}")
            st.write(f"- Diabetic: {prediction_proba[0][1]:.2%}")

        with col2:
            st.subheader("Model Performance")
            metrics = classifier.evaluate(X_test_scaled, y_test)
            st.write(f"Model Accuracy: {metrics['accuracy']:.2%}")
            
            st.subheader("Sample Dataset")
            st.write(df.head())

    # Data Visualizations
    st.subheader("Data Visualizations")
    if st.checkbox("Show Data Visualizations"):
        visualizer.plot_outcome_distribution(df)
        visualizer.plot_correlation_matrix(df)
        visualizer.plot_feature_distributions(df)