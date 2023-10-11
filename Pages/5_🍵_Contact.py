import streamlit as st
import requests
from streamlit_lottie import st_lottie


st.set_page_config(page_title='Buy me coffee',
                   page_icon=':coffee:',
                   layout="wide")



st.header(":mailbox: Get in Touch With Me!!")

st.write('##')

# Loading animations
def loader_url(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


# Loading assets

contact = loader_url('https://lottie.host/7ee946ba-c32d-4297-bcfc-16c641eec4a6/zq1SAVkTjW.json')

# main 

left_col, right_col = st.columns((3,2))

with left_col:
    contact_form = """
    <form action="https://formsubmit.co/mohankrishce@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here"></textarea>
        <button type="submit">Send</button>
    </form>

    """

    st.markdown(contact_form, unsafe_allow_html=True)

with right_col:
    st_lottie(contact, height=250, key='contact')


# Using local css file

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("Styles/styles.css")