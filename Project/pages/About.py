import streamlit as st

st.header('Welcome to the about page of the Spam Detection System')
st.markdown(
        """
        ## Project Overview  
        The **Spam Detection System** is a machine learning mini project that classifies text messages 
        into two categories:
        - **Ham (Not Spam)**
        - **Spam**

        This project demonstrates how Natural Language Processing (NLP) techniques can be applied to 
        detect unwanted or fraudulent messages.

        ---
        ## Dataset  
        - **SMS Spam Collection Dataset** from UCI Machine Learning Repository / Kaggle  
        - Contains **5,574 SMS messages** labeled as *ham* (legitimate) or *spam*.  

        ---
        ## Methodology  
        1. **Data Preprocessing**  
           - Lowercasing  
           - Removing stopwords & punctuation  
        2. **Feature Extraction**  
           - TF-IDF Vectorization  
        3. **Model Training**  
           - Multinomial Naive Bayes  
        4. **Evaluation**  
           - Achieved ~95% accuracy on test data  

        ---
        ## Key Features  
        ✅ Classifies SMS as *Spam* or *Ham*  
        ✅ High accuracy using Naive Bayes  
        ✅ Simple and lightweight for demonstration  
        ✅ Interactive UI built with Streamlit  

        ---
        ## Future Scope  
        - Extend model to detect **email spam**  
        - Use **deep learning models** like LSTMs or Transformers  
        - Deploy as a **web service / API** for real-time spam filtering  

        ---
        ## Developed By  
        👨‍💻 Devansh Pandey  
        🎓 Data Science Mini Project  
        """
    )
