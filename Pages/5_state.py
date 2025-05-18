import streamlit as st 

st.title("State Management Demo")
st.write("This page demonstrates how to use session state in Streamlit")

# Initialize counters in session state
if 'counter_a' not in st.session_state:
    st.session_state.counter_a = 0
if 'counter_b' not in st.session_state:
    st.session_state.counter_b = 0

# Functions to increment counters
def increment_counter_a():
    st.session_state.counter_a += 1

def increment_counter_b():
    st.session_state.counter_b += 1

# Create two columns for the counters
col1, col2 = st.columns(2)

with col1:
    st.subheader("Counter A")
    st.write(f"Value: {st.session_state.counter_a}")
    st.button("Increment A", on_click=increment_counter_a, key="btn_a")

with col2:
    st.subheader("Counter B")
    st.write(f"Value: {st.session_state.counter_b}")
    st.button("Increment B", on_click=increment_counter_b, key="btn_b")

# Display the current session state
st.divider()
st.subheader("Current Session State:")
st.write(st.session_state)