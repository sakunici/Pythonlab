import streamlit as st 
import matplotlib.pyplot as plt

def cal_rectangle_area(w, h):
    return w * h 

def plot_rectangle(width, height):
    fig, ax = plt.subplots()
    rectangle = plt.Rectangle((0, 0), width, height, fill=True, color='#845ec2', alpha=0.3)
    ax.add_patch(rectangle)
    ax.set_aspect('equal')
    ax.grid(True)
    ax.set_xlim(-width*0.2, width*1.2)
    ax.set_ylim(-height*0.2, height*1.2)
    ax.set_title(f'Rectangle {width} x {height}')
    return fig

st.title("Rectangle Calculator")
st.write("This is the calculator app")

w = st.number_input("Width", min_value=0.01)
h = st.number_input("Height", min_value=0.01)

submit_btn = st.button("Submit")

if submit_btn:
    area = cal_rectangle_area(w, h)
    st.write(f"Area: {area:.2f} ")
    
    # Display the rectangle visualization
    fig = plot_rectangle(w, h)
    st.pyplot(fig)