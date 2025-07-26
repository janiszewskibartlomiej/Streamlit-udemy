import streamlit as st

# Diagnostic print to verify Streamlit import
print(f"Streamlit type: {type(st)}")

st.header('Lesson on Pills')

city_list = ['Austin', 'Huston', 'London', 'New York', 'Paris', 'San Francisco', 'Tokyo', 'Washington']

city_selected = st.pills(label='Pick a city',
         options=city_list,
         selection_mode='single',
         default=city_list[0],
         key='pills_key',
         help='Pick your favorite city',
         disabled=False,
         label_visibility='visible')
st.markdown(f'You picked: {city_selected}')

city_multi_selected = st.pills(label='Select tom cities',
         options=city_list,
         selection_mode='multi',
         default=city_list,
         key='pills_multi_key',
         help='Pick your favorite cities',)
print(city_multi_selected)
st.markdown(f'You picked: {city_multi_selected}')