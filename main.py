import streamlit as st
import base64

st.set_page_config(page_title="Test Title", page_icon=":tada:", layout="wide")

data = open('data.txt', 'r')

def clear_text(): # for clearing medicine and dosage
    st.session_state.medicine = ""
    st.session_state.dosage = ""

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
    global file
    st.divider()
    left_column, middle_column, right_column  = st.columns((2,0.7,2))
    with left_column:
        medicine = st.text_input("What medicine are you currently taking?", key="medicine").lower()
        if len(medicine) > 0 and not ("," in medicine):

        #radio buttons
            medication_form_name = ['Tablet', 'Liquid', 'Capsule', 'Topical']
            medication_form = st.radio('Form of Medication', medication_form_name, index = None)
            with middle_column:
                    st.write('#') #blank text to make units of medication aligned with user input
                    st.write('#')
                    st.write('#')

            if medication_form:
                if medication_form == "Tablet":
                    with middle_column:
                        st.write("tablets")
                elif medication_form == "Capsule":
                    with middle_column:
                        st.write("capsules")
                elif medication_form == "Liquid" or medication_form == "Topical":
                    with middle_column:
                        st.write("mL")
                daily_dosage = st.text_input(f"What is your daily dosage of {medicine}?", key="dosage")
                if len(daily_dosage) > 0:
                    if daily_dosage.isdigit() and medication_form == "Liquid":
                        st.write(f"Medicine: {medicine}. Daily Dosage: {daily_dosage} mL")
                        with open('data.txt', 'a') as file:
                            file.write(f"({medicine}, {daily_dosage}),")
                    elif daily_dosage.isdigit() and medication_form == "Topical":
                        st.write(f"Medicine: {medicine}. Daily Dosage: {daily_dosage} mL")
                        with open('data.txt', 'a') as file:
                            file.write(f"({medicine}, {daily_dosage}),")
                    elif daily_dosage.isdigit() and medication_form == "Tablet":
                        st.write(f"Medicine: {medicine}. Daily Dosage: {daily_dosage} tables")
                        with open('data.txt', 'a') as file:
                            file.write(f"({medicine}, {daily_dosage}),")
                    elif daily_dosage.isdigit() and medication_form == "Capsule":
                        st.write(f"Medicine: {medicine}. Daily Dosage: {daily_dosage} capsules")
                        with open('data.txt', 'a') as file:
                            file.write(f"({medicine}, {daily_dosage}),")
                    else:
                        st.write("Please enter an integer")
    
        
        # Medicine input validation
        elif len(medicine) == 0 or ',' in medicine:
            st.write("Invalid Medicine Name.")
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

    # Function for updating dosage to a text file
    def update_dosage():
        with open('dosages.txt', 'a') as file:
            file.write(f"(Medicine: {medicine}. Dosages: {buttons})")
        pass



    # daily tracker
    if len(dictionary) > 0:
        with right_column:
            st.subheader("Daily Tracker 📅")
            count = 0
            for medicine in dictionary:
                medicine = medicine[0].upper() + medicine[1:] # capatalises 1st letter of medicine
                left, right = st.columns((4.9, 0.7)) # column for medicine name and amount of dose taken today
               
                with left:
                    st.write(f"**{medicine}**")
                    
                col1, col2, col3 = st.columns((1.4, 3.5, 0.7)) # columns for user input, progess bar and metric
                
                with col1:
                    buttons = st.number_input("test", step = 1, label_visibility = "collapsed", key = f'{count}', min_value = 0, on_change=update_dosage)
                 
                with col2:
                    if buttons <= int(dictionary[medicine.lower()]):
                        progress_bar = col2.progress(buttons / int(dictionary[medicine.lower()]))
                    else:
                        progress_bar = col2.progress(100) # max value of progress bar is 100
                
                with col3:
                    percent_increase = str(round(buttons / int(dictionary[medicine.lower()]) * 100)) + "%" 
                    col3.metric(label = "secret", value = f"{dictionary[medicine.lower()]}", delta = percent_increase, label_visibility = "collapsed")
                    st.write(f"Medicine: {medicine}. Dosages: {buttons} - debug purposes")
                    
                with right:
                    st.write(f"**{buttons}**")

                count += 1  
            #Clear button logic
            global clear_button
            clear_button = st.button("Clear all data")
            if clear_button:
                @st.experimental_dialog("Clear all entries?", width="small")
                def show_cleardialog():
                    global clear_button, file
                    st.write("Press Confirm if you want to clear all of your medicine and dosage information.")

                    if st.button("Confirm", on_click=clear_text):
                        clear_button = False
                        with open('data.txt', 'w') as file:
                            pass
                        with open('dosages.txt', 'w') as file:
                            pass
                        st.rerun()

                
                show_cleardialog()

placeholder = st.empty()
with placeholder.container():
    st.write("test")
    placeholder.empty()
