import dash
from dash import html
from utils.styles import SELECTION_CONTAINER, EXPLORATORY_SELECTION_HALF, EXPLORATORY_SELECTION_HEADER, TARGETED_SELECTION_HALF, TARGETED_SELECTION_HEADER, TARGETED_SELECTION_QUARTER, CALCULATE_SELECTION_QUARTER
from utils.ids import SEARCH_SELECTION_IDS

## Define container

search_selection = html.Div(
    id = SEARCH_SELECTION_IDS["overall-container"],
    style = {'display':'none'},
    children = [
        html.Div(
            id = SEARCH_SELECTION_IDS["exploratory-block"],
            style = EXPLORATORY_SELECTION_HALF,
            children = html.H1("Exploratory Search", style = EXPLORATORY_SELECTION_HEADER)
        ),
        html.Div(
            id = SEARCH_SELECTION_IDS["targeted-block"],
            style = TARGETED_SELECTION_HALF,
            children = [
                html.Div(
                    id = SEARCH_SELECTION_IDS["target-sub-block"],
                    style = TARGETED_SELECTION_QUARTER,
                    children = html.H1("Targeted Search", style = TARGETED_SELECTION_HEADER)
                ),
                html.Div(
                    id = SEARCH_SELECTION_IDS["calculate-sub-block"],
                    style = CALCULATE_SELECTION_QUARTER,
                    children = html.H1("Score Statements", style = TARGETED_SELECTION_HEADER)
                ),
            ]
        )
    ]
)