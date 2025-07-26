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

df_plot_pie = df_plot.loc[:, ['PassengerId', 'Survived']].groupby('Survived').count().reset_index()
df_plot_pie.rename({'PassengerId': 'Count of passengers'}, axis='columns', inplace=True)
print(df_plot_pie)
pie_plot = ply.pie(data_frame=df_plot_pie, template='seaborn', values='Count of passengers', names='Survived', title='Count of passengers that survived')
col2.plotly_chart(pie_plot)

plot = ply.box(data_frame=df_plot, y='Fare', color='Survived', template='seaborn', title='Distribution of fare across survival status')
st.plotly_chart(plot)