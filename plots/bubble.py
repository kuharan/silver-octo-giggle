import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd

df = pd.read_csv(r'data\mpg.csv')
print(df.head())

horsepower_mpg = [go.Scatter(x=df['horsepower'],
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

displacement_acceleration = [go.Scatter(x=df['displacement'],
                    y=df['acceleration'],
                    text=df['name'],
                    mode='markers',
                    marker=dict(
                        size=2*df['weight']/300,
                        opacity=0.5,
                        showscale=True
                    )                    
                )
        ]

layout1 = go.Layout(title='Bubble Chart',
                    hovermode='closest',
                    xaxis=dict(title='Horsepower'),
                    yaxis=dict(title='MPG')
                )

layout2 = go.Layout(title='Bubble Chart',
                    hovermode='closest',
                    xaxis=dict(title='displacement'),
                    yaxis=dict(title='acceleration')
                )

fig1 = go.Figure(data=horsepower_mpg, layout=layout1)
fig2 = go.Figure(data=displacement_acceleration, layout=layout2)
pyo.plot(fig1, filename=r'figure\bubble1.html')
pyo.plot(fig2, filename=r'figure\bubble2.html')