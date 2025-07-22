import pandas as pd
import plotly.express as px

df = pd.read_csv('data/iris.csv')

print(df.columns)

# - `plotly` (default light theme)
# - `plotly_white` (clean white background)
# - `presentation` (optimized for presentations)
# - `ggplot2` (mimics the ggplot2 style in R)
# - `seaborn` (resembles visualizations from Seaborn)
# - `simple_white` (a minimal white theme)
# - `plotly_dark` (dark background and vibrant colors)

plot = px.scatter(data_frame=df,
                  size='sepal_width',
                  x='sepal_length',
                  y='petal_length',
                  # facet_col='species',
                  template='plotly_dark',
                  color='species',
                  title='Scatterplot of Iris Dataset')
plot.show()

plot.show()
