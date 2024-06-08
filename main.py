import streamlit as st
import pickle

st.set_page_config(page_title="Test Title", page_icon=":tada:", layout="wide")

dictionary = {}

with st.container():
    st.subheader("Hi, I'm your digital medicine tracker :wave:")
    st.title("MyMedMate")
    st.write(
        "MyMedApp helps patients manage their medications by tracking dosages, and providing essential information on potential drug interactions."
    )
    st.divider()
    medicine = st.text_input("What medicine are you currently taking?")
    if type(medicine) == str:
        daily_dosage= st.text_input(f"What is your daily dosage of {medicine}?")
        st.write(medicine, daily_dosage)
    else:
        st.write("Medicine not entered.")
        

placeholder = st.empty()
with placeholder.container():
    st.write("test")
    placeholder.empty()

with open('saved_dictionary.pkl', 'wb') as f:
    pickle.dump(dictionary, f)
        
with open('saved_dictionary.pkl', 'rb') as f:
    dictionary = pickle.load(f)


