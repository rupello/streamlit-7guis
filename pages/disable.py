import streamlit as st

# Initialize session state for button states
if 'button1_clicked' not in st.session_state:
    st.session_state.button1_clicked = False
if 'button2_clicked' not in st.session_state:
    st.session_state.button2_clicked = False
if 'button3_clicked' not in st.session_state:
    st.session_state.button3_clicked = False

def reset_buttons():
    st.session_state.button1_clicked = False
    st.session_state.button2_clicked = False
    st.session_state.button3_clicked = False

# Main app
st.title("Button Click App")

# Button 1
if st.button("Button 1", disabled=st.session_state.button2_clicked or st.session_state.button3_clicked):
    st.session_state.button1_clicked = True

# Button 2
if st.button("Button 2", disabled=st.session_state.button1_clicked or st.session_state.button3_clicked):
    st.session_state.button2_clicked = True

# Button 3
if st.button("Button 3", disabled=st.session_state.button1_clicked or st.session_state.button2_clicked):
    st.session_state.button3_clicked = True

# Reset button
if st.button("Reset Buttons"):
    reset_buttons()

# Display which button was clicked
if st.session_state.button1_clicked:
    st.write("Button 1 was clicked")
elif st.session_state.button2_clicked:
    st.write("Button 2 was clicked")
elif st.session_state.button3_clicked:
    st.write("Button 3 was clicked")
