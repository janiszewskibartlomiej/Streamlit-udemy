import pandas as pd
import streamlit as st
import plotly.express as ply

st.set_page_config(layout='wide')

st.markdown('# Gapminder Dashboard')

df = pd.read_csv('data/gapminder_data_graphs.csv')

unique_years = df['year'].unique()
# print(unique_years)
# print(type(unique_years))

selected_year = st.selectbox(label='Year', options=unique_years)

df_plot = df[df['year'] == selected_year]
# st.write(df_plot)

col1, col2, col3 = st.columns([1, 1, 1])

average_gdp = df_plot['gdp'].mean()
average_life_exp = df_plot['life_exp'].mean()
average_hdi = df_plot['hdi_index'].mean()

col1.metric(label='Average GDP', value=average_gdp.round(2))
col2.metric(label='Average Life Expectancy', value=average_life_exp.round(2))
col3.metric(label='Average HDI', value=average_hdi.round(2))

title = f'Plot of GDP vs Life expectancy for year {selected_year}'
scatter_plot = ply.scatter(data_frame=df_plot,
                           x='gdp',
                           y='life_exp',
                           color='continent',
                           title=title)
st.plotly_chart(scatter_plot)

col4, col5 = st.columns(2)

boxplot1 = ply.box(data_frame=df_plot, x='continent', y='gdp',
                   title='Distribution of GDP across the different cotinents')

histo_gdp = ply.histogram(data_frame=df_plot, x= 'gdp', title='Distribution of GDP across the different cotinents')

col4.plotly_chart(boxplot1)
col5.plotly_chart(histo_gdp)