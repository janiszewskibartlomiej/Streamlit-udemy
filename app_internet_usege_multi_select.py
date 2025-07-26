import pandas as pd
import streamlit as st
import plotly.express as ply

df = pd.read_csv('data/share-of-individuals-using-the-internet.csv')

st.set_page_config(layout='wide')
st.header('Internet Usage Dashboard')

print(df.columns)
print(df.info())

df = df[(df['Year'] >= 2000) & (df['Year'] <= 2016)]

years = list(df['Year'].unique())
years.sort()
continents = list(df['Country'].unique())

selected_year = st.selectbox(label='Year', index=0, options=years)
df_plot = df[df['Year'] == selected_year]
col1, col2 = st.columns([3, 1])

plot = ply.choropleth(data_frame=df_plot,
                      locations='Country',
                      locationmode='country names',
                      featureidkey='properties.name',
                      color='Individuals using the Internet (% of population)',
                      hover_name='Country',
                      color_continuous_scale=ply.colors.qualitative.Vivid,
                      title=f'Share of individuals using the internet in {selected_year}')

histogram1 = ply.histogram(data_frame=df_plot,
                           x='Individuals using the Internet (% of population)',
                           title=f'Distribution of internet usage in {selected_year}')

col1.plotly_chart(plot)
col2.plotly_chart(histogram1)

st.sidebar.subheader('Select a continent')

selected_continent = st.sidebar.multiselect(label='Continent', label_visibility='collapsed', options=continents)

if selected_continent:
    st.subheader(f'Country level analytics for  {selected_continent}')
    df_by_year_and_country = df[df['Country'].isin(selected_continent)]
    line_plot = ply.line(data_frame=df_by_year_and_country,
                         x='Year',
                         color='Country',
                         y='Individuals using the Internet (% of population)',
                         title=f'Internet Usage over time in {selected_continent}')
    st.plotly_chart(line_plot)
