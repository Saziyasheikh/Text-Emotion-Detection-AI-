import streamlit as st
import pickle

st.set_page_config(page_title="Emotion Detector AI", page_icon="🎭", layout="centered")

st.title("🎭 Text Emotion Detection AI")
st.write("Hex Softwares Internship - Project 1")
st.markdown("---")

# Model load karne ki koshish karenge
try:
    with open("emotion_model.pkl", "rb") as file:
        model = pickle.load(file)
except:
    with open("C:/Users/hp/AppData/Local/Programs/Microsoft VS Code/emotion_model.pkl", "rb") as file:
        model = pickle.load(file)

user_input = st.text_area("Apna text yahan likho (English mein):", placeholder="Type here, e.g., I am so happy today...")

if st.button("Predict Emotion", type="primary"):
    if user_input.strip() != "":
        prediction = model.predict([user_input])[0]
        emojis = {"joy": "😊 JOY", "sadness": "😢 SADNESS", "anger": "😡 ANGER"}
        result = emojis.get(prediction.lower(), prediction.upper())
        st.success(f"### Detected Emotion: **{result}**")
    else:
        st.warning("Pehle kuch text toh likho!")