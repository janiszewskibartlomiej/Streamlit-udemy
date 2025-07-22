import streamlit as st

st.header('Dropdown multiselect')

cars = ('Ford', 'BMW', 'Mercedes-Benz', 'Audi', 'Volkswagen', 'Porsche', 'Chrysler')

car_select = st.multiselect(
    label='Select favourites cars',
    options=cars,
    key='car_select',
    help='Select your favourite cars',
    max_selections=3,
    placeholder='Select your top 3 favourite cars',
    label_visibility='collapsed'

)
print(car_select)