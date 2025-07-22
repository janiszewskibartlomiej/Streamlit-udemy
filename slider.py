import datetime

import streamlit as st

st.header('Slider')

basic_slider = st.slider(
    label='Select a value',
    min_value=0,
    max_value=100,
    value=50,
    step=1,
    help='This is a slider',
    key='basic_slider',
)

st.write(f'Selected number: {basic_slider}')

range_slider = st.slider(
    label='Select a range',
    min_value=0,
    max_value=100,
    value=(50, 76),
    step=1,
    help='This is a slider',
    key='range_slider',
)

st.write(f'Selected range: {range_slider}')

float_slider = st.slider(label='Float slider', min_value=0.0, max_value=5.0, value=0.5, step=0.1, key='float_slider')

date_slider = st.slider(label='Date slider', min_value=datetime.date(2025,1,1), max_value=datetime.date(2025,7,22), value=datetime.date(2025,6,15), key='date_slider', format="MM/DD/YYYY")

st.write(f'Selected date: {date_slider}')