import streamlit as st 

st.title("Shape Calculator")
st.write("This is Best Shape Calculator Application")

if 'name' in st.session_state:
    st.write(f"Welcome {st.session_state.name}")

name = st.text_input("Enter your name")
if name:
    st.session_state.name = name
    st.rerun()
    