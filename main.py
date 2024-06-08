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
    if type(medicine) != str:
        st.write("Medicine not entered.")
    else:
        st.write(medicine)

placeholder = st.empty()
with placeholder.container():
    st.write("test")
    placeholder.empty()

with open('saved_dictionary.pkl', 'wb') as f:
    pickle.dump(test, f)
        
with open('saved_dictionary.pkl', 'rb') as f:
    loaded_dict = pickle.load(f)


