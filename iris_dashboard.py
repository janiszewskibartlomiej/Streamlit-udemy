import pandas as pd
import streamlit as st
import plotly.express as ply

df = pd.read_csv('data/iris.csv')

st.set_page_config(layout='wide')
st.title('Iris Dashboard')

unique_species = df['species'].unique()
print(unique_species)
color_map = {'setosa': 'gray',
             'versicolor': 'gray',
             'virginica': 'gray'
             }

cola, colb = st.columns([1, 1])
selected_species = cola.selectbox(label='Species',
                                  label_visibility='collapsed',
                                  options=unique_species)
show_hist = colb.checkbox(label='Show histogram', key='show_hist')

df_plot = df[df['species'] == selected_species]

col1, col2, col3, col4 = st.columns([1, 1, 1, 1])

sl_mean = df_plot['sepal_length'].mean()
sw_mean = df_plot['sepal_width'].mean()
pl_mean = df_plot['petal_length'].mean()
pw_mean = df_plot['petal_width'].mean()

col1.metric(label='Sepal Length Average', value=sl_mean.round(2))
col2.metric(label='Sepal Width Average', value=sw_mean.round(2))
col3.metric(label='Petal Length Average', value=pl_mean.round(2))
col4.metric(label='Petal Width Average', value=pw_mean.round(2))

color_map[selected_species] = 'blue'

title = f'Sepal length vs Petal width for {selected_species}'
scatter_plot = ply.scatter(data_frame=df,
                           color_discrete_map=color_map,
                           x='sepal_length',
                           y='petal_length',
                           color='species',
                           size='petal_length',
                           title=title)
st.plotly_chart(scatter_plot)

if show_hist:
    col5, col6, col7, col8 = st.columns([1, 1, 1, 1])

    hist1 = ply.histogram(data_frame=df_plot, x='sepal_length', color_discrete_sequence=['blue'],
                          title='Distribution of Sepal Length')
    hist2 = ply.histogram(data_frame=df_plot, x='sepal_width', color_discrete_sequence=['blue'],
                          title='Distribution of Sepal With')
    hist3 = ply.histogram(data_frame=df_plot, x='petal_length', color_discrete_sequence=['blue'],
                          title='Distribution of Petal Length')
    hist4 = ply.histogram(data_frame=df_plot, x='petal_width', color_discrete_sequence=['blue'],
                          title='Distribution of Petal Width')

    col5.plotly_chart(hist1)
    col6.plotly_chart(hist2)
    col7.plotly_chart(hist3)
    col8.plotly_chart(hist4)
