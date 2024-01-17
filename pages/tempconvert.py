import streamlit as st


# Conversion functions
def fahrenheit_to_celsius(f):
    return (f - 32) * 5.0 / 9.0


def celsius_to_fahrenheit(c):
    return 9.0 / 5.0 * c + 32


# Initialize session states
if 'f_temp' not in st.session_state:
    st.session_state.f_temp = 32.0  # Default Fahrenheit value

if 'c_temp' not in st.session_state:
    st.session_state.c_temp = 0.0  # Default Celsius value

# Title
st.title('Temperature Conversion App')

st.write("This app converts temperatures between Fahrenheit and Celsius interactively.")


# Fahrenheit to Celsius conversion
def update_celsius():
    st.session_state.c_temp = fahrenheit_to_celsius(st.session_state.f_temp)


# Celsius to Fahrenheit conversion
def update_fahrenheit():
    st.session_state.f_temp = celsius_to_fahrenheit(st.session_state.c_temp)


# Fahrenheit input with callback to update Celsius
st.number_input("Enter temperature in Fahrenheit:", step=1.0, key="f_temp", on_change=update_celsius)

# Celsius input with callback to update Fahrenheit
st.number_input("Enter temperature in Celsius:", step=1.0, key="c_temp", on_change=update_fahrenheit)

