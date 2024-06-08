import streamlit as st

st.set_page_config(page_title="Test Title", page_icon=":tada:", layout="wide")

data = open('data.txt', 'r')
medical_information = data.read()
if medical_information != "":
  medical_information = medical_information.rstrip(medical_information[-1])
  dictionary = dict([x.split(',') for x in medical_information[1:-1].split('),(')])
else: dictionary = {}

with st.container():
    st.subheader("Hi, I'm your digital medicine tracker :wave:")
    st.title("MyMedMate")
    st.write(
        "MyMedApp helps patients manage their medications by tracking dosages, and providing essential information on potential drug interactions."
    )
    st.divider()
    medicine = st.text_input("What medicine are you currently taking?").lower()
    if len(medicine) > 0:
        if "clear" in medicine:
            with open('data.txt', 'w') as file:
                pass
        daily_dosage = st.text_input(f"What is your daily dosage of {medicine}?")
        if len(daily_dosage) > 0:
            st.write(f"Medicine: {medicine}. Daily Dosage: {daily_dosage}")
            with open('data.txt', 'a') as file:
                file.write(f"({medicine}, {daily_dosage}),")
    elif len(medicine) == 0:
        st.write("Medicine not entered.")

    with open('data.txt', 'r') as file:
        contents = file.read()
        st.write(contents)
        st.write(dictionary)




placeholder = st.empty()
with placeholder.container():
    st.write("test")
    placeholder.empty()
