from dash import Dash
from layout import app_layout  # Import the centralized layout
from callbacks import register_all_callbacks  # Register all callbacks
from utils.styles import index_string
import dash_bootstrap_components as dbc

# Initialize the Dash app
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
# app = Dash(__name__)

# Customize app index string
app.index_string = index_string

# Set app layout
app.layout = app_layout

# Register all callbacks
register_all_callbacks(app)

# Run the app
if __name__ == "__main__":
    app.run_server(debug=True)
    # app.run_server(debug=True, port = 8049, host='0.0.0.0')
