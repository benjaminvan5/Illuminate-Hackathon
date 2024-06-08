import streamlit as st
import pickle
import os

st.set_page_config(page_title="Test Title", page_icon=":tada:", layout="wide")

dictionary = {}


with st.container():
    st.subheader("Hi, I'm your digital medicine tracker :wave:")
    st.title("MyMedMate")
    st.write(
        "MyMedApp helps patients manage their medications by tracking dosages, and providing essential information on potential drug interactions."
    )
    st.divider()
    medicine = st.text_input("What medicine are you currently taking?").lower()
    if len(medicine) > 0:
        daily_dosage= st.text_input(f"What is your daily dosage of {medicine}?")
        if len(daily_dosage) > 0:
            st.write(f"Medicine: {medicine}. Daily Dosage: {daily_dosage}")
            dictionary[medicine] = daily_dosage
            st.write(dictionary)
    elif len(medicine) == 0:
        st.write("Medicine not entered.")
        
# line 32 thing makes nothing appear on screen
placeholder = st.empty()
with placeholder.container():
    st.write("test")
    placeholder.empty()
