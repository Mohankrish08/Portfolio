import streamlit as st
import requests
from streamlit_lottie import st_lottie

st.set_page_config(
    page_title='Skills',
    page_icon=':computer:',
    layout='wide'
)

# Loading animations

def loader_url(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Loading assets

lottie_coding = loader_url('https://lottie.host/a2e4e6ab-c839-408b-a17e-01a0973e6dc8/beKMsCTQEy.json')
analytics = loader_url('https://lottie.host/f3850ea7-6153-47ad-9f30-b5013d59d10e/XYTKvi07ZX.json')
ml = loader_url('https://lottie.host/16a080a6-703e-42fa-9c2c-40f0c36a4050/MK19sf2Xbi.json')
dl = loader_url('https://lottie.host/bda8aeca-7063-4fbe-9516-d2666a26daa3/gDPKMOGy8T.json')
frameworks = loader_url('https://lottie.host/34898b06-05bc-4aaf-8646-1536e82bb023/lGwXvMbSnI.json')
editing = loader_url('https://lottie.host/584f11f4-1df5-4f1f-8c30-10e069d8255d/EMGqkesIgY.json')
photography = loader_url('https://lottie.host/fb05dd0c-0a84-4863-8025-90be36039cc5/MVZ90fW9QJ.json')
blog = loader_url('https://lottie.host/0aaf8a89-6260-42b7-ab72-6cd1cb9ebd51/9b9j9EXj0p.json')

# main 

st.title('Professional skills')

st.write('##')
st.write('--------')

left_col, right_col = st.columns([1,0.8])

with right_col:
    st.markdown(
        """
        ## Programming Languages
    
        - **Python**
        - **SQL**
        - **C++**
        """
    )

with left_col:
    st_lottie(lottie_coding, height=250, key='coding')

# Add whitespace between sections
st.write('------')

# Section 2: Data Analysis
st.header('Data Analysis')

left_col, right_col = st.columns((1, 0.8))

with right_col:
    st.markdown(
        """
        ## Data Analysis 
    
        - **Tableau**
        - **Power BI**
        """
    )

with left_col:
    st_lottie(analytics, height=250, key='analytics')

# Add whitespace between sections
st.write('------')

# Section 3: Machine Learning
st.header('Machine Learning')

left_col, right_col = st.columns((1, 0.8))

with right_col:
    st.markdown(
        """
        ## Machine Learning 
            
        - **Supervised**
        - **Unsupervised**
        """
    )

with left_col:
    st_lottie(ml, height=250, key='machine learning')

# Add whitespace between sections
st.write('------')

# Section 4: Deep Learning
st.header('Deep Learning')

left_col, right_col = st.columns((1, 0.8))

with right_col:
    st.markdown(
        """
        ## Deep Learning
    
        - **Computer Vision**
        - **Natural Language Processing**
        """
    )

with left_col:
    st_lottie(dl, height=250, key='Deep learning')

# Add whitespace between sections
st.write('------')

# Section 5: Frameworks
st.header('Frameworks')

left_col, right_col = st.columns((1, 0.8))

with right_col:
    st.markdown(
        """
        ## Frameworks
    
        - **TensorFlow**
        - **PyTorch**
        """
    )

with left_col:
    st_lottie(frameworks, height=250, key='frameworks')

# Add whitespace between sections
st.write('------')

# Section 6: Editing
st.header('Editing')

left_col, right_col = st.columns((1, 0.8))

with right_col:
    st.markdown(
        """
        ## Editing
    
        - **Lightroom CC**
        - **Davinci Resolve**
        """
    )

with left_col:
    st_lottie(editing, height=250, key='editing')

# Add whitespace between sections
st.write('------')

# Section 7: Photographer
st.header('Photographer')

left_col, right_col = st.columns((1, 0.8))

with right_col:
    st.markdown(
        """
        ## Photographer
    
        - **Photography**
        """
    )

with left_col:
    st_lottie(photography, height=250, key='photographer')


st.write('----------')

# Section 8: Blogger

st.header('Blogging')

left_col, right_col = st.columns((1,0.8))

with right_col:
    st.markdown(
        """
        ## Blogger

        - **Technical**
        - **Non-Technical**
        """
    )
with left_col:
    st_lottie(blog, height=250, key='blog')