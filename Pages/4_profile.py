import streamlit as st 

st.set_page_config(
    page_title="Portfolio",
    page_icon=":guardsman:",
    layout="wide",
    initial_sidebar_state="expanded",
)

if 'name' in st.session_state:
    st.write(f"Hello {st.session_state.name}")

name = st.text_input("Enter your name")
if name:
    st.session_state.name = name
    st.rerun()




