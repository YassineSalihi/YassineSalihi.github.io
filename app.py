from PIL import Image
import requests
import streamlit as st
from streamlit_lottie import st_lottie

# emojis from : https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="Yassine Salihi", page_icon="🥳", layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# USE LOCAL CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style/style.css")

# ------- Load assets --------------
lottie_coding = load_lottieurl("https://lottie.host/c1ea0a5e-5fe3-40ab-9e35-71b84a2c9be8/ZhRm4gsjJ8.json")
img_about_me = Image.open("images/app_pic.png") # not a very good name
img_java_certif = Image.open("images/java_certif.png")

# ------- HEADER SECTION ------------
with st.container():
    st.subheader("Hi! I am SALIHI Yassine 👋 . And this is my website")
    st.title("future teacher and specialist in IT from Morocco.")
    st.write("I am an ambitious guy, I like to discover new thing, and I want to make the educational system a lot more effective and better")
    # link to my blog : I dont have one yet hehe
    st.write("[Learn more >](https://github.com/YassineSalihi)")


# -------- about me ----------------
with st.container():
    st.write("---") # divider
    # insert two columns 
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("About me")
        st.write("##")
        st.write(
            '''
            I study at ENS-M (École Normale Supérieure de Marrakech).
            - I'm always exploring and testing new things.
            - I'm now starting to make tutorials on some exercises.
            - I love martial arts, hiking, and playing video games (though it's been a while since I last played—I've missed it, haha).
'''
        )
        st.write("[Let's connect >](https://www.linkedin.com/in/yassine-salihi-2b2141359/)")

# I am using LottieFiles : JSON based animation file format --> small files, work on any device
    with right_column: # insert the animation here.
        st_lottie(lottie_coding, height=400, key="teaching") # optional height and key


# --------------- Projects ----------------
with st.container():
    st.write("---")
    st.header("My projects")
    st.write("##")
    st.subheader("Project #1")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        #insert image
        st.image(img_about_me)
    with text_column:
        st.subheader("From a student book : ")
        st.write(
            '''
            I found out that my sibling's private school uses a student book, 
            and I came across an exercise on average calculation that I really liked. 
            What I enjoyed even more was using the Tkinter library—it was new to me, fun, 
            and a bit challenging.

            '''
        )

        st.markdown("[The repository of this project : ](https://github.com/YassineSalihi/app_calcul_moyenne)")


with st.container():
    #st.write("---")
    #st.header("My projects")
    #st.write("##")
    st.subheader("Project #2")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        #insert image
        st.image(img_java_certif)
    with text_column:
        st.subheader("Not the best design, but it got the job done! ")
        st.write(
            '''
            My goal was to create an app for certification management.
            It allows you to create, add, delete, and list existing certifications.
            I also used JFreeChart to make statistics easier to read.
            And yes — it’s a Java Swing project!

            '''
        )

        st.markdown("[The repository of this project : ](https://github.com/YassineSalihi/Gestion-des-cerifications)")


# ------------------------- CONTACT ------------------------
with st.container():
    st.write("---")
    st.header("Get in touch with me 📲")
    st.write("##")

    # changed to my email @
    contact_form = """
    <form action="https://formsubmit.co/salihiy0@gmail.com" method="POST">
     <input type="hidden" name="_captcha" value=false>
     <input type="text" name="name" placeholder="Your name" required>
     <input type="email" name="email" placeholder="Your email" required>
     <textarea name="message" placeholder="Your message here" require></textarea>
     <button type="submit">Send</button>
    </form> 
    
    """

    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()








