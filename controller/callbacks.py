from dash import ctx

from controller.orchestrator import max_start_app_iterations, start_app, select_data, max_select_app_iterations, select_data_now
from dash import (dash_table, dcc, html)
from controller.reader import lang
from controller.mapper import map_date, map_bar_chart_data
from view.constants import STATUS_TYPES
from view.components import ALERT, SUCCESS_ICON, ERROR_ICON, TABLE, BAR_CHART, PIE_CHART
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


def disabled_start_app_interval(store_status: str):
    return store_status == STATUS_TYPES['uninitialized'] or store_status == STATUS_TYPES['finished']


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


def update_store_with_start_button(start_app_button_clicked: bool):
    if start_app_button_clicked:
        return STATUS_TYPES['initialized']
    else:
        return STATUS_TYPES['uninitialized']


def update_store(start_app_interval_n_intervals: int, start_app_button_clicked: bool):
    status = STATUS_TYPES['uninitialized']
    success = ''
    loading = ''
    error = ''
    print("start_app_interval_n_intervals", start_app_interval_n_intervals)
    if start_app_interval_n_intervals:
        status, success, loading, error = update_store_with_start_app_interval(
            start_app_interval_n_intervals)
    else:
        status = update_store_with_start_button(start_app_button_clicked)
    return status, success, loading,  error


def update_alert_section(store_success_message: str, store_error_message: str, alerts_section_children: any):
    if store_success_message and not alerts_section_children:
        return [ALERT([SUCCESS_ICON(), store_success_message])]
    elif store_success_message and alerts_section_children:
        return [*alerts_section_children, ALERT([SUCCESS_ICON(), store_success_message])]
    elif store_error_message and not alerts_section_children:
        return [ALERT([ERROR_ICON(), store_error_message], color='danger')]
    elif store_error_message and alerts_section_children:
        return [*alerts_section_children, ALERT([ERROR_ICON(), store_error_message], color='danger')]
    return alerts_section_children


def show_start_app_button_spinner(store_status: str):
    if store_status == STATUS_TYPES['initialized']:
        return show_component
    else:
        return hide_component


def update_start_app_button_text(store_status: str, store_loading_message: str):
    if store_status == STATUS_TYPES['uninitialized'] or store_status == STATUS_TYPES['finished']:
        return lang("component_start_app_label")
    elif store_status == STATUS_TYPES['initialized']:
        return store_loading_message
    return ''


def disabled_start_app_button(store_status: str):
    return store_status == STATUS_TYPES['finished']


def show_control_buttons(store_status: str):
    if store_status == STATUS_TYPES['finished']:
        return show_component
    else:
        return hide_component


def update_table_section(table_section_style, show_database_button_n_clicks, select_table_interval_n_intervals, table_section):
    data = []
    children = table_section
    disabled = True
    table_section_hided = table_section_style == hide_component
    if table_section_hided:
        return children, True

    table_section_first_render = show_database_button_n_clicks == 1 and not select_table_interval_n_intervals

    if table_section_first_render:
        return children, False

    interval_finished = select_table_interval_n_intervals > max_select_app_iterations

    if not interval_finished:
        try:
            data, _, loading, error = next(select_data)
            if data:
                children = TABLE(data)
                disabled = True

            if loading:
                children = loading
                disabled = False

            if error:
                children = error
                disabled = True

        except StopIteration:
            disabled = True

    return children, disabled


def show_section(show_button_n_clicks_timestamp, hide_button_n_clicks_timestamp):
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


def hide_option(child, value):
    if child['props']['children'] == value:
        child['props']['class_name'] = 'default-hide-section'
    else:
        child['props']['class_name'] = 'default-show-section'
    return child


def update_selected_dimension(age_timestamp, gender_timestamp, schooling_timestamp, ethnicity_timestamp, region_timestamp, social_welfare_timestamp, period_timestamp):
    selected_field = list(filter(lambda dimension: dimension is not None, [age_timestamp, gender_timestamp, schooling_timestamp, ethnicity_timestamp,
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


def update_other_dimension_dropdown(selected_dimension_label, other_dimension_children):
    return list(map(lambda child: (hide_option(child=child, value=selected_dimension_label)), other_dimension_children))


def update_dimension_dropdown_label(dimension_label, other_dimension_label, selected_other_dimension):
    sameLabel = dimension_label == other_dimension_label
    is_selected = dimension_label != lang("component_dropdown_label")
    if sameLabel and is_selected and selected_other_dimension:
        return lang("component_dropdown_label")
    return dimension_label


def get_pie_chart(first_dimension, second_dimension, start_date, end_date, select_chart_interval_n_intervals):
    data = []
    min_year = ''
    min_month = ''
    max_year = ''
    max_month = ''
    hasDistinctDimensions = first_dimension != second_dimension
    hasDimensions = first_dimension and first_dimension != 'empty' and second_dimension and second_dimension != 'empty'
    hasPeriod = start_date and end_date
    has_some_period = start_date or end_date
    if hasPeriod:
        min_year, min_month = map_date(start_date)
        max_year, max_month = map_date(end_date)

    if hasDimensions and hasDistinctDimensions:
        first_dimension_range = PUC_DB_HOMELESS_COLUMNS_RANGES[first_dimension]
        second_dimension_values = {}
        for first_dimension_value in first_dimension_range:
            value_data_raw, _, error = select_data_now(first_column=first_dimension, second_column=second_dimension, first_column_value=first_dimension_value,
                                                       max_month=max_month, max_year=max_year, min_year=min_year, min_month=min_month)
            for amout, second_dimension_value in value_data_raw:
                try:
                    second_dimension_values[second_dimension_value].append(
                        amout)
                except:
                    second_dimension_values[second_dimension_value] = [amout]
        return [PIE_CHART(first_dimension_values=first_dimension_range, second_dimension_values=second_dimension_values)]
    return data


# def calling():
#     keep_loop = True
#     while keep_loop:


def get_bar_chart(first_dimension, second_dimension, start_date, end_date, select_chart_interval_n_intervals):
    data = []
    min_year = ''
    min_month = ''
    max_year = ''
    max_month = ''
    hasDistinctDimensions = first_dimension != second_dimension
    hasDimensions = first_dimension and first_dimension != 'empty' and second_dimension and second_dimension != 'empty'
    hasPeriod = start_date and end_date
    if hasPeriod:
        min_year, min_month = map_date(start_date)
        max_year, max_month = map_date(end_date)

    if hasDimensions and hasDistinctDimensions:
        first_dimension_range = PUC_DB_HOMELESS_COLUMNS_RANGES[first_dimension]
        for first_dimension_value in first_dimension_range:
            value_data_raw, success, error = select_data_now(first_column=first_dimension, second_column=second_dimension, first_column_value=first_dimension_value,
                                                             max_month=max_month, max_year=max_year, min_year=min_year, min_month=min_month)
            amouts = []
            second_dimension_values = []
            print('value_data_raw', value_data_raw)
            for amout, second_dimension_value in value_data_raw:

                amouts.append(amout)
                second_dimension_values.append(second_dimension_value)
            data.append({'type': 'bar', 'name': first_dimension_value,
                         'x': second_dimension_values, 'y': amouts})
        return [BAR_CHART(figure={"data": data})]
    return data


def update_charts(pie_chart_button_n_clicks_timestamp, bar_chart_button_n_clicks_timestamp, store_first_dimension, store_second_dimension, start_date, end_date, select_chart_interval_n_intervals):
    if pie_chart_button_n_clicks_timestamp is None and bar_chart_button_n_clicks_timestamp is None:
        return ''
    if pie_chart_button_n_clicks_timestamp is not None and bar_chart_button_n_clicks_timestamp is None:
        return get_pie_chart(first_dimension=store_first_dimension, second_dimension=store_second_dimension, start_date=start_date, end_date=end_date, select_chart_interval_n_intervals=select_chart_interval_n_intervals)
    if pie_chart_button_n_clicks_timestamp is None and bar_chart_button_n_clicks_timestamp is not None:
        return get_bar_chart(first_dimension=store_first_dimension, second_dimension=store_second_dimension, start_date=start_date, end_date=end_date, select_chart_interval_n_intervals=select_chart_interval_n_intervals)
    if pie_chart_button_n_clicks_timestamp > bar_chart_button_n_clicks_timestamp:
        return get_pie_chart(first_dimension=store_first_dimension, second_dimension=store_second_dimension, start_date=start_date, end_date=end_date, select_chart_interval_n_intervals=select_chart_interval_n_intervals)
    if pie_chart_button_n_clicks_timestamp < bar_chart_button_n_clicks_timestamp:
        return get_bar_chart(first_dimension=store_first_dimension, second_dimension=store_second_dimension, start_date=start_date, end_date=end_date, select_chart_interval_n_intervals=select_chart_interval_n_intervals)
    return ''
