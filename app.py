import pandas as pd
import streamlit as st
import plotly.express as ply

df = pd.read_csv('data/titani_data.csv')

st.set_page_config(layout='wide')
st.title('Titanic Dashboard')

print(df.columns)
print(df.info())

df['Embarked'] = df['Embarked'].fillna('Unknown')

embarked_port = list(df['Embarked'].unique())
gender = list(df['Sex'].unique())

col1, col2 = st.columns([1, 1])
selected_port = col1.selectbox(options=embarked_port, label='Select a port')
selected_gender = col2.selectbox(options=gender, label='Select a gender')

df_plot = df[df['Embarked'] == selected_port]
df_plot = df_plot[df_plot['Sex'] == selected_gender]

plot = ply.histogram(data_frame=df_plot,
                     template='seaborn',
                     color='Survived',
                     title='Distribution of Age',
                     facet_col='Survived',
                     x='Age')
col1.plotly_chart(plot)