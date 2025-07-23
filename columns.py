import streamlit as st

col1, col2, col3 = st.columns(3, gap='medium', vertical_alignment='top')

with col1:
    st.header('col 1')
    st.image('data/img.png')

with col2:
    st.header('col 2')
    st.image('data/img.png')

with col3:
    st.header('col 3')
    st.image('data/img.png')

col4, col5 = st.columns([1,4], gap='small', vertical_alignment='top')
col4.header('col 4')
col4.image('data/img.png')
col5.header('col 5')
col5.image('data/img.png')