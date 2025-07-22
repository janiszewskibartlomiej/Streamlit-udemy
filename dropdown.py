import streamlit as st

st.header('Dropdown')

cars = ('Ford', 'BMW', 'Mercedes-Benz', 'Audi', 'Volkswagen')

car_select = st.selectbox(
    label='Select your car manufacturer',
    options=cars,
    key='car_select',
    index=2,
    help='This is a dropdown',
    placeholder='Select your car manufacturer',
    # label_visibility='collapsed'

)
print(car_select)