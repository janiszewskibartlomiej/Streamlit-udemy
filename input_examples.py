import streamlit as st

# Diagnostic print to verify Streamlit import
print(f"Streamlit type: {type(st)}")

st.title('Input Example')

# Simplified text input
user_name = st.text_input(
    label='Enter your name',
    placeholder='Type here...',
    help='This is a text input',
    max_chars=100,
    type='default',
    key='user_name_input'
)

if user_name:
    st.write(f'Hello, {user_name}!')

my_password = st.text_input(label='Enter your password', type='password', max_chars=14, key='password_input')

text_area = st.text_area(label='Enter your text', height=150, key='text_area_key', help='This is a text area',
                         placeholder='Type here...', max_chars=1000)

if text_area:
    st.write(f'You wrote:\n{text_area}')

number_input = st.number_input(label='Enter a number', min_value=0, max_value=100, value=50, step=1,
                               help='This is a number input', key='number_input', label_visibility='visible')

sider_number_input = st.sidebar.number_input(label='Enter a number', min_value=5, max_value=100, value=30, step=1,)

st.write(sider_number_input)