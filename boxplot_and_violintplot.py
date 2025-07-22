import pandas as pd
import plotly.express as px

df = pd.read_csv('data/iris.csv')

print(df.columns)
print()

plot = px.box(data_frame=df,
              x='species',
              y='petal_width',
              color='species',
              title='Boxplot of Iris Dataset')
plot.show()

plot1 = px.violin(data_frame=df,
                  x='species',
                  y='petal_width',
                  color='species',
                  box=True,
                  title='Violinplot of Iris Dataset')

plot1.show()
