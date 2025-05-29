import dash
from dash import html, dcc
from utils.ids import STATEMENT_OUT_IDS, DATA_EXPORT_ID
from utils.constants import TEMPLATE_OUT
from utils.styles import CELL_STYLING_FUNC_PROPENSITY, CELL_STYLING_EWS, DATA_EXPORT_BUTTON
import dash_ag_grid as dag
import numpy as np
import pandas as pd

out = [
    {
        "headerName": name, "field": col,
        "cellStyle": {"textAlign": "center"},
        "filter": True, "floatingFilter": True, "flex": 1
    }
    for name, col in zip(TEMPLATE_OUT.columns, TEMPLATE_OUT.iloc[0,])
]

defaultColDef = {
    "initialWidth": 200,
    "wrapHeaderText": True,
    "autoHeaderHeight": True,
}

statements_out_table = html.Div(
    id = STATEMENT_OUT_IDS["overall-container"],
    style = {"display":"none"},
    children = [
        html.H1("", style = {"text-align":"center"}),
        dag.AgGrid(
            id = STATEMENT_OUT_IDS["output-statements"],
            columnDefs = out,
            rowData = [],
            defaultColDef=defaultColDef,
            dashGridOptions = {
                "pagination": True,
                "paginationPageSize": 20,
                "rowSelection": "single"  # Single selection to add row by row
                },
            csvExportParams = {"fileName": "OA_Scored_Statements.csv"}
            ),
        html.Div([
            html.Button("Export as csv", id = DATA_EXPORT_ID["output-statements"], 
                        n_clicks = 0,
                        style = DATA_EXPORT_BUTTON)
            ],
                 style = {'display': 'flex', 'align-items': 'center', 'justify-content': 'center', 
                          'marginTop':'20px'}
        ),
        ]
)