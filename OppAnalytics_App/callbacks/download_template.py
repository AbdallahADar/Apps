import pandas as pd
import numpy as np
import dash
from dash import html, Input, Output, State, dcc
from utils.ids import STATEMENT_IDS
from utils.constants import PATH

def register_callbacks(app):
    """
    Register callbacks related to the dashboard page.
    """
    @app.callback(
        [
            Output(STATEMENT_IDS['download'], 'data'),
        ],
        [
            Input(STATEMENT_IDS["download-button"], "n_clicks"),
        ],
        prevent_initial_call = True
    )
    def update(clicked):
        
        print("template-download")

        TEMPLATE_DF = pd.read_csv(f"{PATH}data/statement_template/template_download.csv")

        return [dcc.send_data_frame(TEMPLATE_DF.to_csv, "Opp_Analytics_template.csv", index=False)]