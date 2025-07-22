import pandas as pd
import plotly.express as px

df = pd.read_csv('data/iris.csv')

print(df.head())
print()

plot = px.histogram(data_frame=df,
                    x='sepal_length',
                    nbins=10,
                    barmode='overlay',
                    color='species',
                    title='Histogram of Iris Dataset')
plot.show()
