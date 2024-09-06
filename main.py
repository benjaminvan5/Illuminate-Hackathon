import streamlit as st
import base64
import datetime

st.set_page_config(page_title="MyMedMate", page_icon=":tada:", layout="wide")

# Data for medication + daily dosage, dosages
data = open('data.txt', 'r')
dosages_track_dictionary = {} 

# converting dosages_track.txt into a dictionary
try:
    with open('dosages_track.txt', 'r') as dosages_read:
        for line in dosages_read:
            medicine, dosage = line.split()
            dosages_track_dictionary[medicine] = dosage

except:
    pass

# print(dosages_track_dictionary)

def clear_text():  # for clearing medicine and dosage
    st.session_state.medicine = ""
    st.session_state.dosage = ""


with st.container():
    left_column, right_column = st.columns((4, 1))

    with left_column:
        st.subheader("Hi, I'm your digital medicine tracker :wave:")
        st.title("MyMedMate")
        st.write(
            "MyMedApp helps patients manage their medications by tracking dosages.")

    # apple gif (an apple a day keeps the doctor away!) https://discuss.streamlit.io/t/how-to-show-local-gif-image/3408/4
    with right_column:
        file_ = open("apple.gif", "rb")
        contents = file_.read()
        data_url = base64.b64encode(contents).decode("utf-8")
        file_.close()
        st.markdown(f'<img src="data:image/gif;base64,{data_url}" width="200">', unsafe_allow_html=True, )

with st.container():
    global file
    st.divider()
    left_column, middle_column, right_column = st.columns((2, 0.7, 2)) # left column is for user medication input, right column is for daily tracker and middle is for separation between the two
    with left_column:
        medicine = st.text_input("What medicine are you currently taking?", key="medicine").title()
        if len(medicine) > 0 and not ("," in medicine): # if user inputs a comma (eg Panadol,) then it causes the dictionary to malfunction hence "and not ("," in medicine)" is added 

            # radio buttons
            medication_form_name = ['Tablet', 'Liquid', 'Capsule', 'Topical']
            medication_form = st.radio('Form of Medication', medication_form_name, index=None)
            with middle_column:
                st.write('#')  # blank text to make units of medication aligned with user input
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
                if len(daily_dosage) > 0: #different forms of medication have different if statements because they have different units (tablets, capsules or mL)
                    if daily_dosage.isdigit() and medication_form == "Liquid":
                        st.write(f"Medicine: {medicine}. Daily Dosage: {daily_dosage} mL")
                        with open('data.txt', 'a') as file:
                            file.write(f"({medicine}, {daily_dosage}),")
                    elif daily_dosage.isdigit() and medication_form == "Topical":
                        st.write(f"Medicine: {medicine}. Daily Dosage: {daily_dosage} mL")
                        with open('data.txt', 'a') as file:
                            file.write(f"({medicine}, {daily_dosage}),")
                    elif daily_dosage.isdigit() and medication_form == "Tablet":
                        st.write(f"Medicine: {medicine}. Daily Dosage: {daily_dosage} tablets")
                        with open('data.txt', 'a') as file:
                            file.write(f"({medicine}, {daily_dosage}),")
                    elif daily_dosage.isdigit() and medication_form == "Capsule":
                        st.write(f"Medicine: {medicine}. Daily Dosage: {daily_dosage} capsules")
                        with open('data.txt', 'a') as file:
                            file.write(f"({medicine}, {daily_dosage}),")
                    else:
                        st.write("Please enter an integer")


        # Medicine input validation. Commas break the dictionary algorithm
        elif len(medicine) == 0 or ',' in medicine:
            st.write("Invalid Medicine Name.")
        medical_information = data.read()
        
    with left_column:
        st.subheader("Our Goal Is To")
        st.write("We aim to assist users with managing their medication effectively by providing an accessible platform for tracking and managing daily medication intake.")
        st.write("Medication non-adherence is a prominent issue worldwide leading to 125,000 deaths in the U.S alone. As a team, we created a suitable software solution in order to combat this pressing issue. We used the python library, streamlit, to create a frontend for a website that reminds users to take their medication. Users input their specific medication, as well as their recommended dosage per day, and once the day is over, the website reminds the user to take their medication.")
        
        # Converts each (medicine, dosage) pair into a key-value element in a dictionary
        if medical_information != "":
            medical_information = medical_information.rstrip(medical_information[-1])
            dictionary = dict([x.split(',') for x in medical_information[1:-1].split('),(')])
        else:
            dictionary = {}
        with open('data.txt', 'r') as file:
            contents = file.read()


    # daily tracker
    if len(dictionary) > 0:
        with right_column:
            st.subheader("Daily Tracker 📅")
            count = 0
            for medicine in dictionary:
                # medicine = medicine[0].upper() + medicine[1:]  # capatalises 1st letter of medicine
                left, right = st.columns((4.9, 0.7))  # column for medicine name and amount of dose taken today

                with left:
                    st.write(f"**{medicine}**")

                col1, col2, col3 = st.columns((1.4, 3.5, 0.7))  # columns for user number input, progess bar and metric (metric is daily dosage and percentage of daily dosage taken)
                
                with col1: # user number input
                    try:
                        dosages = int(dosages_track_dictionary[medicine])
                        dosages = st.number_input("test", value = dosages, step=1, label_visibility="collapsed", key=f'{count}', min_value=0,
                        )
            
                    except:
                        dosages = st.number_input("test", value = 0, step=1, label_visibility="collapsed", key=f'{count}', min_value=0,
                        )



                with col2: # progress bar
                    if dosages <= int(dictionary[medicine]):
                        progress_bar = col2.progress(dosages / int(dictionary[medicine]))
                    else:
                        progress_bar = col2.progress(100)  # max value of progress bar is 100

                with col3: # metric (metric is daily dosage and percentage of daily dosage taken)
                    percent_increase = str(round(dosages / int(dictionary[medicine]) * 100)) + "%"
                    col3.metric(label="secret", value=f"{dictionary[medicine]}", delta=percent_increase,
                            label_visibility="collapsed")

                with right:
                    st.write(f"**{dosages}**")

                count += 1
                
                # Creating a dictionary to save medicine + medicine dosage
                dosages_track_dictionary[medicine] = dictionary.get(None, dosages)

            # Save button saves the dictionary into dosages_track.txt
            global save_button
            save_button = st.button("Save all data")
            if save_button:
                with open('dosages_track.txt', 'w') as dosages_track:
                    for medicine, dosages in dosages_track_dictionary.items():
                        dosages_track.write(f"{medicine.title()} {dosages}\n")

            # Clear button logic
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
                        with open('dosages_track.txt', 'w') as file:
                            pass
                        dosages_track_dictionary = {}
                        st.rerun()

                show_cleardialog()


    with right_column: # medication gif
        file_ = open("meds.gif", "rb")
        contents = file_.read()
        data_url = base64.b64encode(contents).decode("utf-8")
        file_.close()
        st.markdown(f'<img src="data:image/gif;base64,{data_url}" width="400" style="display: block; margin: 0 auto;">', unsafe_allow_html=True)

# if time is 0:0:0.0 then it's a new day so the dosages that the user has taken resets
today = str(datetime.datetime.today())
if today[11] == 0 and today[12] == 0 and today[14] == 0 and today[15] == 0 and today[17] == 0 and today[18] == 0 and today[20]:
    dosages_dictionary = {}
