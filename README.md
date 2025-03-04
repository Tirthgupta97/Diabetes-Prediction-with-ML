# 🏥 Diabetes Prediction Using Machine Learning

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://diabetes-prediction-with-ml.streamlit.app/)

## 📌 Overview

An interactive web application that predicts diabetes risk using machine learning. Built with Streamlit and scikit-learn, this tool analyzes medical indicators to provide real-time diabetes risk assessment.

🔴 [Live Demo](https://diabetes-prediction-with-ml.streamlit.app/)

## 🎯 Features

- **Real-time Prediction**: Get instant diabetes risk assessment
- **Interactive Interface**: Easy-to-use sliders for input parameters
- **Data Visualization**: Explore feature distributions and correlations
- **Model Insights**: View model performance metrics
- **Responsive Design**: Works on both desktop and mobile devices

## 📊 Input Parameters

| Parameter | Description | Range |
|-----------|------------|--------|
| Pregnancies | Number of pregnancies | 0-17 |
| Glucose | Plasma glucose concentration | 0-200 |
| Blood Pressure | Diastolic blood pressure (mm Hg) | 0-122 |
| Skin Thickness | Triceps skin fold thickness (mm) | 0-100 |
| Insulin | 2-Hour serum insulin (mu U/ml) | 0-846 |
| BMI | Body mass index | 0-67.1 |
| Diabetes Pedigree | Diabetes pedigree function | 0.078-2.42 |
| Age | Age in years | 21-81 |

## 🛠️ Technology Stack

- **Frontend:** Streamlit
- **Backend:** Python 3.8+
- **ML Libraries:** scikit-learn, pandas, numpy
- **Visualization:** Seaborn, Matplotlib

## ⚙️ Installation & Setup

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/diabetes-prediction.git
cd diabetes-prediction
```

2. **Create and activate virtual environment**
```bash
python -m venv venv
.\venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Run the application**
```bash
cd src
streamlit run app.py
```

## 📁 Project Structure

```
diabetes-prediction/
│
├── src/
│   ├── components/
│   │   ├── __init__.py
│   │   ├── data_loader.py
│   │   ├── data_preprocessor.py
│   │   └── data_visualizer.py
│   ├── models/
│   │   ├── __init__.py
│   │   └── classifier.py
│   └── app.py
│
├── data/
│   └── diabetes.csv
│
├── requirements.txt
├── README.md
└── .gitignore
```

## 📈 Model Performance

- **Algorithm:** Random Forest Classifier
- **Accuracy:** ~85%
- **Features:** 8 input parameters
- **Target:** Binary classification (0: Non-diabetic, 1: Diabetic)

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👥 Authors

Tirth Gupta - [@Tirthgupta97](https://github.com/Tirthgupta97)

## 🙏 Acknowledgments

- [Pima Indians Diabetes Database](https://www.kaggle.com/uciml/pima-indians-diabetes-database)
- [Streamlit Documentation](https://docs.streamlit.io/)
- [Scikit-learn Documentation](https://scikit-learn.org/stable/)

---
⭐️ Star this repository if you found it helpful!