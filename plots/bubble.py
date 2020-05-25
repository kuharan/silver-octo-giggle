import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd

df = pd.read_csv(r'data\mpg.csv')
print(df.head())

data = [go.Scatter(x=df['horsepower'],
                    y=df['mpg'],
                    text=df['name'],
                    mode='markers',
                    marker=dict(
                        size=2*df['weight']/300,
                        color=df['cylinders'],
                        colorscale='mygbm', #https://plotly.com/python/builtin-colorscales/
                        opacity=0.5,
                        showscale=True
                    )                    
                )
        ]

layout = go.Layout(title='Bubble Chart',
                    hovermode='closest',
                    xaxis=dict(title='Horsepower'),
                    yaxis=dict(title='MPG')
                )
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename=r'figure\bubble.html')