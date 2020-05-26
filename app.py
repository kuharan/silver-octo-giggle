import dash
import dash_core_components as dcc
import dash_html_components as html
from plots.bar import fig as bar_figure
from plots.box import figure as box_figure
from plots.bubble import fig1 as bubble1_figure, fig2 as bubble2_figure 
from plots.line import fig as line_figure
from plots.scatter import fig as scatter_figure

app = dash.Dash()

app.layout = html.Div(children=[
                html.H1('Hello Dash!'),
                html.Div('Dash: Web Dashboard with python!'), 
                dcc.Graph(id='bar_graph', figure=bar_figure),
                dcc.Graph(id='box_graph', figure=box_figure),
                dcc.Graph(id='bubble1_graph', figure=bubble1_figure),
                dcc.Graph(id='bubble2_graph', figure=bubble2_figure),
                dcc.Graph(id='line_graph', figure=line_figure),
                dcc.Graph(id='scatter_graph', figure=scatter_figure)
            ])

if __name__ == "__main__":
    app.run_server(debug=True)