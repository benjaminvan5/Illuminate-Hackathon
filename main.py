import streamlit as st

st.set_page_config(page_title="Test Title", page_icon=":tada:", layout="wide")


with st.container():
    st.subheader("Hi, I'm your digital medicine tracker :wave:")
    st.title("MyMedMate")
    st.write(
        "MyMedApp helps patients manage their medications by tracking dosages, and providing essential information on potential drug interactions."
    )
    st.divider()
    medicine = st.text_input("What medicine are you currently taking?")
    st.write(medicine)
    st.clear()


