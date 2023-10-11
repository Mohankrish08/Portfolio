import streamlit as st
import requests
from streamlit_lottie import st_lottie

st.set_page_config(
    page_title='Experience',
    page_icon='sparkle',
    layout='wide'
)

# Loading animations

def loader_url(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Loading assets

Research = loader_url('https://lottie.host/4c09451b-180b-4eb2-85b2-5687d4ec1c8f/d6CdFJLFCS.json')
forge = loader_url('https://lottie.host/34e35eed-6899-4577-8172-afaaf67ea906/Cwpk9xbX2v.json')
photo = loader_url('https://lottie.host/18779cba-e867-4be8-a2af-2254821e5e6f/KSGUqsk06X.json')


st.title('Experiences')

st.write('##')
st.write('--------')

# 1. Research intern

left_col, right_col = st.columns([1,0.8])

with right_col:
    st.markdown(
        """
        ## Research Internship

        ### Working for professor
         
        #### (University of Iowa)
    
        - **Large learning models**
        - **Mutli models**
        """
    )

with left_col:
    st_lottie(Research, height=250, key='coding')


st.write('--------')

# 2. Forge

left_col, right_col = st.columns([1,0.8])

with right_col:
    st.markdown(
        """
        ## Forge innovation and ventures
    
        - Innovation Engineer at ForgeInnovation and ventures
        - Gained experience in how to solve the problem.
        """
    )
    st.markdown(
        """
        <div style="font-size: 24px; color: #fff; animation: fade-in 2s ease 1s 1 both;">
            <b>Duration:</b> Jan 2023 - Jun 2023    
        </div>
        """,
        unsafe_allow_html=True)

with left_col:
    st_lottie(forge, height=250, key='innovation')


st.write('---------')

# 3. Studio 

left_col, right_col = st.columns([1,0.8])

with right_col:
    st.markdown(
        """
        ## Studio KCT
        

    
        - Professional Photographer at Studio KCT
        - Gained different photography techniques.
        """
    )
    st.markdown(
        """
        <div style="font-size: 24px; color: #fff; animation: fade-in 2s ease 1s 1 both;">
            <b>Duration:</b> Oct 2021 - May 2022
        </div>
        """,
        unsafe_allow_html=True)
    

with left_col:
    
    st_lottie(photo, height=250, key='photography')


