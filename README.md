# Set the title of the app
st.title("Welcome to My Streamlit App!")

# Create a sidebar for user input
st.sidebar.header("User Input")

# Get user input for name and age
name = st.sidebar.text_input("Enter your name:")
age = st.sidebar.number_input("Enter your age:", min_value=0, max_value=120, value=25)

# Display the greeting message
if st.sidebar.button("Submit"):
    if name:
        st.write(f"Hello, {name}! You are {age} years old.")
        
        # Age-based message
        if age < 18:
            st.write("You're still a minor!")
        elif 18 <= age < 65:
            st.write("You're an adult!")
        else:
            st.write("You're a senior citizen!")
    else:
        st.write("Please enter your name.")

# Add a footer
st.markdown("---")
st.write("This is a simple Streamlit app to demonstrate user input.")
```

### How to Run the App

1. Save the code in a file named `app.py`.
2. Open a terminal or command prompt.
3. Navigate to the directory where you saved `app.py`.
4. Run the following command:

```bash
streamlit run app.py
```

5. This will start a local server, and you should see a message in the terminal with a URL (usually `http://localhost:8501`). Open that URL in your web browser to see your Streamlit app in action.

### Features of the App

- A sidebar for user input where users can enter their name and age.
- A button to submit the input.
- A personalized greeting message based on the input.
- An age-based message that categorizes the user as a minor, adult, or senior citizen.

Feel free to modify the code to add more features or customize it according to your needs!