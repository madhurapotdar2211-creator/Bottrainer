import streamlit as st
import pandas as pd
from src.nlu_pipeline import predict
from src.evaluator import evaluate
import matplotlib.pyplot as plt
import seaborn as sns
import tempfile
import os
import speech_recognition as sr

st.title("🤖 BotTrainer - LLM Based NLU System")

menu = st.sidebar.selectbox("Choose Option", ["Single Prediction", "Evaluate Model"])

# --------------------------
# SINGLE PREDICTION
# --------------------------

if menu == "Single Prediction":
    st.write("Enter your message via text or voice:")
    
    # 1. Initialize session state to store text
    if "current_text" not in st.session_state:
        st.session_state.current_text = ""

    # 2. Manual Text Input
    user_input = st.text_input("Enter your message", value=st.session_state.current_text)

    # 3. Voice Input
    audio_value = st.audio_input("Record your message")
    if audio_value:
        try:
            r = sr.Recognizer()
            with sr.AudioFile(audio_value) as source:
                audio_data = r.record(source)
                transcribed_text = r.recognize_google(audio_data)
            
            # Update the session state and rerun so the text input reflects the voice
            st.session_state.current_text = transcribed_text
            st.rerun() 
            
        except Exception as e:
            st.error(f"Transcription failed: {e}")

    # 4. Predict Button (Now always visible)
    if st.button("Predict") and user_input:
        result = predict(user_input)
        intent = result["intent"]
        confidence = result["confidence"]
        entities = result["entities"]

        st.success("Prediction Complete")

        col1, col2 = st.columns(2)

        with col1:
            st.metric("🎯 Intent Detected", intent)

        with col2:
            st.metric("📊 Confidence", f"{round(confidence*100,2)} %")

        st.write("📦 Entities")
        st.code(entities, language="json")
# --------------------------
# MODEL EVALUATION
# --------------------------

if menu == "Evaluate Model":
    st.write("Running Evaluation on Sample Data")

    test_data = [
        {"text": "Book flight to Delhi", "intent": "book_flight"},
        {"text": "Order pizza", "intent": "order_food"},
        {"text": "Weather in Pune", "intent": "check_weather"}
    ]

    true_labels = []
    predicted_labels = []

    for item in test_data:
        prediction = predict(item["text"])
        true_labels.append(item["intent"])
        predicted_labels.append(prediction["intent"])

    results = evaluate(true_labels, predicted_labels)

    st.write("### Metrics")
    st.write(results)

    st.write("### Confusion Matrix")
    fig, ax = plt.subplots()
    sns.heatmap(results["confusion_matrix"], annot=True, fmt='d', ax=ax)
    st.pyplot(fig)