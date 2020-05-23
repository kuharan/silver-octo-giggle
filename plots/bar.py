import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd

df = pd.read_csv(r'data\state_wise.csv')
df = df[df['State']!='Total'].head(15)
# print(df.head())

Confirmed = go.Bar(x=df['State'],
                    y=df['Confirmed'], 
                    name='Confirmed',
                    marker=dict(color="Red")
                    )

Recovered = go.Bar(x=df['State'], 
                    y=df['Recovered'], 
                    name='Recovered', 
                    marker=dict(color="Green")
                    )

Active = go.Bar(x=df['State'], 
                    y=df['Active'], 
                    name='Active', 
                    marker=dict(color="Blue")
                    )

data = [Confirmed, Active, Recovered]

layout = go.Layout(title='Covid-19 (as of 26-04-2020)', 
                    xaxis=dict(title='State'),
                    yaxis=dict(title='No. of cases')
                    )

fig = go.Figure(data=data, layout=layout)
pyo.plot(figure_or_data=fig, filename=r'figure\bar.html')