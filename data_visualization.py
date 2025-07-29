import pandas as pd
import streamlit as st
import plotly.express as ply

st.set_page_config(layout='wide')
st.title('Data Visualization Applications')

st.sidebar.subheader('Visualization Settings')
file_upload = st.sidebar.file_uploader(label='Upload your CSV or Excel file hire',
                                       type=['csv', 'xlsx'])

display_dataset = st.sidebar.checkbox(label='Would you like to view the uploaded dataset ?',)

global df
global numeric_columns
global no_numeric_columnS

if file_upload:
    try:
        df = pd.read_csv(file_upload)
        file_upload.seek(0)

        if display_dataset:
            st.write(df)
        # print(df.shape)
    except Exception as e:
        print(e)
        df = pd.read_excel(file_upload)

    numeric_columns = list(df.select_dtypes(['float','int']).columns)

    non_numeric_columns = list(df.select_dtypes('object').columns)
    non_numeric_columns.append('None')
    st.write(numeric_columns)
    st.write(non_numeric_columns)

chart_select = st.sidebar.selectbox(label='Select the visualization type.',
                                    options=['Scatterplots', 'Lineplots', 'Histogram'])
if chart_select == 'Scatterplots':
    st.sidebar.subheader('Settings for Scratterplots')
    x_value = st.sidebar.selectbox(label='X axis', options=numeric_columns)
    y_value = st.sidebar.selectbox(label='Y axis', options=numeric_columns)
    specify_color = st.sidebar.checkbox(label='Would you like to specify the color?')
    if specify_color:
        color_value = st.sidebar.selectbox(label='Color', options=non_numeric_columns)
        plot = ply.scatter(data_frame=df, x=x_value, y=y_value, color=color_value)
    else:
        plot = ply.scatter(data_frame=df, x=x_value, y=y_value)
    st.plotly_chart(plot)

if chart_select == 'Histogram':
    st.sidebar.subheader('Settings for Histogram')
    x = st.sidebar.selectbox(label='Feature', options=numeric_columns)
    bin_size = st.sidebar.slider(label='Number of bins', min_value=10, max_value=100,
                                 value=50)
    plot = ply.histogram(data_frame=df, x=x, nbins=bin_size)
    st.plotly_chart(plot)

if chart_select == 'Lineplots':
    st.sidebar.subheader('Settings for Lineplots')
    x_value = st.sidebar.selectbox(label='X axis', options=numeric_columns)
    y_value = st.sidebar.selectbox(label='Y axis', options=numeric_columns)
    plot = ply.line(data_frame=df, x=x_value, y=y_value)
    st.plotly_chart(plot)