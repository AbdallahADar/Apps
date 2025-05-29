import pandas as pd
import numpy as np
import dash
from dash import html, Input, Output, State
from utils.ids import STATEMENT_IDS
from utils.constants import TEMPLATE

def register_callbacks(app):
    """
    Register callbacks related to the dashboard page.
    """
    @app.callback(
        [
            Output(STATEMENT_IDS['input-statements'], 'data', allow_duplicate=True),
        ],
        [
            Input(STATEMENT_IDS['add-row-button'], "n_clicks"),
            State(STATEMENT_IDS['input-statements'], "data")
        ],
        prevent_initial_call = True
    )
    def update(clicked, rows):
        
        print("statement-add-row")

        rows.append({i:"" for i in TEMPLATE.iloc[0,]})
                
        return [rows]