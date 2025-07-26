import pandas as pd
import streamlit as st
import plotly.express as ply

st.cache_data()


def load_data():
    df = pd.read_csv('data/all_stocks_5yr.csv', index_col='date')

    numeric_df = df.select_dtypes(include=[int, float])
    numeric_cols = numeric_df.columns

    text_df = df.select_dtypes(include=[object])
    text_cols = text_df.columns

    stock_column = df['Name']

    unique_stocks = stock_column.unique()

    return df, numeric_cols, text_cols, unique_stocks


df, numeric_cols, text_cols, unique_stocks = load_data()

st.set_page_config(layout='wide')
st.title('Stock Dashboard')

check_box = st.sidebar.checkbox('Display the dataset')

if check_box:
    st.write(df)

st.sidebar.title('Settings')
st.sidebar.subheader('Timeseries settings')

selected_stocks = st.sidebar.multiselect(label='Select stocks',
                                         options=numeric_cols)

stock_ticker = st.sidebar.selectbox(label='Stock Ticker',
                                    options=unique_stocks)

stock_df = df[df['Name'] == stock_ticker]

try:
    plot = ply.line(data_frame=stock_df, x=stock_df.index, y=selected_stocks, title=f'Timeseries of {stock_ticker} prices.')
    st.plotly_chart(plot)
except:
    print('No data to plot')
