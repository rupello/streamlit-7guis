import streamlit as st

st.write(st.session_state)

# note that using a session as a key in a widget will cause it to be cleared out after
# the page is navigated away from
# see here for workarounds
#   https://stackoverflow.com/questions/74968179/session-state-is-reset-in-streamlit-multipage-app

# Conversion functions
def fahrenheit_to_celsius(f):
    return (f - 32) * 5.0 / 9.0


def celsius_to_fahrenheit(c):
    return 9.0 / 5.0 * c + 32


# Fahrenheit to Celsius conversion
def update_celsius():
    st.session_state.c_temp = fahrenheit_to_celsius(st.session_state.f_temp)

# Celsius to Fahrenheit conversion
def update_fahrenheit():
    st.session_state.f_temp = celsius_to_fahrenheit(st.session_state.c_temp)


# Initialize if one of 'f_temp' or 'c_temp' exist
if 'f_temp' in st.session_state:
    update_celsius()
elif 'c_temp' in st.session_state:
    update_fahrenheit()
else:
    # default
    st.session_state.f_temp = 32.0  # Default Fahrenheit value
    update_celsius()

# Title
st.title('Temperature Conversion App')

st.write("This app converts temperatures between Fahrenheit and Celsius interactively.")

# Fahrenheit input with callback to update Celsius
st.number_input("Enter temperature in Fahrenheit:", step=1.0, key="f_temp", on_change=update_celsius)

# Celsius input with callback to update Fahrenheit
st.number_input("Enter temperature in Celsius:", step=1.0, key="c_temp", on_change=update_fahrenheit)

