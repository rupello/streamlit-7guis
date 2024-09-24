import streamlit as st

def safe_clear(key):
    if key in st.session_state:
        del st.session_state[key]

if st.button("Temp. Convert -50C"):
    # pass value to convert
    safe_clear('f_temp')
    st.session_state.c_temp = -50.0
    st.switch_page("pages/tempconvert.py")

if st.button("Temp. Convert +50F"):
    # pass value to convert
    safe_clear('c_temp')
    st.session_state.f_temp = 50.0
    st.switch_page("pages/tempconvert.py")
