import streamlit as st
import base64

    
# ----- Page configs (tab title, favicon) -----
st.set_page_config(
<<<<<<< HEAD
    page_title="Albert  Portfolio",
=======
    page_title="Albert's Portfolio",
>>>>>>> dd26482d208c9d0032df04d98d5bc6afaf536c7f
    page_icon="📊",
)


# ----- Left menu -----
with st.sidebar:
    st.image("eae_img.png", width=200)
    st.header("Introduction to Programming Languages for Data")
    st.write("###")
<<<<<<< HEAD
    st.write("***Final Project - March 2025***")
=======
    st.write("***Final Project - Feb 2025***")
>>>>>>> dd26482d208c9d0032df04d98d5bc6afaf536c7f
    st.write("**Author:** Albert Protasio")
    st.write("**Instructor:** [Enric Domingo](https://github.com/enricd)")


# ----- Top title -----
<<<<<<< HEAD
st.write(f"""<div style="text-align: center;"><h1 style="text-align: center;">👋 Hi! My name is Albert </h1></div>""", unsafe_allow_html=True)  # TODO: Add your name
=======
st.write(f"""<div style="text-align: center;"><h1 style="text-align: center;">👋 Hi! My name is Albert</h1></div>""", unsafe_allow_html=True)  # TODO: Add your name
>>>>>>> dd26482d208c9d0032df04d98d5bc6afaf536c7f


import base64
import streamlit as st

import base64
import streamlit as st

# ----- Profile image file -----
profile_image_file_path = "IMG_6994_copy_2.JPG"  # Update with the correct file path

# Open the image file and encode it as base64
with open(profile_image_file_path, "rb") as img_file:
    img = "data:image/jpg;base64," + base64.b64encode(img_file.read()).decode()

# ----- Your Profile Image -----
st.write(f"""
<div style="display: flex; justify-content: center;">
    <img src="{img}" alt="Your Name" width="300" height="300" style="border-radius: 50%; object-fit: cover; margin-top: 40px; margin-bottom: 40px;">
</div>
""", unsafe_allow_html=True)


# ----- Personal title or short description -----
<<<<<<< HEAD
current_role = "Bbig Data & Analytics Masters Student"   # TODO: Change this
=======
current_role = "Big Data & Analytics Master's Student"   # TODO: Change this
>>>>>>> dd26482d208c9d0032df04d98d5bc6afaf536c7f

st.write(f"""<div style="text-align: center;"><h4><i>{current_role}</i></h4></div>""", unsafe_allow_html=True)

st.write("##")    # Adding some space


# ----- About me section -----
st.subheader("About Me")

# TODO: Modify and adapt the following lines to your info, you can add or remove some details if you want
st.write("""
<<<<<<< HEAD
- 🧑‍💻 I am a Big Data & Analytics Masters Student 

- 🛩️ prev: finance, retail, consulting
=======
- 🧑‍💻 I am a Big Data & Analytics Master's student 

- 🛩️ Banking, Retail, Consulting
>>>>>>> dd26482d208c9d0032df04d98d5bc6afaf536c7f

- ❤️ Passionate about constantly learning new things and stepping outside my comfort zone

- 🤖 SQL, Python

- 🏂 Learning a foreign language, reading, sports, music

- 📫 How to reach me: albertprotasio.es@gmail.com

- 🏠 Barcelona
""")

# Feel free to add other points like your Linkedin, Github, Social Media, etc.
