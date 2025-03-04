import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from .data_loader import load_data
from .data_preprocessor import DataPreprocessor
from .data_visualizer import DataVisualizer

__all__ = ['load_data', 'DataPreprocessor', 'DataVisualizer']

# Set the title of the app
st.title("CSV Data Visualizer")

# File uploader for CSV files
uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

if uploaded_file is not None:
    # Read the CSV file into a DataFrame
    df = pd.read_csv(uploaded_file)

    # Display the first few rows of the DataFrame
    st.write("Data Preview:")
    st.dataframe(df.head())

    # Display basic statistics
    st.write("Basic Statistics:")
    st.write(df.describe())

    # Select a column for visualization
    column_names = df.columns.tolist()
    selected_column = st.selectbox("Select a column to visualize", column_names)

    # Plotting the selected column
    st.write(f"Line Chart for {selected_column}")
    plt.figure(figsize=(10, 5))
    plt.plot(df[selected_column])
    plt.title(f"Line Chart of {selected_column}")
    plt.xlabel("Index")
    plt.ylabel(selected_column)
    plt.grid()
    st.pyplot(plt)

    # Optionally, you can add more visualizations or analyses here
else:
    st.write("Please upload a CSV file to get started.")