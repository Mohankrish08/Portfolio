import streamlit as st
import requests
from streamlit_lottie import st_lottie
from streamlit_option_menu import option_menu
from PIL import Image
from io import BytesIO

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
lottie_coding = loader_url('https://lottie.host/a2e4e6ab-c839-408b-a17e-01a0973e6dc8/beKMsCTQEy.json')
analytics = loader_url('https://lottie.host/f3850ea7-6153-47ad-9f30-b5013d59d10e/XYTKvi07ZX.json')
ml = loader_url('https://lottie.host/16a080a6-703e-42fa-9c2c-40f0c36a4050/MK19sf2Xbi.json')
dl = loader_url('https://lottie.host/bda8aeca-7063-4fbe-9516-d2666a26daa3/gDPKMOGy8T.json')
frameworks = loader_url('https://lottie.host/34898b06-05bc-4aaf-8646-1536e82bb023/lGwXvMbSnI.json')
editing = loader_url('https://lottie.host/584f11f4-1df5-4f1f-8c30-10e069d8255d/EMGqkesIgY.json')
photography = loader_url('https://lottie.host/fb05dd0c-0a84-4863-8025-90be36039cc5/MVZ90fW9QJ.json')
blog = loader_url('https://lottie.host/0aaf8a89-6260-42b7-ab72-6cd1cb9ebd51/9b9j9EXj0p.json')
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
Research = loader_url('https://lottie.host/4c09451b-180b-4eb2-85b2-5687d4ec1c8f/d6CdFJLFCS.json')
forge = loader_url('https://lottie.host/34e35eed-6899-4577-8172-afaaf67ea906/Cwpk9xbX2v.json')
photo = loader_url('https://lottie.host/18779cba-e867-4be8-a2af-2254821e5e6f/KSGUqsk06X.json')
contact = loader_url('https://lottie.host/7ee946ba-c32d-4297-bcfc-16c641eec4a6/zq1SAVkTjW.json')





# st.sidebar.success('Select an option above')

with st.sidebar:
    with st.container():
        l, m, r = st.columns((1,3,1))
        with l:
            st.empty()
        with m:
            st.empty()
        with r:
            st.empty()
    
    choose = option_menu(
                        "Mohan krish!", 
                        ["About Me", "Professional Skills", "Projects", "Experience", "Contact"],
                         icons=["personfill", "books", "Star", "missle", "Coffee"],
                         menu_icon="mortarboard", 
                         default_index=0,
                         styles={
        "container": {"padding": "0!important", "background-color": "#000000"},
        "icon": {"color": "darkorange", "font-size": "20px"}, 
        "nav-link": {"font-size": "17px", "text-align": "left", "margin":"0px", "--hover-color": "gray"},
        "nav-link-selected": {"background-color": "gray"},
    }
    )
if choose == "About Me":
    #aboutme.createPage()
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

## elif for Professional skills       

elif choose == "Professional Skills":
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

## Projects section

elif choose == "Projects":
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


## Experience section 
elif choose == "Experience":
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
            <div style="font-size: 24px; color: #fff; animation: fade-in 2s ease 1s 1 both;">
                <b>Duration:</b> Jan 2023 - Jun 2023    
            </div>
            
            
        
            - Innovation Engineer at ForgeInnovation and ventures
            - Gained experience in how to solve the problem.
            """, unsafe_allow_html=True
        )
        

    with left_col:
        st_lottie(forge, height=250, key='innovation')


    st.write('---------')

    # 3. Studio 

    left_col, right_col = st.columns([1,0.8])

    with right_col:
        st.markdown(
            """
            ## Studio KCT
            
            <div style="font-size: 24px; color: #fff; animation: fade-in 2s ease 1s 1 both;">
                <b>Duration:</b> Oct 2021 - May 2022
            </div>

            

            - Professional Photographer at Studio KCT
            - Gained different photography techniques.
            """, unsafe_allow_html=True
        )
    
        

    with left_col:
        
        st_lottie(photo, height=250, key='photography')


## Contact section

elif choose == "Contact":
    st.header(":mailbox: Get in Touch With Me!!")

    st.write('##')
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