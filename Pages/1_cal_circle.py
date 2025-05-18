import streamlit as st

def cal_circle_area(r):
    return 3.14*r*r

circle_area = cal_circle_area(4)

print ("the area is " + str(circle_area))
print (f"the area is {circle_area}" )

st.title("Circle calculator")
st.write("This is the calculator app")

radius = st.number_input ("Enter radius")
submit_btn = st.button ("Submit")
if submit_btn:
    circle_area = cal_circle_area(radius)
    st.write(f"the area is {circle_area} " )

