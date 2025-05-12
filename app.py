import streamlit as st

# emojis from : https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="Yassine Salihi", page_icon="🥳", layout="wide")

# ------- Load assets --------------
lottie_coding = "https://lottie.host/5916a905-a131-4a93-a6e2-121e9f0de580/2Q3SJEITJu.lottie"


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
    with right_column:


