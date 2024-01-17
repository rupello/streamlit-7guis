import streamlit as st


# Main page with navigation buttons
st.sidebar.title("Navigation")
if st.sidebar.button("Map"):
    st.switch_page("pages/map.py")
if st.sidebar.button("Temp. Convert"):
    st.switch_page("pages/tempconvert.py")