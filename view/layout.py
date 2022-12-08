from database.constants import PUC_DB_HOMELESS_COLUMNS_LABELS
from view.constants import (COMPONENTS_IDS, STORE_IDS)
from view.components import (BAR_CHART, BOLD_TEXT,
                             BUTTON, CARD,
                             COLUMN_SECTION, DATE_PICKER_RANGE,
                             DROPDOWN, INTERVAL, LINK,
                             MAIN_SECTION, MAIN_TITLE,
                             PIE_CHART, ROW_SECTION, SPINNER,
                             STORE, TEXT)
from controller.orchestrator import max_start_app_iterations, max_select_app_iterations

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


CHARTS_BUTTONS = ROW_SECTION(
    [BAR_CHART_BUTTON, PIE_CHART_BUTTON])

CHARTS_DROPDOWNS = ROW_SECTION([
    DROPDOWN(id=COMPONENTS_IDS["first_dimension_dropdown"],
             options=PUC_DB_HOMELESS_COLUMNS_LABELS),
    DROPDOWN(id=COMPONENTS_IDS["second_dimension_dropdown"],
             options=PUC_DB_HOMELESS_COLUMNS_LABELS),
], id=COMPONENTS_IDS['charts_dropdowns'], hide=True)


PERIOD_RANGE = DATE_PICKER_RANGE(id=COMPONENTS_IDS["date_picker_range"])

CHARTS_CONTROL_SECTION = COLUMN_SECTION(
    [CHARTS_BUTTONS, ROW_SECTION([CHARTS_DROPDOWNS, PERIOD_RANGE])])

CHARTS = COLUMN_SECTION(id="charts")

CHARTS_SECTION = COLUMN_SECTION(
    [CHARTS_CONTROL_SECTION, CHARTS], id=COMPONENTS_IDS['charts_section'], hide=True)

TABLE_SECTION = COLUMN_SECTION(id=COMPONENTS_IDS['table_section'], hide=True)

CHARTS_BUTTON = BUTTON(
    children=TEXT('component_show_charts_label'),
    color="success",
    id=COMPONENTS_IDS["show_charts_button"]
)

DATABASE_BUTTON = BUTTON(
    children=TEXT('component_show_database_text'),
    color="success",
    id=COMPONENTS_IDS["show_database_button"]
)

END_APP_BUTTON = BUTTON(
    children=TEXT('component_restart_app_label',
                  id=COMPONENTS_IDS["restart_app_button_text"]),
    color="warning",
    id=COMPONENTS_IDS["restart_app_button"]
)

CONTROL_BUTTONS = ROW_SECTION(
    children=[DATABASE_BUTTON, CHARTS_BUTTON, END_APP_BUTTON], id=COMPONENTS_IDS["control_buttons"], hide=True)

ALERTS_SECTION = COLUMN_SECTION(id=COMPONENTS_IDS["alerts_section"])

START_APP_BUTTON = BUTTON(
    children=[SPINNER(id=COMPONENTS_IDS['start_app_button_spinner']),
              TEXT('component_start_app_label', id=COMPONENTS_IDS['start_app_button_text'])],
    id=COMPONENTS_IDS["start_app_button"]
)

CONTROL_SECTION = COLUMN_SECTION(
    [START_APP_BUTTON, ALERTS_SECTION, CONTROL_BUTTONS], id=COMPONENTS_IDS["control_section"])

AUTHORS_CARD = CARD(
    [BOLD_TEXT('component_authors_label'), TEXT('component_authors_name')])

DATABASE_CARD = CARD([
    BOLD_TEXT('component_database_label'),
    LINK(key='component_database_name', href='component_database_link')
])

INFO_CARDS = ROW_SECTION([DATABASE_CARD, AUTHORS_CARD],
                         id=COMPONENTS_IDS["info_cards"])

HEADER_SECTION = COLUMN_SECTION([MAIN_TITLE(), INFO_CARDS, ])

APP_STORE = [
    STORE(STORE_IDS['error_message']),
    STORE(STORE_IDS['first_dimension']),
    STORE(STORE_IDS['loading_message']),
    STORE(STORE_IDS['second_dimension']),
    STORE(STORE_IDS['status']),
    STORE(STORE_IDS['success_message']),
    STORE(STORE_IDS['second_dimension_label']),
    STORE(STORE_IDS['first_dimension_label']),
    STORE(STORE_IDS['status_graph']),


]

BEHAVIOR_SECTION = [
    *APP_STORE, INTERVAL(id=COMPONENTS_IDS["start_app_interval"], max_intervals=max_start_app_iterations), INTERVAL(id=COMPONENTS_IDS["select_table_interval"], max_intervals=max_select_app_iterations), INTERVAL(id=COMPONENTS_IDS["select_chart_interval"], max_intervals=max_select_app_iterations)]


app_layout = MAIN_SECTION(
    [*BEHAVIOR_SECTION, HEADER_SECTION, CONTROL_SECTION, TABLE_SECTION, CHARTS_SECTION])
