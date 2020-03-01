# this dashboard is here simply to display graph results of code in following folders

import dash
import dash_core_components as dcc
import dash_html_components as html
from plotly.tools import mpl_to_plotly

app = dash.Dash()

app.layout = html.Div(children=[
    html.H1(children='Machine data graphs'),

    dcc.Graph(
        id='example',
        figure={
            'data': [
                {'x': [1, 2, 3, 4, 5], 'y': [9, 6, 2, 1, 5], 'type': 'line', 'name': 'Boats'},
                {'x': [1, 2, 3, 4, 5], 'y': [8, 7, 2, 7, 3], 'type': 'bar', 'name': 'Cars'},
            ],
            'layout': {
                'title': 'Basic Dash Example'
            }
        }
    ),

    # html.Img(src='/assets/IMG_9137.png')
    html.Img(src='/assets/IMG_9137.png', style={'height': '40%', 'width': '50%'})

])

if __name__ == '__main__':
    app.run_server(debug=True)
