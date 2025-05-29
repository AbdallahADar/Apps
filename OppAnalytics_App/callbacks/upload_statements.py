import pandas as pd
import numpy as np
import dash
from dash import html, Input, Output, State, dcc
from utils.ids import STATEMENT_IDS
from utils.constants import PATH
import base64
import io

def register_callbacks(app):
    """
    Register callbacks related to the dashboard page.
    """
    @app.callback(
        [
            Output(STATEMENT_IDS['input-statements'], 'data'),
        ],
        [
            Input(STATEMENT_IDS["upload"], "contents"),
        ],
        prevent_initial_call = True
    )
    def update(contents):
        
        print("template-upload")

        if contents is None:
            return [dash.no_update]

        content_type, content_string = contents.split(',')
        decoded = base64.b64decode(content_string)
        df = pd.read_csv(io.StringIO(decoded.decode('utf-8')))
        return [df.to_dict("records")]
