import streamlit as st

st.header('Welcome to home page of the project')


# Title
st.title("📩 Spam Detection System")
st.subheader("Mini Project in Data Science")

# Hero Banner GIF
st.image(
        "https://media.giphy.com/media/qgQUggAC3Pfv687qPC/giphy.gif",
        caption="Machine Learning in Action 🚀",
        use_container_width=True
    )

st.markdown("---")

# Introduction
st.markdown(
        """
        ## 👋 Welcome!  
        This project is a **Spam Detection System** that classifies SMS messages into:  
        - ✅ **Ham (Not Spam)**  
        - 🚨 **Spam**

        It demonstrates the use of **Natural Language Processing (NLP)** and **Machine Learning** 
        to filter unwanted messages.  

        ---
        """
    )

# Add Project Workflow
st.header("⚙️ How It Works")
st.markdown(
        """
        1. **Data Preprocessing** – Clean and prepare the dataset  
        2. **Feature Extraction** – Convert text into numerical form (TF-IDF)  
        3. **Model Training** – Train a Naive Bayes classifier  
        4. **Evaluation** – Test the accuracy on real data  
        5. **Prediction** – Classify new messages as spam or ham  

        ---
        """
    )

# Workflow GIF
st.image(
        "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExaGJ5eDcwNHRtNGM3bHJxZ3dxYWF0aWlrbW42bGg1dTl0Y2ZtbnVjOCZlcD12MV9naWZzX3NlYXJjaCZjdD1n/du3J3cXyzhj75IOgvA/giphy.gif",
        caption="From raw text ➝ features ➝ prediction",
        use_container_width=True
    )

# Features
st.header("✨ Key Features")
st.markdown(
        """
        - 📊 Uses the **SMS Spam Collection Dataset**  
        - 🤖 Trained using **Naive Bayes (NLP)**  
        - ⚡ Achieves ~95% accuracy  
        - 🖥️ Built with **Python + Streamlit** for an interactive experience  

        ---
        """
    )

# Closing GIF
st.image(
        "https://media.giphy.com/media/111ebonMs90YLu/giphy.gif",
        caption="Say goodbye to spam! 🎉",
        use_container_width=True
    )

# Footer
st.markdown("👨‍💻 Developed as a **Data Science Mini Project**")
