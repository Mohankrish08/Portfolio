import streamlit as st
from streamlit_option_menu import option_menu
import requests
from streamlit_lottie import st_lottie
from PIL import Image
from io import BytesIO

st.set_page_config(
    page_title='Projects',
    page_icon=':books:',
    layout='wide'
)

# Loading assets

Shrimp = Image.open('Images/Shrimp disease montoring system.png')
Sign_lang = Image.open('Images/Hand recognition.png')
pdf = Image.open('Images/Pdf parser.jpg')
knee = Image.open('Images/Knee_bend_exercise.png')
slub = Image.open('Images/Slub.png')
cricket_url = 'https://miro.medium.com/v2/resize:fit:1050/1*lCa5MKZc8oEqjt6wcEFuDQ.jpeg'
rep_url = 'https://purepng.com/public/uploads/large/dumbbells-nzl.png'
pdf_url = 'https://docparser.com/wp-content/uploads/2017/05/pdf-parser.jpg'
face_url = 'https://media.licdn.com/dms/image/D4D12AQEdieBNHt0AXQ/article-cover_image-shrink_600_2000/0/1688448131433?e=2147483647&v=beta&t=wWkYFkLS_JKOvmkW06MCzWHMYvlprnc-weZiTeUteeg'
emotion_url = 'https://acart.com/wp-content/uploads/2017/04/facial-recognition-img2.jpg'
bommer_url = 'https://ozonetel.com/wp-content/uploads/2021/02/voicebot.jpg'

# main

st.title('Projects')

st.write('------------')

# 1. Shrimp disease monitoring system

with st.container():
    
    left_col, right_col = st.columns((1,0.8))
    with right_col:
        st.subheader('Shrimp disease monitoring system')
        st.write('##')
        st.write(
            """
            This project is to monitor and classify the Good shrimp and
            Infected shrimps in the pond, and also send an intimation to
            shrimp farm owners as to how many infected shrimps are in the
            pond.

            """
        )
    with left_col:
        st.image(Shrimp, width=300)

# Sign language classification of a week

with st.container():
    st.write('-----')
    left_col, right_col = st.columns((1,0.8))
    with right_col:
        st.subheader('Sign Language classification using days of a week (LSTM vs GRU)')
        st.write('##')
        st.write(
            """
            This project aims to classify sign language gestures for the days
            of the week using Recurrent Neural Networks (RNNs), This was
            trained by using Google’s Mediapipe Library to Predict the days of
            a week.
    
            """)
        github_sign = "https://github.com/Mohankrish08/Second-brain/blob/main/Computer%20vision/Sign%20languages%20for%20days%20of%20a%20week%20(LSTM%20vs%20GRU)%20.ipynb"
        github_link = f'<a href="{github_sign}" target="_blank"><img src="https://i.pinimg.com/736x/b5/1b/78/b51b78ecc9e5711274931774e433b5e6.jpg" alt="GitHub" style="width: 50px;"></a>'
        st.markdown(github_link, unsafe_allow_html=True)
            
    with left_col:
        #st.subheader('Sign Language classification using days of a week (LSTM vs GRU)')
        st.image(Sign_lang, width=300)

# 3. Cricket insights hub

with st.container():
    st.write('-----')
    left_col, right_col = st.columns((1,0.8))
    with right_col:
        st.subheader('Cricket insights hub')
        st.write('##')
        st.write(
            """
            This project is about Tableau-powered cricket data insights
            project, where we transform raw cricket statistics into visually
            compelling and actionable insights for enthusiasts and
            professionals alike.
            """
        )
    with left_col:
        response_cricket = requests.get(cricket_url)
        cricket = Image.open(BytesIO(response_cricket.content))
        st.image(cricket, width=300)

# 4. Rep counter using Mediapipe


with st.container():
    st.write('-----')
    left_col, right_col = st.columns((1,0.8))
    with right_col:
        st.subheader('Rep counter using Mediapipe')
        st.write('##')
        st.write(
            """
            This project uses the OpenCV library to detect and track the
            movement of an object, such as a weight or a human limb, within
            a video stream.
            """
        )
        github_rep = "https://github.com/Mohankrish08/Second-brain/blob/main/Computer%20vision/Rep%20counter.ipynb"
        github_link = f'<a href="{github_rep}" target="_blank"><img src="https://i.pinimg.com/736x/b5/1b/78/b51b78ecc9e5711274931774e433b5e6.jpg" alt="GitHub" style="width: 50px;"></a>'
        st.markdown(github_link, unsafe_allow_html=True)

    with left_col:
        response_rep = requests.get(rep_url)
        rep = Image.open(BytesIO(response_rep.content))
        st.image(rep, width=300)

# 5. Page parser chatbot

with st.container():
    st.write('-----')
    left_col, right_col = st.columns((1,0.8))
    with right_col:
        st.subheader('Page parser chatbot')
        st.write('##')
        st.write(
            """
            Introducing our innovative project harnessing the power of FAISS
            to convert PDFs into vectors and LLMs like Llama to train models
            for intelligent, book-specific Q&A. Explore a new era of knowledge
            retrieval.
            """
        )
    with left_col:
        st.image(pdf, width=300)

# 6. Face attendance system

with st.container():
    st.write('-----')
    left_col, right_col = st.columns((1,0.8))
    with right_col:
        st.subheader('Face Attendance System')
        st.write('##')
        st.write(
            """
            This project is about creating a Face attendance system using
            face recognition library and dlib to find the face landmarks of the
            person.
            """
        )
    with left_col:
        st.write('##')
        st.image(face_url, width=300)

# 7. Emotion detection

with st.container():
    st.write('-----')
    left_col, right_col = st.columns((1,0.8))
    with right_col:
        st.subheader('Emotion detection')
        st.write('##')
        st.write(
            """
            This project is about human facial emotion detection using
            Facebook’s Deep Face library, it predicts the emotion of the human
            being.
            """
        )
        github_emotion = "https://github.com/Mohankrish08/Second-brain/blob/main/Computer%20vision/Emotion%20detection%20using%20Deepface%20(1).ipynb"
        github_link = f'<a href="{github_emotion}" target="_blank"><img src="https://i.pinimg.com/736x/b5/1b/78/b51b78ecc9e5711274931774e433b5e6.jpg" alt="GitHub" style="width: 50px;"></a>'
        st.markdown(github_link, unsafe_allow_html=True)
    with left_col:
        st.image(emotion_url, width=300)

# 8. Bommer bot

with st.container():
    st.write('-----')
    left_col, right_col = st.columns((1,0.8))
    with right_col:
        st.subheader('Bommer bot')
        st.write('##')
        st.write(
            """
            Automation Echo Bot: Echoing Messages with Precision and Ease Using PyAutoGUI
            """
        )
        github_bot = "https://github.com/Mohankrish08/Second-brain/blob/main/Pyautogui/Boomer%20bot.ipynb"
        github_link = f'<a href="{github_bot}" target="_blank"><img src="https://i.pinimg.com/736x/b5/1b/78/b51b78ecc9e5711274931774e433b5e6.jpg" alt="GitHub" style="width: 50px;"></a>'
        st.markdown(github_link, unsafe_allow_html=True)
    with left_col:
        st.image(bommer_url, width=300)

# 9. Slub analysis

with st.container():
    st.write('-----')
    left_col, right_col = st.columns((1,0.8))
    with right_col:
        st.subheader('Slub Analysis using OpenCV')
        st.write('##')
        st.write(
            """
            This project calculates the distance between slubs, representing the difference between the excellent thread and uneven thread areas in garments. 
            """
        )
        github_slub = "https://github.com/Mohankrish08/Second-brain/blob/main/Computer%20vision/Slub%20Analysis.ipynb"
        github_link = f'<a href="{github_slub}" target="_blank"><img src="https://i.pinimg.com/736x/b5/1b/78/b51b78ecc9e5711274931774e433b5e6.jpg" alt="GitHub" style="width: 50px;"></a>'
        st.markdown(github_link, unsafe_allow_html=True)
    with left_col:
        st.image(slub, width=300)

# 10. Knee bend exercise

with st.container():
    st.write('-----')
    left_col, right_col = st.columns((1,0.8))
    with right_col:
        st.subheader('Knee bend exercise')
        st.write('##')
        st.write(
            """
            This project uses the OpenCV library to detect and track body movements and calculate the knee bending time for the people.
            """
        )
        github_knee = "https://github.com/Mohankrish08/Second-brain/blob/main/Computer%20vision/Knee%20bend%20exercise.ipynb"
        github_link = f'<a href="{github_knee}" target="_blank"><img src="https://i.pinimg.com/736x/b5/1b/78/b51b78ecc9e5711274931774e433b5e6.jpg" alt="GitHub" style="width: 50px;"></a>'
        st.markdown(github_link, unsafe_allow_html=True)
    with left_col:
        st.image(knee, width=300)