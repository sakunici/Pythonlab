import random
from streamlit_d3_demo import d3_line
import streamlit as st

def generate_random_data(x_r, y_r):
    return list(zip(range(x_r), [random.randint(0, y_r) for _ in range(x_r)]))

st.title("X & Y Chart")
st.write("Demo Your Chart Here!")

# Add form for user input
with st.form("chart_params"):
    col1, col2 = st.columns(2)
    
    with col1:
        x_range = st.number_input("Number of points (X-range)", 
                                min_value=5, 
                                max_value=50, 
                                value=5)
    
    with col2:
        y_range = st.number_input("Maximum Y value", 
                                min_value=100, 
                                max_value=1000, 
                                value=100)
    
    submit_btn = st.form_submit_button("Generate Chart")

# Generate and display chart when form is submitted
if submit_btn:
    data = generate_random_data(x_range, y_range)
    d3_line(data, circle_radius=15, circle_color="#ff6f91")