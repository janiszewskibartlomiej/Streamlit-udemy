import pandas as pd
import plotly.express as px

df = pd.read_csv('data/us-cities-top-1k.csv')

print(df.head())
print()

plot = px.scatter_map(data_frame=df,
                      lat='lat',
                      lon='lon',
                      size='Population',
                      hover_name='City',
                      zoom=4.5,
                      map_style='open-street-map',
                      title='Map of US Cities by Population')
plot.show()
