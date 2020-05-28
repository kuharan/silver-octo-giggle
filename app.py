import dash
import dash_core_components as dcc
import dash_html_components as html
from plots.bar import fig as bar_figure
from plots.box import figure as box_figure
from plots.bubble import fig1 as bubble1_figure, fig2 as bubble2_figure 
from plots.line import fig as line_figure
from plots.scatter import fig as scatter_figure
from configs.config import colors
from dash.dependencies import Input, Output

app = dash.Dash(__name__)

app.layout = html.Div([
                    html.Div(
                        children=[
                            html.H1('Dashboard!', style=dict(color=colors['text'], textAlign='center'))]
                    ),
                    html.Div(
                        children=[
                            dcc.Dropdown(
                                id='select-graph',
                                options=[
                                    dict(label='Scatter Graph', value='scatter_figure'),
                                    dict(label='Line Graph', value='line_figure'),
                                    dict(label='Bubble1 Graph', value='bubble1_figure'),
                                    dict(label='Bubble2 Graph', value='bubble2_figure'),
                                    dict(label='Bar Graph', value='bar_figure'),
                                    dict(label='Box Graph', value='box_figure')
                                ],
                                placeholder="Select a Graph",
                                style=dict(textAlign='center')
                            )                                        
                        ]
                    ),
                    html.Div(
                        id='display-graph'
                    )
                ],
                style = dict(backgroundColor=colors['bg'])
            )

@app.callback(Output(component_id='display-graph',component_property='children'),[Input(component_id='select-graph',component_property='value')])
def show_graph(graph_name):
    if graph_name=="scatter_figure":
        return dcc.Graph(id='scatter_graph', figure=scatter_figure)
    if graph_name=="line_figure":    
        return dcc.Graph(id='line_graph', figure=line_figure)
    if graph_name=="bubble1_figure":
        return dcc.Graph(id='bubble1_graph', figure=bubble1_figure),
    if graph_name=="bubble2_figure":
        return dcc.Graph(id='bubble2_graph', figure=bubble2_figure),
    if graph_name=="bar_figure":
        return dcc.Graph(id='bar_graph', figure=bar_figure),
    if graph_name=="box_figure":
        return dcc.Graph(id='box_graph', figure=box_figure)

if __name__ == "__main__":
    app.run_server(debug=True, port=8050)