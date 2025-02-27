import streamlit as st
import base64

    
# ----- Page configs (tab title, favicon) -----
st.set_page_config(
    page_title="Albert Protasio's Portfolio",
    page_icon="📊",
)


# ----- Left menu -----
with st.sidebar:
    st.image("eae_img.png", width=200)
    st.header("Introduction to Programming Languages for Data")
    st.write("###")
    st.write("*Final Project - March 2025*")
    st.write("Author: Albert Protasio")
    st.write("Instructor: [Enric Domingo](https://github.com/enricd)")


# ----- Top title -----
<<<<<<< HEAD
st.write(f"""<div style="text-align: center;"><h1 style="text-align: center;">👋 Hi! My name is Fabrizio Troche 🐐</h1></div>""", unsafe_allow_html=True)  # TODO: Add your name


# ----- Profile image file -----
profile_image_file_path = "profile.png"       # TODO: Upload your profile image to the same folder as this script and update this if it has a different name

with open(profile_image_file_path, "rb") as img_file:
    img = "data:image/png;base64," + base64.b64encode(img_file.read()).decode()
=======
st.write(f"""<div style="text-align: center;"><h1 style="text-align: center;">👋 Hi! My name is Albert Protasio </h1></div>""", unsafe_allow_html=True)  # TODO: Add your name


# ----- Profile image file -----
profile_image_file_path = "IMG_6994_copy_2.JPG"       # TODO: Upload your profile image to the same folder as this script and update this if it has a different name

with open(profile_image_file_path, "rb") as img_file:
    img = "data:image/jpeg;base64," + base64.b64encode(img_file.read()).decode()
>>>>>>> 83abc120af88aedb8a2b09fb9534032aa1de1b2f


# ----- Your Profile Image -----
st.write(f"""
<div style="display: flex; justify-content: center;">
    <img src="{img}" alt="Your Name" width="300" height="300" style="border-radius: 50%; object-fit: cover; margin-top: 40px; margin-bottom: 40px;">
</div>
""", unsafe_allow_html=True)


# ----- Personal title or short description -----
<<<<<<< HEAD
current_role = "Assistant Key Account Manager Intern and Big Data & Analytics Master's Student"   # TODO: Change this
=======
current_role = "Assistant Key Account Manager Intern at ManoMano"   # TODO: Change this
>>>>>>> 83abc120af88aedb8a2b09fb9534032aa1de1b2f

st.write(f"""<div style="text-align: center;"><h4><i>{current_role}</i></h4></div>""", unsafe_allow_html=True)

st.write("##")    # Adding some space


# ----- About me section -----
st.subheader("About Me")

# TODO: Modify and adapt the following lines to your info, you can add or remove some details if you want
st.write("""
<<<<<<< HEAD
- 🧑‍💻 I am an intern for ManoMano, an e-commerce company, while pursuing a Master's in Big Data & Analytics degree

- 🛩️ prev: Banking, Retail, Consulting

- ❤️ Learning, literature, languages, sports, and getting to know people

- 🤖 My personal project is myself and my personal and professional development 

- 🏂 Sports, music, reading
=======
- 🧑‍💻 I am an Assistant Key Account Manager at ManoMano and a Master's in Big Data & Analytics student

- 🛩️ prev: Banking, Retail, Consulting

- ❤️ Sports, Music, Books, People

- 🤖 My personal project is to develop myself

- 🏂 Sports, Music, Books
>>>>>>> 83abc120af88aedb8a2b09fb9534032aa1de1b2f

- 📫 How to reach me: albertprotasio.es@gmail.com

- 🏠 Barcelona
""")

# Feel free to add other points like your Linkedin, Github, Social Media, etc.
