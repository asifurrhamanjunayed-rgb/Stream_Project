import streamlit as st
from api_calling import code_analyzer
from PIL import Image

st.title(":blue[Wellcome to the code analyzer] ")
st.markdown("Upload your image for code analyzing ")
st.divider()

with st.sidebar:
    st.header("Upload your image here: ")
    image = st.file_uploader(
        "Upload your image ",
        type=['jpg', 'jpeg', 'png']
    )
    if image:
        st.image(image)
    else:
        st.error("You must choose one picture")
    option = st.selectbox(
        "Enter you need",
        ("Fix", "Hints"),
        index=None
    )
    if option:
        st.markdown(f"You have selected {option} for your code")

    button = st.button("Press to procced", type="primary")
if image and button and option:
    with st.container(border=True):
        st.subheader("Your solution ")
        image = Image.open(image)
        with st.spinner("Ai is analyzing your code"):
            generated_notes = code_analyzer(image, option)
            st.markdown(generated_notes)
if button and not image:
    st.error("You must choose one picture")
elif button and not option:
    st.error("You must choose one option")
