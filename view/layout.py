from database.constants import PUC_DB_HOMELESS_COLUMNS_LABELS
from view.constants import (COMPONENTS_IDS, STORE_IDS)
from view.components import (BOLD_TEXT,
                             BUTTON, CARD,
                             COLUMN_SECTION, DATE_PICKER_RANGE,
                             DROPDOWN, INTERVAL, LINK,
                             MAIN_SECTION, MAIN_TITLE,
                             ROW_SECTION, SPINNER,
                             STORE, TEXT)
from controller.orchestrator import max_start_app_iterations, max_select_table_iterations


APP_STORE = [
    STORE(STORE_IDS['error_message']),
    STORE(STORE_IDS['first_column_label']),
    STORE(STORE_IDS['first_column']),
    STORE(STORE_IDS['loading_message']),
    STORE(STORE_IDS['second_column_label']),
    STORE(STORE_IDS['second_column']),
    STORE(STORE_IDS['status']),
    STORE(STORE_IDS['success_message']),
]

START_APP_INTERVAL = INTERVAL(
    id=COMPONENTS_IDS["start_app_interval"], max_intervals=max_start_app_iterations)

SELECT_TABLE_INTERVAL = INTERVAL(
    id=COMPONENTS_IDS["select_table_interval"], max_intervals=max_select_table_iterations, interval=1000)

SELECT_CHART_INTERVAL = INTERVAL(
    id=COMPONENTS_IDS["select_chart_interval"], max_intervals=-1, interval=1000)

BEHAVIOR_SECTION = [
    *APP_STORE, START_APP_INTERVAL, SELECT_TABLE_INTERVAL, SELECT_CHART_INTERVAL]


AUTHORS_CARD = CARD(
    [BOLD_TEXT('component_authors_label'), TEXT('component_authors_name')])

DATABASE_CARD = CARD([
    BOLD_TEXT('component_database_label'),
    LINK(key='component_database_name', href='component_database_link')
])

INFO_CARDS = ROW_SECTION([DATABASE_CARD, AUTHORS_CARD],
                         id=COMPONENTS_IDS["info_cards"])

HEADER_SECTION = COLUMN_SECTION([MAIN_TITLE(), INFO_CARDS])


ALERTS_SECTION = COLUMN_SECTION(id=COMPONENTS_IDS["alerts_section"])

CHARTS_BUTTON = BUTTON(
    children=TEXT('component_show_charts_label'),
    color="success",
    id=COMPONENTS_IDS["show_charts_button"]
)

TABLE_BUTTON = BUTTON(
    children=TEXT('component_show_table_text'),
    color="success",
    id=COMPONENTS_IDS["show_table_button"]
)

CONTROL_BUTTONS = ROW_SECTION(
    children=[TABLE_BUTTON, CHARTS_BUTTON], id=COMPONENTS_IDS["control_buttons"], hide=True)

START_APP_BUTTON = BUTTON(
    children=[SPINNER(id=COMPONENTS_IDS['start_app_button_spinner']),
              TEXT('component_start_app_label', id=COMPONENTS_IDS['start_app_button_text'])],
    id=COMPONENTS_IDS["start_app_button"]
)

CONTROL_SECTION = COLUMN_SECTION(
    [START_APP_BUTTON, ALERTS_SECTION, CONTROL_BUTTONS], id=COMPONENTS_IDS["control_section"])


TABLE_SECTION = COLUMN_SECTION(id=COMPONENTS_IDS['table_section'], hide=True)


BAR_CHART_BUTTON = BUTTON(
    children=TEXT('component_bar_chart_text'),
    color="success",
    id=COMPONENTS_IDS["bar_chart_button"]
)

PIE_CHART_BUTTON = BUTTON(
    children=TEXT('component_pie_chart_text'),
    color="success",
    id=COMPONENTS_IDS["pie_chart_button"]
)

CREATE_GRAPH_BUTTON = BUTTON(
    children=TEXT('component_create_graph'),
    color="success",
    id=COMPONENTS_IDS["create_graph_button"]
)

CHARTS_BUTTONS = ROW_SECTION(
    [BAR_CHART_BUTTON, PIE_CHART_BUTTON])

CHARTS_DROPDOWNS = ROW_SECTION([
    DROPDOWN(id=COMPONENTS_IDS["first_column_dropdown"],
             options=PUC_DB_HOMELESS_COLUMNS_LABELS),
    DROPDOWN(id=COMPONENTS_IDS["second_column_dropdown"],
             options=PUC_DB_HOMELESS_COLUMNS_LABELS),
], id=COMPONENTS_IDS['charts_dropdowns'])


PERIOD_RANGE = DATE_PICKER_RANGE(id=COMPONENTS_IDS["date_picker_range"])

CHARTS_CONTROL_SECTION = COLUMN_SECTION(
    [CHARTS_BUTTONS, ROW_SECTION([CHARTS_DROPDOWNS, PERIOD_RANGE, CREATE_GRAPH_BUTTON], id=COMPONENTS_IDS["charts_control_section"], hide=True)])

BAR_CHART = COLUMN_SECTION(id=COMPONENTS_IDS["bar_chart"])

PIE_CHART = COLUMN_SECTION(id=COMPONENTS_IDS["pie_chart"])

CHARTS = COLUMN_SECTION([BAR_CHART, PIE_CHART],
                        id=COMPONENTS_IDS["charts"])

CHARTS_SECTION = COLUMN_SECTION(
    [CHARTS_CONTROL_SECTION, CHARTS], id=COMPONENTS_IDS['charts_section'], hide=True)


app_layout = MAIN_SECTION(
    [*BEHAVIOR_SECTION, HEADER_SECTION, CONTROL_SECTION, TABLE_SECTION, CHARTS_SECTION])
