import streamlit as st
import requests
from streamlit_lottie import st_lottie
from streamlit_option_menu import option_menu
from PIL import Image

# Setting the page
st.set_page_config(
    page_title="Mohan's Portfolio",
    page_icon=':rocket:',
    layout="wide"
)


# Loading animations
def loader_url(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# URLs for links
github_url = "https://github.com/Mohankrish08"
linkedin_url = "https://www.linkedin.com/in/mohan-krishnan-o-158417201/"
kaggle_url = "https://www.kaggle.com/mohankrishnan08"
medium_url = "https://medium.com/@mohankrishce"

# HTML to load the links
github_link = f'<a href="{github_url}" target="_blank"><img src="https://i.pinimg.com/736x/b5/1b/78/b51b78ecc9e5711274931774e433b5e6.jpg" alt="GitHub" style="width: 100px;"></a>'
linkedin_link = f'<a href="{linkedin_url}" target="_blank"><img src="https://cdn1.iconfinder.com/data/icons/logotypes/32/circle-linkedin-512.png" alt="LinkedIn" style="width: 90px;"></a>'
kaggle_link = f'<a href="{kaggle_url}" target="_blank"><img src="https://cdn4.iconfinder.com/data/icons/logos-and-brands/512/189_Kaggle_logo_logos-512.png" alt="Kaggle" style="width: 90px;"></a>'
medium_link = f'<a href="{medium_url}" target="_blank"><img src="https://miro.medium.com/v2/resize:fit:2400/1*sHhtYhaCe2Uc3IU0IgKwIQ.png" alt="Medium" style="width: 90px;"></a>'
# Loading assets
my_photo = Image.open('Images/My_photo.png')

st.sidebar.success('Select an option above')

# Containers to organize the code
with st.container():
    left_col, right_col = st.columns([3, 1])
    with left_col:
        st.title("Hi! I'm Mohan Krishnan O")
        st.subheader("Final year at KCT")
        st.write('##')
        st.write(
            """
            As an AI & Data Science Enthusiast and an Undergraduate Student
            at KCT'24, majoring in Artificial Intelligence & Data Science, I am
            actively working on projects based on Machine Learning and Data
            Science. I consider myself a critical thinker, passionately curious,
            and a problem solver. Additionally, I am obsessed with
            photography. Being a fast learner, I always make sure to learn
            from my mistakes. Currently, I am eagerly looking for an
            Internship/Job in my area of expertise to apply my knowledge and
            contribute to consistent growth.
            """
        )
        st.write('##')
        git_col, lin_col, kaggle_col, medium_col = st.columns(4)
        with git_col:
            st.markdown(github_link, unsafe_allow_html=True)
        with lin_col:
            st.markdown(linkedin_link, unsafe_allow_html=True)
        with kaggle_col:
            st.markdown(kaggle_link, unsafe_allow_html=True)
        with medium_col:
            st.markdown(medium_link, unsafe_allow_html=True)
    with right_col:
        st.write('##')
        st.image(my_photo, width=300)

