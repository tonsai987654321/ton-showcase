import streamlit as st

# st.title('😎Ton data showcase')
st.markdown("<h1 style='text-align: center; color: #BD98E3;'>😎Ton data showcase</h1>", unsafe_allow_html=True)


st.write("")
st.write('My first time with Streamlit🐔')


placeholder = st.empty()
status = st.radio("This is just a radio",
                  ["Success","Error"])

if status == "Error":
    placeholder.error("I told you it just a radio")
else:
    placeholder.success("IT JUST A RADIO!")
