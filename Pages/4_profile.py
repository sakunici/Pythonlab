import streamlit as st

# Initialize session state variables
if 'name' not in st.session_state:
    st.session_state.name = ""
if 'phone' not in st.session_state:
    st.session_state.phone = ""
if 'profile_pic' not in st.session_state:
    st.session_state.profile_pic = None

st.title("My Profile")

# Create two columns for layout
col1, col2 = st.columns(2)

with col1:
    # Name input
    name = st.text_input("Name", value=st.session_state.name)
    if name != st.session_state.name:
        st.session_state.name = name
        st.rerun()

    # Phone number input
    phone = st.text_input("Phone Number", value=st.session_state.phone)
    if phone != st.session_state.phone:
        st.session_state.phone = phone
        st.rerun()

with col2:
    # Profile picture upload
    uploaded_file = st.file_uploader("Choose a profile picture", type=['png', 'jpg', 'jpeg'])
    if uploaded_file is not None:
        st.session_state.profile_pic = uploaded_file
        st.image(uploaded_file, caption="Profile Picture", width=200)
    elif st.session_state.profile_pic is not None:
        st.image(st.session_state.profile_pic, caption="Profile Picture", width=200)

# Display profile information
st.divider()
st.subheader("Profile Information")
if st.session_state.name:
    st.write(f" Name: {st.session_state.name}")
if st.session_state.phone:
    st.write(f" Phone: {st.session_state.phone}")

# Add clear button
if st.button("Clear Profile"):
    st.session_state.name = ""
    st.session_state.phone = ""
    st.session_state.profile_pic = None
    st.rerun()





