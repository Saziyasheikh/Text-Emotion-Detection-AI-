##  🎭 Text Emotion Detection AI 

An end-to-end Machine Learning web application that predicts core human emotions (**Joy**, **Sadness**, or **Anger**) from English text inputs in real-time. This project features a robust Scikit-Learn backend pipeline seamlessly integrated with a clean, responsive Streamlit frontend user interface.

Developed as part of the **Hex Softwares Internship (Project 1)**.

## ✨ Features
 **Real-time Prediction:** Input any sentence and get instant emotion classification.
 
 **Smart ML Pipeline:** Powered by TF-IDF Vectorization and a Logistic Regression classifier.

 **Premium UI:** Designed a minimalistic, aesthetic, and user-friendly web interface.
 
 **Dynamic Feedback:** Display context-aware emojis along with clear success states.


##  🛠️ Tech Stack & Libraries
 **Language:** Python 3.x
 
 **Data Processing:** Pandas
 
 **Machine Learning:** Scikit-Learn (TF-IDF Vectorizer, Logistic Regression)
 
 **Model Deployment:** Pickle (for model serialization)
 
 **Frontend Framework:** Streamlit



## 📁 Project Structure
```text

├── train_model.py      # Backend script to clean data, train, and save the ML model
├── app.py              # Frontend Streamlit web application script
├── emotion_model.pkl   # Saved serialized weights of the trained AI model
└── README.md           # Project documentation
