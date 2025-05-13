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

# ------- Load assets --------------
lottie_coding = load_lottieurl("https://lottie.host/c1ea0a5e-5fe3-40ab-9e35-71b84a2c9be8/ZhRm4gsjJ8.json")


# ------- HEADER SECTION ------------
with st.container():
    st.subheader("Hi! I am SALIHI Yassine 👋 . And this is my website")
    st.title("futur teacher and specialist in IT from Morocco.")
    st.write("I am an ambitious guy, I like to discover new thing, and I want to make the educational system a lot effective and better")
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
            I study at ENS-M (Ecole Normale Superieure Marrakech)
            - I always test new things.
            - I am now starting making tutos about some exercices.
            - I love martials art, hiking and playing video games (It was a long time since I played a game,I missed it haha)
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
    image_column, text_column = st.columns((1, 2))
    with image_column:
        #insert image
    with text_column:
        st.subheader("From a student book : ")
        st.write(
            '''
            I found out that there is a student book (for private school) used by my sibling
            and I Liked an exercice about the average calculation, but what I liked more is 
            using tkinter biblio which was new, fun and challenging a bit.

            '''
        )

        st.markdown("[The repository of this project : ](https://github.com/YassineSalihi/app_calcul_moyenne)")


