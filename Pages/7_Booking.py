import streamlit as st
from datetime import datetime, time
import pandas as pd

# Initialize session state for bookings
if 'bookings' not in st.session_state:
    st.session_state.bookings = []
if 'editing_idx' not in st.session_state:
    st.session_state.editing_idx = None

st.title("📅 Appointment Booking System")
st.write("Schedule and manage your appointments")

# Create booking form
with st.form(key='booking_form'):
    col1, col2 = st.columns(2)
    
    with col1:
        date = st.date_input("Select Date", min_value=datetime.today())
        time_slot = st.time_input("Select Time", value=time(9, 0))
        name = st.text_input("Name")
    
    with col2:
        phone = st.text_input("Phone Number")
        email = st.text_input("Email")
        notes = st.text_area("Notes", height=100)
    
    if st.session_state.editing_idx is not None:
        submit_button = st.form_submit_button("Update Appointment")
    else:
        submit_button = st.form_submit_button("Book Appointment")
    
    if submit_button and name and phone:  # Validate required fields
        appointment = {
            "date": date,
            "time": time_slot,
            "name": name,
            "phone": phone,
            "email": email,
            "notes": notes
        }
        
        if st.session_state.editing_idx is not None:
            # Update existing appointment
            st.session_state.bookings[st.session_state.editing_idx] = appointment
            st.session_state.editing_idx = None
            st.success("Appointment updated successfully!")
        else:
            # Add new appointment
            st.session_state.bookings.append(appointment)
            st.success("Appointment booked successfully!")
        
        st.rerun()

# Display bookings
if st.session_state.bookings:
    st.divider()
    st.subheader("Your Appointments")
    
    # Convert bookings to DataFrame for better display
    df = pd.DataFrame(st.session_state.bookings)
    
    for idx, booking in enumerate(st.session_state.bookings):
        with st.expander(f"📌 {booking['date'].strftime('%Y-%m-%d')} - {booking['time'].strftime('%H:%M')} - {booking['name']}"):
            col1, col2, col3 = st.columns([3, 1, 1])
            
            with col1:
                st.write(f"**Date:** {booking['date'].strftime('%Y-%m-%d')}")
                st.write(f"**Time:** {booking['time'].strftime('%H:%M')}")
                st.write(f"**Name:** {booking['name']}")
                st.write(f"**Phone:** {booking['phone']}")
                if booking['email']:
                    st.write(f"**Email:** {booking['email']}")
                if booking['notes']:
                    st.write(f"**Notes:** {booking['notes']}")
            
            with col2:
                if st.button("✏️ Edit", key=f"edit_{idx}"):
                    st.session_state.editing_idx = idx
                    st.rerun()
            
            with col3:
                if st.button("🗑️ Delete", key=f"delete_{idx}"):
                    st.session_state.bookings.pop(idx)
                    st.rerun()

    # Add export functionality
    if st.button("Export Appointments (CSV)"):
        df.to_csv("appointments.csv", index=False)
        st.success("Appointments exported to appointments.csv!")

# Clear all appointments button
if st.session_state.bookings:
    if st.button("Clear All Appointments"):
        st.session_state.bookings = []
        st.session_state.editing_idx = None
        st.rerun()