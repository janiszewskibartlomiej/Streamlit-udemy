import pandas as pd
import plotly.express as px

df = pd.read_csv('data/iris.csv')

print(df.head())
print()

df1 = df.groupby('species').mean().reset_index()
print(df1)

plot = px.bar(data_frame=df1,
              x='species',
              y='petal_width',
              color='species',
              title='Bar Chart of Iris Dataset')
plot.show()