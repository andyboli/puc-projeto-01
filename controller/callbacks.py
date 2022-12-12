from dash import ctx

from controller.orchestrator import max_start_app_iterations, start_app, select_data, max_select_table_iterations, select_table_iterator
from dash import (dash_table, dcc, html)
from controller.reader import lang
from controller.mapper import map_date, map_bar_chart_data
from view.constants import STATUS_TYPES
from view.components import ALERT, SUCCESS_ICON, ERROR_ICON, TABLE, BAR_CHART, PIE_CHART, SPINNER
from database.constants import (PUC_DB_HOMELESS_COLUMNS_LABELS,
                                AGE_COLUMN,
                                PUC_DB_HOMELESS_COLUMNS_RANGES,
                                ETHNICITY_COLUMN,
                                GENDER_COLUMN,

                                PERIOD_COLUMN,
                                REGION_COLUMN,
                                SCHOOLING_COLUMN,
                                SOCIAL_WELFARE_COLUMN
                                )

hide_component = {'display': 'none'}
show_component = {'display': 'flex'}


def disabled_create_graph_button(first_column, second_column, start_date, end_date):
    hasColumns = first_column and first_column != 'empty' and second_column and second_column != 'empty'
    sameColumns = first_column == second_column
    halfPeriod = start_date and not end_date or not start_date and end_date
    return not hasColumns or sameColumns or halfPeriod


def disabled_start_app_button(status: str):
    return status == STATUS_TYPES['finished']


def disabled_start_app_interval(status: str):
    return status == STATUS_TYPES['uninitialized'] or status == STATUS_TYPES['finished']


def display_control_buttons(status: str):
    if status == STATUS_TYPES['finished']:
        return show_component
    else:
        return hide_component


def display_section(show_button_n_clicks_timestamp, hide_button_n_clicks_timestamp):
    if show_button_n_clicks_timestamp is None and hide_button_n_clicks_timestamp is None:
        return hide_component
    elif show_button_n_clicks_timestamp is not None and hide_button_n_clicks_timestamp is None:
        return show_component
    elif show_button_n_clicks_timestamp is None and hide_button_n_clicks_timestamp is not None:
        return hide_component
    elif show_button_n_clicks_timestamp > hide_button_n_clicks_timestamp:
        return show_component
    elif show_button_n_clicks_timestamp < hide_button_n_clicks_timestamp:
        return hide_component
    return hide_component


def display_start_app_button_spinner(status: str):
    if status == STATUS_TYPES['initialized']:
        return show_component
    else:
        return hide_component


def get_bar_chart(first_column, second_column, max_month, max_year, min_year, min_month):
    first_column_range = PUC_DB_HOMELESS_COLUMNS_RANGES[first_column]
    data = []
    error = ''
    for first_column_value in first_column_range:
        value_data_raw, error = select_data(first_column=first_column, second_column=second_column, first_column_value=first_column_value,
                                            max_month=max_month, max_year=max_year, min_year=min_year, min_month=min_month)
        if error:
            error = error
            break
        amouts = []
        second_column_values = []
        for amout, second_column_value in value_data_raw:
            amouts.append(amout)
            second_column_values.append(second_column_value)
        data.append({'type': 'bar', 'name': first_column_value,
                     'x': second_column_values, 'y': amouts})
    if (data and len(data)):
        return [BAR_CHART(figure={"data": data})]
    if (error):
        return ALERT(
            [SPINNER(size='md', color='dark'), error], color='light')
    return []


def get_pie_chart(first_column, second_column, max_month, max_year, min_year, min_month):
    error = ''
    first_column_range = PUC_DB_HOMELESS_COLUMNS_RANGES[first_column]
    second_column_values = {}
    for first_column_value in first_column_range:
        value_data_raw, error = select_data(first_column=first_column, second_column=second_column, first_column_value=first_column_value,
                                            max_month=max_month, max_year=max_year, min_year=min_year, min_month=min_month)
        if error:
            error = error
            break
        for amout, second_column_value in value_data_raw:
            try:
                second_column_values[second_column_value].append(
                    amout)
            except:
                second_column_values[second_column_value] = [amout]
    if (error):
        return ALERT(
            [SPINNER(size='md', color='dark'), error], color='light')

    return [PIE_CHART(first_column_values=first_column_range, second_column_values=second_column_values)]


def update_alert_section(success_message: str, error_message: str, alerts_section: any):
    if success_message and not alerts_section:
        return [ALERT([SUCCESS_ICON(), success_message])]
    elif success_message and alerts_section:
        return [*alerts_section, ALERT([SUCCESS_ICON(), success_message])]
    elif error_message and not alerts_section:
        return [ALERT([ERROR_ICON(), error_message], color='danger')]
    elif error_message and alerts_section:
        return [*alerts_section, ALERT([ERROR_ICON(), error_message], color='danger')]
    return alerts_section


def update_chart(create_graph_button_n_clicks, first_column, second_column, start_date, end_date, chart_callback):
    min_year = ''
    min_month = ''
    max_year = ''
    max_month = ''
    hasColumns = first_column and first_column != 'empty' and second_column and second_column != 'empty'
    sameColumns = first_column == second_column
    halfPeriod = start_date and not end_date or not start_date and end_date
    hasPeriod = start_date and end_date
    if hasPeriod:
        min_year, min_month = map_date(start_date)
        max_year, max_month = map_date(end_date)
    if hasColumns and not halfPeriod and not sameColumns and create_graph_button_n_clicks:
        return chart_callback(
            first_column=first_column, second_column=second_column, max_month=max_month, max_year=max_year, min_year=min_year, min_month=min_month)
    return []


def update_column_dropdown_label(column_label, other_column_label, selected_other_column):
    sameLabel = column_label == other_column_label
    is_selected = column_label != lang("component_dropdown_label")
    if sameLabel and is_selected and selected_other_column:
        return lang("component_dropdown_label")
    return column_label


def update_selected_column(age_timestamp, gender_timestamp, schooling_timestamp, ethnicity_timestamp, region_timestamp, social_welfare_timestamp, period_timestamp):
    selected_field = list(filter(lambda column: column is not None, [age_timestamp, gender_timestamp, schooling_timestamp, ethnicity_timestamp,
                                                                     region_timestamp, social_welfare_timestamp, period_timestamp]))

    selected_field_timestamp = 0

    if len(selected_field):
        selected_field_timestamp = max(selected_field)

    if selected_field_timestamp == age_timestamp:
        return AGE_COLUMN, PUC_DB_HOMELESS_COLUMNS_LABELS[AGE_COLUMN]
    if selected_field_timestamp == gender_timestamp:
        return GENDER_COLUMN, PUC_DB_HOMELESS_COLUMNS_LABELS[GENDER_COLUMN],
    if selected_field_timestamp == schooling_timestamp:
        return SCHOOLING_COLUMN, PUC_DB_HOMELESS_COLUMNS_LABELS[SCHOOLING_COLUMN],
    if selected_field_timestamp == ethnicity_timestamp:
        return ETHNICITY_COLUMN, PUC_DB_HOMELESS_COLUMNS_LABELS[ETHNICITY_COLUMN],
    if selected_field_timestamp == region_timestamp:
        return REGION_COLUMN, PUC_DB_HOMELESS_COLUMNS_LABELS[REGION_COLUMN],
    if selected_field_timestamp == social_welfare_timestamp:
        return SOCIAL_WELFARE_COLUMN, PUC_DB_HOMELESS_COLUMNS_LABELS[SOCIAL_WELFARE_COLUMN]
    if selected_field_timestamp == period_timestamp:
        return PERIOD_COLUMN, PUC_DB_HOMELESS_COLUMNS_LABELS[PERIOD_COLUMN]

    return "empty", lang("component_dropdown_label")


def update_start_app_button_text(status: str, loading_message: str):
    if status == STATUS_TYPES['initialized']:
        return loading_message
    return lang("component_start_app_label")


def update_store_with_start_button(start_app_button_clicked: bool):
    if start_app_button_clicked:
        return STATUS_TYPES['initialized']
    else:
        return STATUS_TYPES['uninitialized']


def update_store_with_start_app_interval(n_intervals: int):
    status = STATUS_TYPES['initialized']
    success = ''
    loading = ''
    error = ''
    try:
        success, loading, error = next(start_app)
        if n_intervals == max_start_app_iterations:
            status = STATUS_TYPES['finished']
    except StopIteration:
        status = STATUS_TYPES['finished']
    finally:
        return status, success, loading,  error


def update_store(start_app_interval_n_intervals: int, start_app_button_clicked: bool):
    status = STATUS_TYPES['uninitialized']
    success = ''
    loading = ''
    error = ''
    if start_app_interval_n_intervals:
        status, success, loading, error = update_store_with_start_app_interval(
            start_app_interval_n_intervals)
    else:
        status = update_store_with_start_button(start_app_button_clicked)
    return status, success, loading,  error


select_table = None


def update_table_section(table_section_style, show_table_button_n_clicks, select_table_interval_n_intervals, table_section):
    global select_table
    data = []
    children = table_section
    disabled = True
    table_section_hided = table_section_style == hide_component

    if table_section_hided:
        return children, True

    table_section_first_render = show_table_button_n_clicks == 1 and not select_table_interval_n_intervals

    if table_section_first_render:
        select_table = select_table_iterator(select_data)
        return children, False

    interval_finished = select_table_interval_n_intervals > max_select_table_iterations

    if not interval_finished and select_table:
        try:
            data, loading, error = next(select_table)
            if data:
                children = TABLE(data)
                disabled = True

            if loading:
                children = ALERT(
                    [SPINNER(size='md', color='dark'), loading], color='light')
                disabled = False

            if error:
                children = ALERT(
                    [SPINNER(size='md'), error], color='danger')
                disabled = True

        except StopIteration:
            disabled = True

    return children, disabled
