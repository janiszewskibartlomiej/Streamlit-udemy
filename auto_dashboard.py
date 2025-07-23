import pandas as pd
import streamlit as st
import plotly.express as ply

df = pd.read_csv('data/clean_auto_mpg.csv')

st.set_page_config(layout='wide')
st.title('Auto MPG Dashboard')

print(df.columns)
unique_origin = list(df['origin'].unique())
unique_origin.sort()
print(unique_origin)
unique_origin_str = [f'Origin: {origin}' for origin in unique_origin]

print(unique_origin_str)

tab1, tab2, tab3 = st.tabs(unique_origin_str)

with tab1:
    index = 0
    st.subheader(unique_origin_str[index])
    col1, col2, col3, col4 = st.columns([1, 1, 1, 1])
    df_tab = df[df['origin'] == unique_origin[index]]
    avg_mpg = round(df_tab['mpg'].mean(), 1)
    avg_disp = round(df_tab['displacement'].mean(), 1)
    avg_hp = round(df_tab['horsepower'].mean(), 1)
    avg_wt = round(df_tab['weight'].mean(), 1)
    col1.metric(label='Avg MPG', value=avg_mpg)
    col2.metric(label='Avg Displacement', value=avg_disp)
    col3.metric(label='Avg Horsepower', value=avg_hp)
    col4.metric(label='Avg Weight', value=avg_wt)

    col5, col6 = st.columns([4, 1])

    scatter = ply.scatter(data_frame=df_tab, x='weight', y='horsepower', size='displacement', hover_name='car name',
                          color='cylinders', title=f'Weight vs HP for cars from {unique_origin[index]}')
    col5.plotly_chart(scatter)

    hist = ply.histogram(data_frame=df_tab, x='mpg', title='MPG Distribution')
    col6.plotly_chart(hist)

with tab2:
    index = 1
    st.subheader(unique_origin_str[1])
    col1, col2, col3, col4 = st.columns([1, 1, 1, 1])
    df_tab = df[df['origin'] == unique_origin[index]]
    avg_mpg = round(df_tab['mpg'].mean(), 1)
    avg_disp = round(df_tab['displacement'].mean(), 1)
    avg_hp = round(df_tab['horsepower'].mean(), 1)
    avg_wt = round(df_tab['weight'].mean(), 1)
    col1.metric(label='Avg MPG', value=avg_mpg)
    col2.metric(label='Avg Displacement', value=avg_disp)
    col3.metric(label='Avg Horsepower', value=avg_hp)
    col4.metric(label='Avg Weight', value=avg_wt)

    col5, col6 = st.columns([4, 1])

    scatter = ply.scatter(data_frame=df_tab, x='weight', y='horsepower', size='displacement', hover_name='car name',
                          color='cylinders', title=f'Weight vs HP for cars from {unique_origin[index]}')
    col5.plotly_chart(scatter)

    hist = ply.histogram(data_frame=df_tab, x='mpg', title='MPG Distribution')
    col6.plotly_chart(hist)

with tab3:
    index = 2
    st.subheader(unique_origin_str[2])
    col1, col2, col3, col4 = st.columns([1, 1, 1, 1])
    df_tab = df[df['origin'] == unique_origin[index]]
    avg_mpg = round(df_tab['mpg'].mean(), 1)
    avg_disp = round(df_tab['displacement'].mean(), 1)
    avg_hp = round(df_tab['horsepower'].mean(), 1)
    avg_wt = round(df_tab['weight'].mean(), 1)
    col1.metric(label='Avg MPG', value=avg_mpg)
    col2.metric(label='Avg Displacement', value=avg_disp)
    col3.metric(label='Avg Horsepower', value=avg_hp)
    col4.metric(label='Avg Weight', value=avg_wt)

    col5, col6 = st.columns([4, 1])

    scatter = ply.scatter(data_frame=df_tab, x='weight', y='horsepower', size='displacement', hover_name='car name',
                          color='cylinders', title=f'Weight vs HP for cars from {unique_origin[index]}')
    col5.plotly_chart(scatter)

    hist = ply.histogram(data_frame=df_tab, x='mpg', title='MPG Distribution')
    col6.plotly_chart(hist)
