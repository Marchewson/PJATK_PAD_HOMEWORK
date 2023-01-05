from dash import Dash, html, dcc, Input, Output
import pandas as pd
import plotly.express as px

df_wine = pd.read_csv('winequelity.csv')

def generate_table(df_wine, max_rows=10):
    return html.Table([
        html.Thead(
            html.Tr([html.Th(col) for col in df_wine.columns])
        ),
        html.Tbody([
            html.Tr([
                html.Th(df_wine.iloc[i][col]) for col in df_wine.columns
            ]) for i in range(min(len(df_wine), max_rows))
        ])
    ])

app = Dash(__name__)
app.layout = html.Div([
    html.H4(children='Tabela z danymi o winach:'),
    generate_table(df_wine),
    html.Br(),
    html.Label('Wybierz model:'),
    dcc.RadioItems(['Regresja', 'Klasyfikacja'], 'Regresja', id='radio-input'),
    html.Br(),
    html.Label('Wybierz argument x wizualizacji:'),
    dcc.Dropdown(id= 'dropdown-input', options = df_wine.columns, value = 'fixed acidity' ),
    dcc.Graph(id = 'graph')

], style = {'padding': 10})

@app.callback(
    Output(component_id='graph',component_property='figure'),
    Input(component_id = 'radio-input', component_property ='value'),
    Input(component_id = 'dropdown-input', component_property ='value')
)
def update_output_div(input_val1, input_val2):
    if input_val1 == 'Regresja':
        #zaleznosc ph od wybranej zmiennej
        return  px.scatter(df_wine, x=input_val2, y="pH")
    elif input_val1 == 'Klasyfikacja':
        #zaleznosc target od wybranej zmiennej
        return  px.scatter(df_wine, x=input_val2, y="target")


if __name__ == '__main__':
    app.run_server(debug=True)