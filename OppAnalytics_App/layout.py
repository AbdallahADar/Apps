from dash import html, dcc
from components import app_mode, search_selection, details_grid, geo_figure, sector_ndy_figure, company_table, statements_table, statements_out_table
from utils.ids import STATE_DATA_ID
from data.StateManager import StateManager

# Define the overall app layout
app_layout = html.Div([
    dcc.Store(id = STATE_DATA_ID), # StateManager
    app_mode,
    search_selection,
    details_grid,
    geo_figure,
    sector_ndy_figure,
    company_table,
    statements_table,
    statements_out_table,
])
