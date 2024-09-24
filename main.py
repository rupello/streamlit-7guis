import streamlit as st

st.write(st.session_state)

# Main page with navigation buttons
st.sidebar.title("Navigation")
if st.sidebar.button("Map"):
    st.switch_page("pages/map.py")
if st.sidebar.button("Temp. Convert 100F"):
    # pass value to convert
    st.session_state.f_temp = 100.0
    st.switch_page("pages/tempconvert.py")
if st.sidebar.button("Temp. Convert 0C"):
    # pass value to convert
    st.session_state.c_temp = 0.0
    st.switch_page("pages/tempconvert.py")
