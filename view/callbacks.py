from dash import Dash, ctx
from dash.dependencies import Input, Output, State

from controller.callbacks import (disabled_start_app_interval, update_store, update_alert_section, show_start_app_button_spinner, update_start_app_button_text, disabled_start_app_button,
                                  show_control_buttons, show_section, update_table_section, update_chart, update_dimension_dropdown_label, update_other_dimension_dropdown, update_selected_dimension)
from view.constants import COMPONENTS_IDS, STORE_IDS
from view.components import ALERT
from database.constants import (
    AGE_COLUMN,
    BIRTHDAY_COLUMN,
    ETHNICITY_COLUMN,
    GENDER_COLUMN,
    MONTH_YEAR_COLUMN,
    PERIOD_COLUMN,
    REGION_COLUMN,
    SCHOOLING_COLUMN,
    SOCIAL_WELFARE_COLUMN
)
# from controller.orchestrator import start_app, start_app_iterations, map_date, select_app_iterator
# from controller.reader import lang
# from view.constants import COMPONENTS_IDS, STORE_STATE
# from view.components import BAGDE
# from database.constants import TABLES
# from database.connection import select_table


def create_callbacks(app: Dash):

    @ app.callback(
        Output(
            component_id=COMPONENTS_IDS["start_app_interval"], component_property='disabled'),
        Input(
            component_id=STORE_IDS["status"], component_property='data'),
    )
    def disabled_start_app_interval_callback(store_status: str):
        return disabled_start_app_interval(store_status)

    @app.callback(
        Output(
            component_id=STORE_IDS["status"], component_property='data'),
        Output(
            component_id=STORE_IDS["success_message"], component_property='data'),
        Output(
            component_id=STORE_IDS["loading_message"], component_property='data'),
        Output(
            component_id=STORE_IDS["error_message"], component_property='data'),
        Input(
            component_id=COMPONENTS_IDS["start_app_interval"], component_property='n_intervals'),
        Input(
            component_id=COMPONENTS_IDS["start_app_button"], component_property='n_clicks'),
    )
    def update_store_callback(start_app_interval_n_intervals: int, start_app_button_n_clicks: int):
        start_app_button_clicked = bool(start_app_button_n_clicks)
        return update_store(start_app_interval_n_intervals=start_app_interval_n_intervals, start_app_button_clicked=start_app_button_clicked)

    @app.callback(
        Output(
            component_id=COMPONENTS_IDS['alerts_section'], component_property='children'),
        Input(
            component_id=STORE_IDS["success_message"], component_property='data'),
        Input(
            component_id=STORE_IDS["error_message"], component_property='data'),
        State(
            component_id=COMPONENTS_IDS['alerts_section'], component_property='children'),
    )
    def update_alert_section_callback(store_success_message, store_error_message, alerts_section_children):
        return update_alert_section(store_success_message=store_success_message, store_error_message=store_error_message, alerts_section_children=alerts_section_children)

    @app.callback(
        Output(
            component_id=COMPONENTS_IDS['start_app_button_spinner'], component_property='style'),
        Input(
            component_id=STORE_IDS["status"], component_property='data'),
    )
    def show_start_app_button_spinner_callback(store_status):
        return show_start_app_button_spinner(store_status)

    @app.callback(
        Output(
            component_id=COMPONENTS_IDS['start_app_button_text'], component_property='children'),
        Input(
            component_id=STORE_IDS["status"], component_property='data'),
        Input(
            component_id=STORE_IDS["loading_message"], component_property='data'),
    )
    def update_start_app_button_text_callback(store_status, store_loading_message):
        return update_start_app_button_text(store_status=store_status, store_loading_message=store_loading_message)

    @app.callback(
        Output(
            component_id=COMPONENTS_IDS['start_app_button'], component_property='disabled'),
        Input(
            component_id=STORE_IDS["status"], component_property='data'),
    )
    def disabled_start_app_button_callback(store_status):
        return disabled_start_app_button(store_status)

    @app.callback(
        Output(
            component_id=COMPONENTS_IDS["control_buttons"], component_property='style'),
        Input(
            component_id=STORE_IDS["status"], component_property='data'),
    )
    def show_control_buttons_callback(store_status):
        return {'display': 'flex'}
        return show_control_buttons(store_status)

    @app.callback(
        Output(
            component_id=COMPONENTS_IDS["table_section"], component_property='style'),
        Input(
            component_id=COMPONENTS_IDS["show_database_button"], component_property='n_clicks_timestamp'),
        Input(
            component_id=COMPONENTS_IDS["show_charts_button"], component_property='n_clicks_timestamp'),
    )
    def show_table_section_callback(show_database_button_n_clicks_timestamp, show_charts_button_n_clicks_timestamp):
        return show_section(show_button_n_clicks_timestamp=show_database_button_n_clicks_timestamp, hide_button_n_clicks_timestamp=show_charts_button_n_clicks_timestamp)

    @app.callback(
        Output(
            component_id=COMPONENTS_IDS["table_section"], component_property='children'),
        Input(
            component_id=COMPONENTS_IDS["table_section"], component_property='style'),
    )
    def update_table_section_callback(table_section_style):
        return update_table_section(table_section_style=table_section_style)

    @app.callback(
        Output(
            component_id=COMPONENTS_IDS["charts_section"], component_property='style'),
        Input(
            component_id=COMPONENTS_IDS["show_charts_button"], component_property='n_clicks_timestamp'),
        Input(
            component_id=COMPONENTS_IDS["show_database_button"], component_property='n_clicks_timestamp'),
    )
    def show_charts_section_callback(charts_button_n_clicks_timestamp, show_database_button_n_clicks_timestamp):
        return show_section(show_button_n_clicks_timestamp=charts_button_n_clicks_timestamp, hide_button_n_clicks_timestamp=show_database_button_n_clicks_timestamp)

    @app.callback(
        Output(
            component_id=COMPONENTS_IDS["charts_dropdowns"], component_property='style'),
        Input(
            component_id=COMPONENTS_IDS["show_charts_button"], component_property='n_clicks_timestamp'),
        Input(
            component_id=COMPONENTS_IDS["show_database_button"], component_property='n_clicks_timestamp'),
    )
    def show_charts_dropdowns(charts_button_n_clicks_timestamp, show_database_button_n_clicks_timestamp):
        return show_section(show_button_n_clicks_timestamp=charts_button_n_clicks_timestamp, hide_button_n_clicks_timestamp=show_database_button_n_clicks_timestamp)

    @app.callback(
        Output(
            component_id=COMPONENTS_IDS["date_picker_range"], component_property='style'),
        Input(
            component_id=COMPONENTS_IDS["show_charts_button"], component_property='n_clicks_timestamp'),
        Input(
            component_id=COMPONENTS_IDS["show_database_button"], component_property='n_clicks_timestamp'),
    )
    def show_date_picker_range(charts_button_n_clicks_timestamp, show_database_button_n_clicks_timestamp):
        return show_section(show_button_n_clicks_timestamp=charts_button_n_clicks_timestamp, hide_button_n_clicks_timestamp=show_database_button_n_clicks_timestamp)

    @app.callback(
        Output(
            component_id=STORE_IDS["first_dimension"], component_property='data'),
        Output(
            component_id=STORE_IDS["first_dimension_label"], component_property='data'),
        Input(component_id=AGE_COLUMN + '-' + COMPONENTS_IDS['first_dimension_dropdown'],
              component_property="n_clicks_timestamp"),
        Input(component_id=GENDER_COLUMN + '-' + COMPONENTS_IDS['first_dimension_dropdown'],
              component_property="n_clicks_timestamp"),
        Input(component_id=SCHOOLING_COLUMN + '-' + COMPONENTS_IDS['first_dimension_dropdown'],
              component_property="n_clicks_timestamp"),
        Input(component_id=ETHNICITY_COLUMN + '-' + COMPONENTS_IDS['first_dimension_dropdown'],
              component_property="n_clicks_timestamp"),
        Input(component_id=REGION_COLUMN + '-' + COMPONENTS_IDS['first_dimension_dropdown'],
              component_property="n_clicks_timestamp"),
        Input(component_id=SOCIAL_WELFARE_COLUMN + '-' + COMPONENTS_IDS['first_dimension_dropdown'],
              component_property="n_clicks_timestamp"),
        Input(component_id=PERIOD_COLUMN + '-' + COMPONENTS_IDS['first_dimension_dropdown'],
              component_property="n_clicks_timestamp"),
    )
    def update_first_dimension(age_timestamp, gender_timestamp, schooling_timestamp, ethnicity_timestamp, region_timestamp, social_welfare_timestamp, period_timestamp):
        # print('update_first_dimension', ctx.triggered)
        return update_selected_dimension(age_timestamp=age_timestamp, gender_timestamp=gender_timestamp, schooling_timestamp=schooling_timestamp, ethnicity_timestamp=ethnicity_timestamp, region_timestamp=region_timestamp, social_welfare_timestamp=social_welfare_timestamp, period_timestamp=period_timestamp)

    @app.callback(
        Output(
            component_id=STORE_IDS["second_dimension"], component_property='data'),
        Output(
            component_id=STORE_IDS["second_dimension_label"], component_property='data'),
        Input(component_id=AGE_COLUMN + '-' + COMPONENTS_IDS['second_dimension_dropdown'],
              component_property="n_clicks_timestamp"),
        Input(component_id=GENDER_COLUMN + '-' + COMPONENTS_IDS['second_dimension_dropdown'],
              component_property="n_clicks_timestamp"),
        Input(component_id=SCHOOLING_COLUMN + '-' + COMPONENTS_IDS['second_dimension_dropdown'],
              component_property="n_clicks_timestamp"),
        Input(component_id=ETHNICITY_COLUMN + '-' + COMPONENTS_IDS['second_dimension_dropdown'],
              component_property="n_clicks_timestamp"),
        Input(component_id=REGION_COLUMN + '-' + COMPONENTS_IDS['second_dimension_dropdown'],
              component_property="n_clicks_timestamp"),
        Input(component_id=SOCIAL_WELFARE_COLUMN + '-' + COMPONENTS_IDS['second_dimension_dropdown'],
              component_property="n_clicks_timestamp"),
        Input(component_id=PERIOD_COLUMN + '-' + COMPONENTS_IDS['second_dimension_dropdown'],
              component_property="n_clicks_timestamp"),
    )
    def update_second_dimension(age_timestamp, gender_timestamp, schooling_timestamp, ethnicity_timestamp, region_timestamp, social_welfare_timestamp, period_timestamp):
        # print('update_second_dimension', ctx.triggered)
        return update_selected_dimension(age_timestamp=age_timestamp, gender_timestamp=gender_timestamp, schooling_timestamp=schooling_timestamp, ethnicity_timestamp=ethnicity_timestamp, region_timestamp=region_timestamp, social_welfare_timestamp=social_welfare_timestamp, period_timestamp=period_timestamp)

    # @app.callback(
    #     Output(
    #         component_id=COMPONENTS_IDS["first_dimension_dropdown"], component_property='children'),
    #     Input(
    #         component_id=STORE_IDS["second_dimension_label"], component_property='data'),
    #     State(
    #         component_id=COMPONENTS_IDS["first_dimension_dropdown"], component_property='children'),
    # )
    # def update_first_dimension_dropdown(store_second_dimension_label, first_dimension_dropdown):
    #     return update_other_dimension_dropdown(selected_dimension_label=store_second_dimension_label, other_dimension_children=first_dimension_dropdown)

    # @app.callback(
    #     Output(
    #         component_id=COMPONENTS_IDS["second_dimension_dropdown"], component_property='children'),
    #     Input(
    #         component_id=STORE_IDS["first_dimension_label"], component_property='data'),
    #     State(
    #         component_id=COMPONENTS_IDS["second_dimension_dropdown"], component_property='children'),
    # )
    # def update_second_dimension_dropdown(store_first_dimension_label, second_dimension_dropdown):
    #     return update_other_dimension_dropdown(selected_dimension_label=store_first_dimension_label, other_dimension_children=second_dimension_dropdown)

    @app.callback(
        Output(
            component_id=COMPONENTS_IDS["first_dimension_dropdown"], component_property='label'),
        Input(
            component_id=STORE_IDS["first_dimension_label"], component_property='data'),
        Input(
            component_id=STORE_IDS["second_dimension_label"], component_property='data'),
    )
    def update_first_dimension_dropdown_label(store_first_dimension_label, store_second_dimension_label):
        selected_other_dimension = ctx.triggered[0]['prop_id'] == STORE_IDS["second_dimension_label"] + '.data'
        return update_dimension_dropdown_label(dimension_label=store_first_dimension_label, other_dimension_label=store_second_dimension_label, selected_other_dimension=selected_other_dimension)

    @app.callback(
        Output(
            component_id=COMPONENTS_IDS["second_dimension_dropdown"], component_property='label'),
        Input(
            component_id=STORE_IDS["first_dimension_label"], component_property='data'),
        Input(
            component_id=STORE_IDS["second_dimension_label"], component_property='data'),
    )
    def update_second_dimension_dropdown_label(store_first_dimension_label, store_second_dimension_label):
        selected_other_dimension = ctx.triggered[0]['prop_id'] == STORE_IDS["first_dimension_label"] + '.data'
        return update_dimension_dropdown_label(dimension_label=store_second_dimension_label, other_dimension_label=store_first_dimension_label, selected_other_dimension=selected_other_dimension)

    @app.callback(
        Output(
            component_id=COMPONENTS_IDS["charts"], component_property='children'),
        Input(component_id=COMPONENTS_IDS['pie_chart_button'],
              component_property='n_clicks_timestamp'),
        Input(component_id=COMPONENTS_IDS['bar_chart_button'],
              component_property='n_clicks_timestamp'),
        Input(
            component_id=STORE_IDS["first_dimension"], component_property='data'),
        Input(
            component_id=STORE_IDS["second_dimension"], component_property='data'),
        Input(
            component_id=COMPONENTS_IDS["date_picker_range"], component_property='start_date'),
        Input(
            component_id=COMPONENTS_IDS["date_picker_range"], component_property='end_date'),
        Input(
            component_id=STORE_IDS["status"], component_property='data'),
    )
    def update_charts(pie_chart_button_n_clicks_timestamp, bar_chart_button_n_clicks_timestamp, store_first_dimension, store_second_dimension, start_date, end_date, status):
        # print('pie_chart_button_n_clicks_timestamp',
        #       pie_chart_button_n_clicks_timestamp)
        # print('bar_chart_button_n_clicks_timestamp',
        #       bar_chart_button_n_clicks_timestamp)
        return update_chart(pie_chart_button_n_clicks_timestamp=pie_chart_button_n_clicks_timestamp, bar_chart_button_n_clicks_timestamp=bar_chart_button_n_clicks_timestamp, store_first_dimension=store_first_dimension, store_second_dimension=store_second_dimension, start_date=start_date, end_date=end_date)

    return app
    #     @app.callback(
    #         Output(
    #             component_id=STORE_STATE["first_dimension"], component_property='data'),
    #         Output(
    #             component_id=STORE_STATE["first_dimension_label"], component_property='data'),
    #         Input(component_id='age' '-' + COMPONENTS_IDS['bar_chart_first_dimension_dropdown'],
    #               component_property="n_clicks_timestamp"),
    #         Input(component_id="gender" + '-' + COMPONENTS_IDS['bar_chart_first_dimension_dropdown'],
    #               component_property="n_clicks_timestamp"),
    #         Input(component_id="schooling" + '-' + COMPONENTS_IDS['bar_chart_first_dimension_dropdown'],
    #               component_property="n_clicks_timestamp"),
    #         Input(component_id="ethnicity" + '-' + COMPONENTS_IDS['bar_chart_first_dimension_dropdown'],
    #               component_property="n_clicks_timestamp"),
    #         Input(component_id="region" + '-' + COMPONENTS_IDS['bar_chart_first_dimension_dropdown'],
    #               component_property="n_clicks_timestamp"),
    #         Input(component_id="social_welfare" + '-' + COMPONENTS_IDS['bar_chart_first_dimension_dropdown'],
    #               component_property="n_clicks_timestamp"),
    #     )
    #     def update_first_dimension(age_timestamp, gender_timestamp, schooling_timestamp, ethnicity_timestamp, region_timestamp, social_welfare_timestamp):
    #         selected_field = list(filter(lambda dimension: dimension is not None, [age_timestamp, gender_timestamp, schooling_timestamp, ethnicity_timestamp,
    #                                                                                region_timestamp, social_welfare_timestamp]))
    #         current_timestamp = 0

    #         if len(selected_field):
    #             current_timestamp = max(selected_field)

    #         if current_timestamp == age_timestamp:
    #             return "age", dropdown_options["age"]
    #         if current_timestamp == gender_timestamp:
    #             return "gender", dropdown_options["gender"],
    #         if current_timestamp == schooling_timestamp:
    #             return "schooling", dropdown_options["schooling"],
    #         if current_timestamp == ethnicity_timestamp:
    #             return "ethnicity", dropdown_options["ethnicity"],
    #         if current_timestamp == region_timestamp:
    #             return "region", dropdown_options["region"],
    #         if current_timestamp == social_welfare_timestamp:
    #             return "social_welfare", dropdown_options["social_welfare"]

    #         # if current_timestamp == period_timestamp:
    #         #     return "period", dropdown_options["period"], "region"

    #         return "empty", lang("dropdown_label")

    #     @app.callback(
    #         Output(
    #             component_id=COMPONENTS_IDS["control_section"], component_property='style'),
    #         Input(
    #             component_id=COMPONENTS_IDS["charts_button"], component_property='n_clicks_timestamp'),
    #         Input(
    #             component_id=COMPONENTS_IDS["hide_charts_button"], component_property='n_clicks_timestamp'),
    #     )
    #     def update_control_section(charts_button_n_clicks_timestamp, hide_charts_button_n_clicks_timestamp):
    #         if charts_button_n_clicks_timestamp is None and hide_charts_button_n_clicks_timestamp is None:
    #             return show_component
    #         if charts_button_n_clicks_timestamp is not None and hide_charts_button_n_clicks_timestamp is None:
    #             return hide_component
    #         if charts_button_n_clicks_timestamp is None and hide_charts_button_n_clicks_timestamp is not None:
    #             return show_component
    #         if charts_button_n_clicks_timestamp > hide_charts_button_n_clicks_timestamp:
    #             return hide_component
    #         if charts_button_n_clicks_timestamp < hide_charts_button_n_clicks_timestamp:
    #             return show_component
    #         return show_component

    #     @app.callback(
    #         Output(
    #             component_id=COMPONENTS_IDS["charts_section"], component_property='style'),
    #         Input(
    #             component_id=COMPONENTS_IDS["charts_button"], component_property='n_clicks_timestamp'),
    #         Input(
    #             component_id=COMPONENTS_IDS["hide_charts_button"], component_property='n_clicks_timestamp'),
    #     )
    #     def update_charts_section(charts_button_n_clicks_timestamp, hide_charts_button_n_clicks_timestamp):
    #         if charts_button_n_clicks_timestamp is None and hide_charts_button_n_clicks_timestamp is None:
    #             return hide_component
    #         if charts_button_n_clicks_timestamp is not None and hide_charts_button_n_clicks_timestamp is None:
    #             return show_component
    #         if charts_button_n_clicks_timestamp is None and hide_charts_button_n_clicks_timestamp is not None:
    #             return hide_component
    #         if charts_button_n_clicks_timestamp > hide_charts_button_n_clicks_timestamp:
    #             return show_component
    #         if charts_button_n_clicks_timestamp < hide_charts_button_n_clicks_timestamp:
    #             return hide_component
    #         return hide_component

    #     @app.callback(
    #         Output(
    #             component_id=COMPONENTS_IDS["bar_chart_dropdowns"], component_property='style'),
    #         Input(component_id=COMPONENTS_IDS['pie_chart_button'],
    #               component_property='n_clicks_timestamp'),
    #         Input(component_id=COMPONENTS_IDS['bar_chart_button'],
    #               component_property='n_clicks_timestamp'),
    #     )
    #     def update_bar_chart_dropdowns(pie_chart_dropdown_click, bar_chart_dropdown_click):
    #         if bar_chart_dropdown_click is None and pie_chart_dropdown_click is None:
    #             return hide_component
    #         if bar_chart_dropdown_click is not None and pie_chart_dropdown_click is None:
    #             return show_component
    #         if bar_chart_dropdown_click is None and pie_chart_dropdown_click is not None:
    #             return hide_component
    #         if bar_chart_dropdown_click > pie_chart_dropdown_click:
    #             return show_component
    #         if bar_chart_dropdown_click < pie_chart_dropdown_click:
    #             return hide_component
    #         return hide_component

    #     @ app.callback(
    #         Output(
    #             component_id=STORE_STATE["second_dimension"], component_property='data'),
    #         Output(
    #             component_id=STORE_STATE["second_dimension_label"], component_property='data'),
    #         Input(component_id='age' '-' + COMPONENTS_IDS['bar_chart_second_dimension_dropdown'],
    #               component_property="n_clicks_timestamp"),
    #         Input(component_id="gender" + '-' + COMPONENTS_IDS['bar_chart_second_dimension_dropdown'],
    #               component_property="n_clicks_timestamp"),
    #         Input(component_id="schooling" + '-' + COMPONENTS_IDS['bar_chart_second_dimension_dropdown'],
    #               component_property="n_clicks_timestamp"),
    #         Input(component_id="ethnicity" + '-' + COMPONENTS_IDS['bar_chart_second_dimension_dropdown'],
    #               component_property="n_clicks_timestamp"),
    #         Input(component_id="region" + '-' + COMPONENTS_IDS['bar_chart_second_dimension_dropdown'],
    #               component_property="n_clicks_timestamp"),
    #         Input(component_id="social_welfare" + '-' + COMPONENTS_IDS['bar_chart_second_dimension_dropdown'],
    #               component_property="n_clicks_timestamp"),
    #     )
    #     def update_second_dimension(age_timestamp, gender_timestamp, schooling_timestamp, ethnicity_timestamp, region_timestamp, social_welfare_timestamp):
    #         selectec_field = list(filter(lambda dimension: dimension is not None, [age_timestamp, gender_timestamp, schooling_timestamp, ethnicity_timestamp,
    #                                                                                region_timestamp, social_welfare_timestamp]))
    #         current_timestamp = 0

    #         if len(selectec_field):
    #             current_timestamp = max(selectec_field)

    #         if current_timestamp == age_timestamp:
    #             return "age", dropdown_options["age"]
    #         if current_timestamp == gender_timestamp:
    #             return "gender", dropdown_options["gender"],
    #         if current_timestamp == schooling_timestamp:
    #             return "schooling", dropdown_options["schooling"],
    #         if current_timestamp == ethnicity_timestamp:
    #             return "ethnicity", dropdown_options["ethnicity"],
    #         if current_timestamp == region_timestamp:
    #             return "region", dropdown_options["region"],
    #         if current_timestamp == social_welfare_timestamp:
    #             return "social_welfare", dropdown_options["social_welfare"]

    #         return "empty", lang("dropdown_label")

    #     def map_data(data):
    #         dimensions = {}
    #         mapped_data = []
    #         for amout, first_dimension, second_dimension in data:
    #             if first_dimension not in dimensions.keys():
    #                 dimensions[first_dimension] = {}
    #             if second_dimension not in dimensions[first_dimension].keys():
    #                 dimensions[first_dimension][second_dimension] = amout
    #             else:
    #                 dimensions[first_dimension][second_dimension] = [
    #                     *dimensions[first_dimension][second_dimension], amout]
    #         for first_dimension in dimensions.keys():
    #             second_dimensions = dimensions[first_dimension].keys()
    #             amouts = dimensions[first_dimension].values()
    #             mapped_data.append(
    #                 {'type': 'bar', 'name': first_dimension, 'x': list(second_dimensions), 'y': list(amouts)})
    #         return mapped_data

    #     @ app.callback(
    #         Output(
    #             component_id=COMPONENTS_IDS["bar_chart"], component_property='figure'),
    #         Input(
    #             component_id=STORE_STATE["first_dimension"], component_property='data'),
    #         Input(
    #             component_id=STORE_STATE["second_dimension"], component_property='data'),
    #         Input(
    #             component_id=COMPONENTS_IDS["date_range"], component_property='start_date'),
    #         Input(
    #             component_id=COMPONENTS_IDS["date_range"], component_property='end_date'),
    #         # State(
    #         #     component_id=COMPONENTS_IDS["bar_chart_first_dimension_dropdown"], component_property='children'),
    #     )
    #     def update_bar_chart(first_dimension, second_dimension, start_date, end_date):
    #         data = []

    #         filledFilters = first_dimension != 'empty' and second_dimension != 'empty' and start_date and end_date

    #         if filledFilters:
    #             min_year, min_month = map_date(start_date)
    #             max_year, max_month = map_date(end_date)
    #             data_raw = select_app_iterator(column_1=first_dimension, column_2=second_dimension,
    #                                            max_month=max_month, max_year=max_year, min_year=min_year, min_month=min_month)
    #             print('data_raw', data_raw)
    #             data = map_data(data_raw)

    #         return {"data": data}
