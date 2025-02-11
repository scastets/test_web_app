import dash
from dash import html

app = dash.Dash(__name__)

app.layout = html.Div("Hello, Render!")

server = app.server  # Obligatoire pour Render

if __name__ == "__main__":
    app.run_server(debug=True)
