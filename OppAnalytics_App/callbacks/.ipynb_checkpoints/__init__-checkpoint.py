from .app_selection import register_callbacks as app_selection
from .search_selection import register_callbacks as search_selection
from .sector_dropdown import register_callbacks as sector_dropdown
from .risk_type_dropdown import register_callbacks as risk_type_dropdown
from .geo_selection import register_callbacks as geo_selection
from .sector_ndy_selection import register_callbacks as sector_ndy_selection
from .row_selection import register_callbacks as row_selection
from .export_data import register_callbacks as export_data
from .details_grid import register_callbacks as details_grid
from .add_statement_row import register_callbacks as add_statement_row
from .calculate_statements import register_callbacks as calculate_statements
from .output_statements import register_callbacks as output_statements
from .download_template import register_callbacks as download_template
from .upload_statements import register_callbacks as upload_statements

def register_all_callbacks(app):
    """
    Register all callbacks with the app.
    """
    app_selection(app)
    details_grid(app)
    search_selection(app)
    geo_selection(app)
    sector_dropdown(app)
    risk_type_dropdown(app)
    sector_ndy_selection(app)
    row_selection(app)
    export_data(app)
    add_statement_row(app)
    calculate_statements(app)
    output_statements(app)
    download_template(app)
    upload_statements(app)