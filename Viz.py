import dash
import pandas as pd
import plotly.express as px

df = pd.read_excel('steam_data.xlsx')
df.sort_values('Dicount')
fig = px.bar(df,x= 'Title',y='Dicount',color='User Rating',hover_data=['Orignal Price','Discounted Price'])

fig.write_image("Images/discount_graph.png")
