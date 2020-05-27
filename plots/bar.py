import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd
from config.config import colors

df = pd.read_csv(r'data\state_wise.csv')
df = df[df['State']!='Total'].head(15)
# print(df.head())

# Column bar chart
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

# Horizontal bar chart
# swap x and y axis in each trace i.e (Confirmed, Active, Recovered) and add orientation='h'

data = [Confirmed, Active, Recovered]

# Group -> barmode='group' - default
# Stacked Bars -> barmode='stack'
layout = go.Layout(title='Covid-19 (as of 26-04-2020)', 
                    xaxis=dict(title='State'),
                    yaxis=dict(title='No. of cases'),
                    barmode='group',
                    plot_bgcolor=colors['bg']
                )

fig = go.Figure(data=data, layout=layout)

if __name__ == "__main__":
    pyo.plot(figure_or_data=fig, filename=r'figure\bar.html')