import pandas as pd
import plotly.express as px

df = pd.read_csv('data/iris.csv')

print(df.columns)

plot = px.scatter(data_frame=df,
                  size='sepal_width',
                  x='sepal_length',
                  y='petal_length',
                  # facet_col='species',
                  color='species',
                  title='Scatterplot of Iris Dataset')
plot.show()

if __name__ == '__main__':
    pass