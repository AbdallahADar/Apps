import pandas as pd
import numpy as np
import dash
from dash import html, Input, Output, State
from utils.ids import STATEMENT_IDS, STATE_DATA_ID
from utils.constants import TEMPLATE, STATEMENT_DATE, PATH
from datetime import datetime
import subprocess
from data.StateManager import StateManager

def register_callbacks(app):
    """
    Register callbacks related to the dashboard page.
    """
    @app.callback(
        [
            Output(STATEMENT_IDS['loading-out'], 'children', allow_duplicate=True),
            Output(STATEMENT_IDS['loading-trigger'], 'data', allow_duplicate=True),
            Output(STATE_DATA_ID, 'data', allow_duplicate=True)
        ],
        [
            Input(STATEMENT_IDS["calculate-button"], "n_clicks"),
            State(STATEMENT_IDS['input-statements'], "data"),
            State(STATE_DATA_ID, 'data')
        ],
        prevent_initial_call = True
    )
    def update(clicked, rows, state):
        
        print("statement-calculate")

        SM = StateManager.from_dict(state) if state else StateManager()

        # Convert to dataframe and convert date to datetime format
        out = pd.DataFrame(rows)
        out[STATEMENT_DATE] = pd.to_datetime(out[STATEMENT_DATE], format = "%Y-%m-%d")

        # Save data as csv file
        filename = f"{PATH}data/output_statement/statement_output_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
        out.to_csv(filename, index=False)

        # Save output file name
        SM.statement_output_name = filename.replace(".csv", "_processed.csv")

        # Run R Script to score the statements
        result = subprocess.run(
            ["Rscript", f"{PATH}engine/score_statements.R", filename],
            check=True,
            capture_output=True,
            text=True
        )
                
        return [f"", {"status": "done"}, SM.to_dict()]