import streamlit as st 
import matplotlib.pyplot as plt
import numpy as np

def cal_triangle_area(base, height):
    return 0.5 * base * height 

def plot_triangle(base, height):
    fig, ax = plt.subplots()
    
    # Define triangle vertices
    vertices = np.array([[0, 0], [base, 0], [base/2, height]])
    
    # Create triangle patch
    triangle = plt.Polygon(vertices, fill=True, color='#009efa', alpha=1)
    ax.add_patch(triangle)
    
    ax.set_aspect('equal')
    ax.grid(True)
    ax.set_xlim(-base*0.2, base*1.2)
    ax.set_ylim(-height*0.2, height*1.2)
    ax.set_title(f'Triangle with base {base} and height {height}')
    return fig

st.title("Triangle Calculator")
st.write("This is the calculator app")

base = st.number_input("Base", min_value=0.01)
height = st.number_input("Height", min_value=0.01)

submit_btn = st.button("Submit")

if submit_btn:
    area = cal_triangle_area(base, height)
    st.write(f"Area: {area:.2f} ")
    
    # Display the triangle visualization
    fig = plot_triangle(base, height)
    st.pyplot(fig)