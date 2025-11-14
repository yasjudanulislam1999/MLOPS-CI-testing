import streamlit as st

# Streamlit UI

st.title('Power calculator')
st.write('"Enter the number you want to find the power of?')
n = st.number_input('Enter an integer',value=1,step=1)

# calculate_results
square = n*n
cube = n**3
fifth_power = n**5 
#Display results

st.write(f'The square of {n} is: {square}')
st.write(f'The cube of n is {n} is: {cube}')
st.write(f'The 5th power of {n} is: {fifth_power}')
