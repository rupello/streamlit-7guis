import streamlit as st

# st.write(st.session_state)

# Initialize session states
if 'counter' not in st.session_state:
    st.session_state.counter = 0

# Title
st.title('Counter')


def update_counter():
    st.session_state.counter += 1


st.button(f"Count is {st.session_state.counter}", on_click=update_counter())
