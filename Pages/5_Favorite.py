import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# Initialize session state for favorites list
if 'favorites' not in st.session_state:
    st.session_state.favorites = []

st.title("My Favorite Items")
st.write("Add items you like to your collection!")

# Create input form
with st.form(key='favorite_form'):
    col1, col2 = st.columns(2)
    
    with col1:
        item_name = st.text_input("Item Name")
        price = st.number_input("Price", min_value=0.0, step=0.1)
    
    with col2:
        icon = st.selectbox("Select Icon", ["🎮", "📱", "💻", "👕", "👟", "📚", "🎧", "⌚", "🎸", "🎨"])
        collection = st.selectbox("Collection", ["Games", "Electronics", "Fashion", "Books", "Music", "Art", "Other"])
    
    submit_button = st.form_submit_button("Add to Favorites")
    
    if submit_button and item_name:  # Check if item name is not empty
        new_item = {
            "name": item_name,
            "price": price,
            "icon": icon,
            "collection": collection
        }
        st.session_state.favorites.append(new_item)
        st.success(f"Added {icon} {item_name} to your favorites!")

# Display favorites
if st.session_state.favorites:
    st.divider()
    st.subheader("Your Favorite Items")
    
    for idx, item in enumerate(st.session_state.favorites):
        col1, col2, col3 = st.columns([3, 2, 1])
        with col1:
            st.write(f"{item['icon']} {item['name']}")
        with col2:
            st.write(f"${item['price']:.2f}")
        with col3:
            st.write(f"{item['collection']}")
            
    # Add clear button
    if st.button("Clear All Favorites"):
        st.session_state.favorites = []
        st.rerun()