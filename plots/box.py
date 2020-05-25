import plotly.offline as pyo
import plotly.graph_objs as go
import numpy as np

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

pyo.plot(data, filename=r'figure\box.html')