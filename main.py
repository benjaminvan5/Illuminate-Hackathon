import streamlit as st

st.set_page_config(page_title="Test Title", page_icon=":tada:", layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

with st.container():
    st.subheader("subheading")
    st.title("title")
    st.write(
        f"text"
    )
    st.write("[Learn More >](Hi")
