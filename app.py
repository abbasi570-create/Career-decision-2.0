import streamlit as st
import joblib
import numpy as np

st.set_page_config(page_title="Career Decision", page_icon="🎮")

st.title("🎯 Career Prediction Model")
st.caption("Choose options & click predict")

model = joblib.load("career_model.pkl")
career = joblib.load("career.pkl")

cs = st.slider("Computer Skill",1,5,3)
conf = st.slider("Confidence",1,5,3)
cre = st.slider("Creativity",1,5,3)
marks = st.slider("Marks",1,5,3)
lead = st.slider("Leadership",1,5,3)

if st.button("🎉 Predict Career"):
    X = np.array([[cs,conf,cre,marks,lead]])
    pred = model.predict(X)
    st.success("✨ Career Predicted!")
    st.balloons()
