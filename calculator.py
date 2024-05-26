import streamlit as st

# Function to perform the operation
def calculate(num1, num2, operation):
    if operation == 'Add':
        return num1 + num2
    elif operation == 'Subtract':
        return num1 - num2
    elif operation == 'Multiply':
        return num1 * num2
    elif operation == 'Divide':
        try:
            return num1 / num2
        except ZeroDivisionError:
            return "Cannot divide by zero!"

# Streamlit app
st.title('Advanced Calculator')

# Input fields for numbers
num1 = st.number_input('Enter first number', format='%f')
num2 = st.number_input('Enter second number', format='%f')

# Operation selection
operation = st.radio('Select an operation:', ('Add', 'Subtract', 'Multiply', 'Divide'))

# Button to perform calculation
if st.button('Calculate'):
    result = calculate(num1, num2, operation)
    st.success(f'The result is: {result}')

# History log feature
if 'history' not in st.session_state:
    st.session_state.history = []

if st.button('Add to History'):
    st.session_state.history.append((num1, num2, operation, result))
    st.success('Added to history!')

# Display history
if st.checkbox('Show History'):
    for entry in st.session_state.history:
        st.write(f'{entry[0]} {entry[2]} {entry[1]} = {entry[3]}')

# Dictionary to hold conversion factors
conversion_factors = {
    'length': {
        'meters': 1,  # base unit for length is meters
        'kilometers': 0.001,
        'centimeters': 100,
        'millimeters': 1000,
        'miles': 0.000621371,
        'yards': 1.09361,
        'feet': 3.28084,
        'inches': 39.3701
    },
    # You can add more categories like 'weight', 'volume', etc.
}

# Function to convert units
def convert_units(category, value, from_unit, to_unit):
    try:
        # Convert to base unit first
        base_value = value * conversion_factors[category][from_unit]
        # Then convert to the target unit
        return base_value * (1 / conversion_factors[category][to_unit])
    except KeyError:
        return "Invalid unit!"

# Streamlit UI for unit conversion
st.subheader('Unit Conversion')
category = st.selectbox('Select a category:', list(conversion_factors.keys()))
from_unit = st.selectbox('From:', list(conversion_factors[category].keys()))
to_unit = st.selectbox('To:', list(conversion_factors[category].keys()))
value = st.number_input('Enter the value to convert', format='%f')

if st.button('Convert'):
    result = convert_units(category, value, from_unit, to_unit)
    st.success(f'{value} {from_unit} is {result} {to_unit}')
