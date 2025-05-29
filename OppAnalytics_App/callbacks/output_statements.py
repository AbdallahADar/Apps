import pandas as pd
import numpy as np
import dash
from dash import html, Input, Output, State
from utils.ids import STATEMENT_IDS, STATE_DATA_ID, STATEMENT_OUT_IDS
from utils.styles import TABLES_CONTAINER
from data.StateManager import StateManager

def register_callbacks(app):
    """
    Register callbacks related to the dashboard page.
    """
    @app.callback(
        [
            Output(STATEMENT_IDS['overall-container'], 'style', allow_duplicate=True),
            Output(STATEMENT_OUT_IDS['overall-container'], 'style', allow_duplicate=True),
            Output(STATEMENT_OUT_IDS["output-statements"], "rowData", allow_duplicate=True),
            Output(STATE_DATA_ID, 'data', allow_duplicate=True)
        ],
        [
            Input(STATEMENT_IDS['loading-trigger'], "data"),
            State(STATE_DATA_ID, 'data')
        ],
        prevent_initial_call = True
    )
    def update(loading_data, state):
        
        print("output-statement-display")

        SM = StateManager.from_dict(state) if state else StateManager()

        # Save output file name
        df = pd.read_csv(SM.statement_output_name)
                
        return [{'display':'none'}, TABLES_CONTAINER, df.to_dict("records"), SM.to_dict()]