import plotly.offline as pyo
import plotly.graph_objs as go
import numpy as np
from configs.config import colors

y = [1,14,14,15,16,18,18,19,19,20,20,23,24,26,27,27,28,29,33,54]
nos = np.random.randint(0,50,30)

plot1 = go.Box(y=y,
                boxpoints='all', 
                jitter=0.3, 
                pointpos=2.0, 
                name="Plot1"
            )

plot2 = go.Box(y=nos, 
                boxpoints='all', 
                jitter=0.4, 
                pointpos=2.0,
                name="Plot2"
            )

data = [plot1, plot2]

layout = go.Layout(title='two random samples', 
                    plot_bgcolor=colors['bg'],
                    paper_bgcolor=colors['bg'],
                    font = dict(color=colors['text'])
                )

figure = go.Figure(data,layout=layout)

if __name__ == "__main__":
    pyo.plot(figure, filename=r'figure\box.html')