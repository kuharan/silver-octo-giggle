import numpy as np
import plotly.offline as pyo
import plotly.graph_objs as go
from config.config import colors

np.random.seed(80)

x_values = np.linspace(0,1,100)
y_values = np.random.randn(100)

trace0 = go.Scatter(x=x_values, 
                    y=y_values+5,
                    mode='markers',
                    name='markers'
                    )

trace1 = go.Scatter(x=x_values, 
                    y=y_values,
                    mode='lines',
                    name='lines'
                    )

trace2 = go.Scatter(x=x_values, 
                    y=y_values-5,
                    mode='lines+markers',
                    name='lines and markers'
                    )

data = [trace0, trace1, trace2]

layout = go.Layout(title='Line Charts', plot_bgcolor=colors['bg'])

fig = go.Figure(data=data, layout=layout)

if __name__ == "__main__":
    pyo.plot(fig, filename=r'figure\line.html') 