import streamlit as st 
def cal_rectangle_area(w, h):
    return w * h 

st.title("Rectangle Calculator")
st.write("This is the calculator app")

w = st.number_input("Width")
h = st.number_input("Height")

    
submit_btn = st.button("sumbit")

if submit_btn:
    area = cal_rectangle_area(w, h)
    st.write(f"Area: {area}")