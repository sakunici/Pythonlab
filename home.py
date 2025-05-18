import streamlit as st



def cal_rectangle_area(w,h):
    return w * h

area = cal_rectangle_area(10,2)

print ("the area is " + str(area))
print (f"the area is {area}" )

def cal_circle_area(r):
    return 3.14*r*r

circle_area = cal_circle_area(4)

print ("the area is " + str(circle_area))
print (f"the area is {circle_area}" )

st.title("Shape calculator")
st.write("This is the calculator app")

import streamlit as st
from streamlit_chat import message

message("My message") 
message("Hello bot!", is_user=True)  # align's the message to the right
