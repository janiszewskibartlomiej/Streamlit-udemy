import streamlit as st

number_input = st.number_input(
    label='Enter a number',
    min_value=0,
    max_value=100,
    value=50,
    step=1,
    help='This is a number input',
    key='number_input',
    label_visibility='visible'
)

sider_number_input = st.sidebar.number_input(
    label='Enter a number',
    min_value=5,
    max_value=100,
    value=30,
    step=1,
    help='This is a number input form sidebar',
    key='sidebar_number_input',
    label_visibility='visible'
)
st.write(f'Selected number: {number_input}')
st.write(sider_number_input)