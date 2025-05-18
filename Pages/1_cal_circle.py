import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

def cal_circle_area(r):
    return 3.14*r*r

def plot_circle(radius):
    # Create figure and axis
    fig, ax = plt.subplots()
    # Create circle with specified color and opacity
    circle = plt.Circle((0, 0), radius, fill=True, color='#00c9a7', alpha=0.3)  
    ax.add_patch(circle)
    ax.set_aspect('equal')
    ax.grid(True)
    # Set view limits
    ax.set_xlim(-radius*1.5, radius*1.5)
    ax.set_ylim(-radius*1.5, radius*1.5)
    ax.set_title(f'Circle with radius {radius}')
    return fig

st.title("Circle calculator")
st.write("This is the calculator app")

radius = st.number_input("Enter radius", min_value=0.1)
submit_btn = st.button("Submit")

if submit_btn:
    circle_area = cal_circle_area(radius)
    st.write(f"The area is {circle_area:.2f}")
    
    # Display the circle visualization
    fig = plot_circle(radius)
    st.pyplot(fig)

