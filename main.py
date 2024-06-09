import streamlit as st
import base64

st.set_page_config(page_title="Test Title", page_icon=":tada:", layout="wide")

data = open('data.txt', 'r')


with st.container():
    left_column, right_column  = st.columns((4,1))
    
    with left_column:
        st.subheader("Hi, I'm your digital medicine tracker :wave:")
        st.title("MyMedMate")
        st.write("MyMedApp helps patients manage their medications by tracking dosages, and providing essential information on potential drug interactions.")

    # apple gif (an apple a day keeps the doctor away!)
    with right_column:
        file_ = open("apple.gif", "rb")
        contents = file_.read()
        data_url = base64.b64encode(contents).decode("utf-8")
        file_.close()
        st.markdown(f'<img src="data:image/gif;base64,{data_url}" width="200">',unsafe_allow_html=True,)

with st.container():
    st.divider()
    left_column, middle_column, right_column  = st.columns((2,1,2))
    with left_column:
        medicine = st.text_input("What medicine are you currently taking?").lower()
        if len(medicine) > 0:
            if "clear" in medicine:
                st.write("Press Confirm if you want to clear your medicine and dosage information. Otherwise enter the medicine you are currently taking.")
                clear_yes = st.button("Confirm")
                if clear_yes:
                    with open('data.txt', 'w') as file:
                        pass
            else:
                daily_dosage = st.text_input(f"What is your daily dosage of {medicine}?")
                if len(daily_dosage) > 0:
                    if daily_dosage.isdigit():
                        st.write(f"Medicine: {medicine}. Daily Dosage: {daily_dosage}")
                        with open('data.txt', 'a') as file:
                            file.write(f"({medicine}, {daily_dosage}),")
                    else:
                        st.write("Please enter an integer")
    
        
        # Medicine input validation
        elif len(medicine) == 0:
            st.write("Medicine not entered.")
        medical_information = data.read()

        # Converts each (medicine, dosage) pair into a key-value element in a dictionary 
        if medical_information != "":
          medical_information = medical_information.rstrip(medical_information[-1])
          dictionary = dict([x.split(',') for x in medical_information[1:-1].split('),(')])
        else: dictionary = {}
        with open('data.txt', 'r') as file:
            contents = file.read()
            st.write(contents)
            st.write(dictionary)

    # daily tracker
    if len(dictionary) > 0:
        with right_column:
            st.subheader("Daily Tracker")
            count = 0
            for medicine in dictionary:
                medicine = medicine[0].upper() + medicine[1:]
                left, right = st.columns((6, 1))
                with left:
                    st.write(f"**{medicine}**")
                with right:
                    st.write("**3**")
                col1, col2, col3, col4 = st.columns((1,1,4, 1))
                progress_bar = col3.progress(10)
                count += 1 
                with col1:
                    increase = st.button("text", key = count) # adding a unique key removes the error DuplicateWidgetID: There are multiple identical st.selectbox widgets with the same generated key.
                    if increase:
                        pass
                with col2:
                    decrease = st.button("text", key = count + 100)
                    if increase:
                        pass
                with col4:
                    col4.metric(label = "5", value = "7", delta = "10%", label_visibility = "collapsed") 


placeholder = st.empty()
with placeholder.container():
    st.write("test")
    placeholder.empty()
