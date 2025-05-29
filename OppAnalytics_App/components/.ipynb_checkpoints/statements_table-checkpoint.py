import numpy as np
import pandas as pd
from utils.constants import PATH, DROPDOWN_COLS, DROPDOWN, TEMPLATE
from utils.styles import STATEMENT_TABLE_HEADER_STYLE, STATEMENT_TABLE_CELLS, STATEMENT_TABLE_ADD_ROW, STATEMENT_TABLE_CALCULATE, STATEMENT_TABLE_DOWNLOAD, STATEMENT_TABLE_UPLOAD
from utils.ids import STATEMENT_IDS
from dash import html, dcc, dash_table

## Define columns
columns = [
    {
        "name": name,
        "id": col,
        "editable": True,
        **({"presentation": "dropdown"} if col in DROPDOWN_COLS else {})
    }
    for name, col in zip(TEMPLATE.columns, TEMPLATE.iloc[0,])
]

## Define initial data
initial_data = [{i:"" for i in TEMPLATE.iloc[0,]} for _ in range(1)]

statements_table = html.Div(
    id = STATEMENT_IDS["overall-container"],
    style = {"display": "none"},
    children = [
        html.Div([
            html.Button("Add Row", id=STATEMENT_IDS["add-row-button"], 
                        n_clicks=0, style=STATEMENT_TABLE_ADD_ROW),
            html.Button("Download Template", id=STATEMENT_IDS["download-button"], 
                        n_clicks=0, style=STATEMENT_TABLE_DOWNLOAD),
            dcc.Download(id=STATEMENT_IDS["download"]),
            dcc.Upload(
                id=STATEMENT_IDS["upload"],
                children=html.Span(["Upload Statements"], style=STATEMENT_TABLE_UPLOAD),
                multiple=False,
                style={'display': 'inline-block'}
                ),
            html.Button("Calculate", id=STATEMENT_IDS["calculate-button"], 
                        n_clicks=0, style=STATEMENT_TABLE_CALCULATE)
        ], style={'marginTop': '20px','marginBottom': '20px', 'display': 'flex',
                  'gap': '20px', 'marginLeft':'20px', 'marginRight':'20px', 'textAlign': 'center',
                  'justifyContent': 'flex-start', 'alignItems': 'center'}),
        dash_table.DataTable(
            id = STATEMENT_IDS["input-statements"],
            columns = columns,
            data = initial_data,
            editable = True,
            dropdown = DROPDOWN,
            row_deletable = True,
            style_table={
                'height': '100%', 'width': '100%',
                # 'overflowX': 'auto',
                # 'overflowY': 'auto',
            },
            style_header = STATEMENT_TABLE_HEADER_STYLE,
            style_cell = STATEMENT_TABLE_CELLS,
            # style_as_list_view=True
        ),
        # Loading animation
        dcc.Loading(
            id=STATEMENT_IDS['loading-screen'],
            children=html.Div(id=STATEMENT_IDS['loading-out'], style={"height": "500px"}),
            # overlay_style={"visibility":"visible", "filter": "blur(2px)"},
            overlay_style={
                "backgroundColor": "rgba(255, 255, 255, 0.6)",  # semi-transparent white
                "backdropFilter": "blur(4px)",                  # blurs background *behind* overlay
                "WebkitBackdropFilter": "blur(4px)",            # for Safari support
                "zIndex": "9999",                               # keep above everything
            },
            fullscreen=True,
        ),
        # Store to trigger secondary callback
        dcc.Store(id=STATEMENT_IDS['loading-trigger']),
    ]
)