import pandas as pd
import streamlit as st
import os

@st.cache_data
def load_data():
    try:
        # Using os.path for proper path handling
        current_dir = os.path.dirname(os.path.abspath(__file__))
        data_path = os.path.join(os.path.dirname(os.path.dirname(current_dir)), 'data', 'diabetes.csv')
        
        if not os.path.exists(data_path):
            st.error(f"Dataset not found at: {data_path}")
            st.info("Please place the diabetes.csv file in the 'data' directory")
            return None
            
        df = pd.read_csv(data_path)
        return df
    except Exception as e:
        st.error(f"Error loading dataset: {str(e)}")
        return None