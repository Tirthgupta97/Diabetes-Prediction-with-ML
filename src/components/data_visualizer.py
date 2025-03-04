import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt

class DataVisualizer:
    def __init__(self):
        # Changed from 'seaborn' to 'seaborn-v0_8'
        plt.style.use('seaborn-v0_8')
    
    def plot_feature_distributions(self, df):
        st.subheader("Feature Distributions")
        
        fig = plt.figure(figsize=(12, 8))
        for i, column in enumerate(df.columns[:-1], 1):
            plt.subplot(4, 2, i)
            sns.histplot(data=df, x=column, hue='Outcome', multiple="stack")
            plt.title(f'{column} Distribution by Outcome')
            plt.xticks(rotation=45)
        plt.tight_layout()
        st.pyplot(fig)
    
    def plot_correlation_matrix(self, df):
        st.subheader("Correlation Matrix")
        
        fig, ax = plt.subplots(figsize=(10, 8))
        sns.heatmap(df.corr(), annot=True, cmap='coolwarm', center=0, ax=ax)
        plt.title('Feature Correlation Matrix')
        st.pyplot(fig)
    
    def plot_outcome_distribution(self, df):
        st.subheader("Outcome Distribution")
        
        fig, ax = plt.subplots(figsize=(8, 6))
        sns.countplot(data=df, x='Outcome')
        plt.title('Distribution of Diabetes Cases')
        plt.xlabel('Outcome (0: Non-Diabetic, 1: Diabetic)')
        plt.ylabel('Count')
        st.pyplot(fig)