import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd

import dash
import dash_core_components as dcc
import dash_html_components as html

df = pd.read_csv(r'data\mpg.csv')
print(df.head())

data = [go.Scatter(x=df['horsepower'],
                    y=df['mpg'],
                    text=df['name'],
                    mode='markers',
                    marker=dict(
                        size=2*df['weight']/200,
                        color=df['cylinders'],
                        colorscale='mygbm', #https://plotly.com/python/builtin-colorscales/
                        opacity=0.5,
                        showscale=True
                    )                    
                )
        ]

layout = go.Layout(title='Bubble Chart', hovermode='closest')
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename=r'figure\bubble.html')