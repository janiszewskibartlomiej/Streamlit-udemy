import streamlit as st


st.header('Forms')

form = st.form(key='my_form', clear_on_submit=False, enter_to_submit=True, border=True)

state_of_origin = form.selectbox(label='State of origin', options=['GD', 'GDY', 'GSP'])
submit_button = form.form_submit_button(label='Submit')

if submit_button:
    st.write(f'Submit button clicked: {submit_button}')
    st.write(f'State of origin: {state_of_origin}')


second_form = st.sidebar.form(key='second_form')
age = second_form.number_input(label='Age', min_value=18, max_value=100, value=25)
submit_button_sidebar = second_form.form_submit_button(label='Submit')

if submit_button_sidebar:
    st.markdown(f'**Age:** {age} submitted')