import pandas as pd
import plotly.express as px

df = pd.read_csv('data/tips.csv')

print(df.columns)
print(df.nunique())

plot = px.pie(data_frame=df,
              values='tip',
              names='sex',
              facet_col='smoker',
              hole=0.1,
              title='Pie chart of tips dataset'
              )
plot.show()