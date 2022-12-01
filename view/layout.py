from dash import dcc, html
from plotly.subplots import make_subplots
import dash_bootstrap_components as dbc
import plotly.graph_objects as go

from view.components import TEXT, ROW_SECTION, BUTTON, DROPDOWN, MAIN_SECTION, MAIN_TITLE, CARD, BOLD_TEXT, LINK, COLUMN_SECTION, SPINNER, INTERVAL, STORE
from view.constants import COMPONENTS_IDS, STORE_STATE
from controller.orchestrator import start_app_iterations

APP_STORE = [
    STORE(STORE_STATE['done']),
    STORE(STORE_STATE['error']),
    STORE(STORE_STATE['loading']),
    STORE(STORE_STATE['success']),
]

DATABASE_CARD = CARD([
    BOLD_TEXT('database'),
    LINK('database_name', 'https://dados.pbh.gov.br/dataset/populacao-de-rua')
])

AUTHORS_CARD = CARD([BOLD_TEXT('authors'), TEXT('authors_name')])

INFO_CARDS = ROW_SECTION([DATABASE_CARD, AUTHORS_CARD],
                         id=COMPONENTS_IDS["info_cards"])

PAGE_HEADER = [
    MAIN_TITLE(),
    INFO_CARDS
]

START_APP_BUTTON = BUTTON(
    children=[SPINNER(id=COMPONENTS_IDS['start_app_button_spinner']),
              TEXT('start_app', id=COMPONENTS_IDS['start_app_button_text'])],
    id=COMPONENTS_IDS["start_app_button"]
)

STATUS_SECTION = ROW_SECTION(id=COMPONENTS_IDS['status_section'])

END_APP_BUTTON = BUTTON(
    children=TEXT('end_app', id=COMPONENTS_IDS["end_app_button_text"]),
    color="warning",
    id=COMPONENTS_IDS["end_app_button"]
)

DATABASE_BUTTON = BUTTON(
    children=TEXT('show_database'),
    color="success",
    id=COMPONENTS_IDS["database_button"]
)

CHARTS_BUTTON = BUTTON(
    children=TEXT('show_charts'),
    color="success",
    id=COMPONENTS_IDS["charts_button"]
)

BAR_CHART_BUTTON = BUTTON(
    children=TEXT('bar_chart'),
    id=COMPONENTS_IDS["bar_chart_button"]
)


PIE_CHART_BUTTON = BUTTON(
    children=TEXT('pie_chart'),
    id=COMPONENTS_IDS["pie_chart_button"]
)

HIDE_CHARTS_BUTTON = BUTTON(
    children=TEXT('hide_charts'),
    color="warning",
    id=COMPONENTS_IDS["hide_charts_button"]
)


CHARTS_BUTTONS = COLUMN_SECTION(
    [HIDE_CHARTS_BUTTON, ROW_SECTION([BAR_CHART_BUTTON, PIE_CHART_BUTTON])], id=COMPONENTS_IDS['charts_buttons'])


BAR_CHART_DROPDOWNS = ROW_SECTION([
    DROPDOWN(id=COMPONENTS_IDS["bar_chart_first_dimension_dropdown"]),
    DROPDOWN(id=COMPONENTS_IDS["bar_chart_second_dimension_dropdown"]),
    DROPDOWN(id=COMPONENTS_IDS["bar_chart_third_dimension_dropdown"]),
], id=COMPONENTS_IDS['bar_chart_dropdowns'])

PIE_CHART_DROPDOWNS = ROW_SECTION([
    DROPDOWN(id=COMPONENTS_IDS["pie_chart_first_dimension_dropdown"]),
    DROPDOWN(id=COMPONENTS_IDS["pie_chart_second_dimension_dropdown"]),
], id=COMPONENTS_IDS['pie_chart_dropdowns'])

CHARTS_DROPDOWNS = [BAR_CHART_DROPDOWNS, PIE_CHART_DROPDOWNS]


APP_BUTTONS = ROW_SECTION(
    children=[DATABASE_BUTTON, CHARTS_BUTTON, END_APP_BUTTON], id=COMPONENTS_IDS["app_buttons"])


CONTROL_SECTION = COLUMN_SECTION(
    [START_APP_BUTTON, STATUS_SECTION, APP_BUTTONS], id=COMPONENTS_IDS["control_section"])

CHART_SECTION = COLUMN_SECTION(
    [CHARTS_BUTTONS, *CHARTS_DROPDOWNS], id=COMPONENTS_IDS['charts_section'])


app_layout = MAIN_SECTION(
    [*APP_STORE, *PAGE_HEADER, CONTROL_SECTION, CHART_SECTION, INTERVAL(
        id=COMPONENTS_IDS["app_interval"], max_intervals=start_app_iterations)])


# CONTROLS_SECTION = [MAIN_BUTTON, INTERVAL, GRAPH_BUTTONS, GRAPH_DROPDOWNS]

# CONTROLS_SECTION = [START_BUTTON]


# BAR_GRAPH = dcc.Graph(
#     figure={
#         'data': [
#             {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
#             {'x': [1, 2, 3], 'y': [2, 4, 5],
#                 'type': 'bar', 'name': u'Montréal'},
#         ],
#         'layout': {
#             'title': 'Dash Data Visualization'
#         }
#     },
#     id="bar-graph",
#     className="hide"
# )


# labels = ["US", "China", "European Union", "Russian Federation", "Brazil", "India",
#           "Rest of World"]

# # Create subplots: use 'domain' type for Pie subplot
# fig = make_subplots(rows=1, cols=2, specs=[
#                     [{'type': 'domain'}, {'type': 'domain'}]])
# fig.add_trace(go.Pie(labels=labels, values=[16, 15, 12, 6, 5, 4, 42], name="GHG Emissions"),
#               1, 1)
# fig.add_trace(go.Pie(labels=labels, values=[27, 11, 25, 8, 1, 3, 25], name="CO2 Emissions"),
#               1, 2)

# # Use `hole` to create a donut-like pie chart
# fig.update_traces(hole=.4, hoverinfo="label+percent+name")

# fig.update_layout(
#     title_text="Global Emissions 1990-2011",
#     # Add annotations in the center of the donut pies.
#     annotations=[dict(text='GHG', x=0.18, y=0.5, font_size=20, showarrow=False),
#                  dict(text='CO2', x=0.82, y=0.5, font_size=20, showarrow=False)])


# PIE_GRAPH = dcc.Graph(figure=fig, id="pie-graph", className="hide")

# HEADER = [
#     MAIN_TITLE(),
#     ROW_SECTION([CARD([BOLD_TEXT('database'),
#                        LINK(
#         'database_name', 'https://dados.pbh.gov.br/dataset/populacao-de-rua')
#     ]), CARD([BOLD_TEXT('authors'), TEXT('authors_name')])])]


# # CONTROLS_SECTION = [MAIN_BUTTON, INTERVAL, GRAPH_BUTTONS, GRAPH_DROPDOWNS]


# GRAPH_SECTION = [BAR_GRAPH, PIE_GRAPH]

# # app_layout = MAIN_SECTION(
# #     [*HEADER, *CONTROLS_SECTION, *GRAPH_SECTION])
