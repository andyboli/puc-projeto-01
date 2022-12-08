from dash import Dash, ctx
from dash.dependencies import Input, Output, State

from controller.callbacks import (disabled_start_app_interval, update_store, update_alert_section, show_start_app_button_spinner, update_start_app_button_text, disabled_start_app_button,
                                  show_control_buttons, show_section, update_table_section, update_charts, update_dimension_dropdown_label, update_other_dimension_dropdown, update_selected_dimension)
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


def create_callbacks(app: Dash):

    @app.callback(
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
            component_id=COMPONENTS_IDS["show_database_button"], component_property='disabled'),
        Input(
            component_id=COMPONENTS_IDS["select_table_interval"], component_property='disabled'),
    )
    def disabled_show_database_button_callback(select_table_interval_disabled):
        return not select_table_interval_disabled

    @app.callback(
        Output(
            component_id=COMPONENTS_IDS["table_section"], component_property='children'),
        Output(
            component_id=COMPONENTS_IDS["select_table_interval"], component_property='disabled'),
        Input(
            component_id=COMPONENTS_IDS["table_section"], component_property='style'),
        Input(
            component_id=COMPONENTS_IDS["show_database_button"], component_property='n_clicks'),
        Input(
            component_id=COMPONENTS_IDS["select_table_interval"], component_property='n_intervals'),
        State(
            component_id=COMPONENTS_IDS["table_section"], component_property='children'),
    )
    def update_table_section_callback(table_section_style, show_database_button_n_clicks, select_table_interval_n_intervals, table_section):
        return update_table_section(table_section_style=table_section_style, show_database_button_n_clicks=show_database_button_n_clicks, select_table_interval_n_intervals=select_table_interval_n_intervals, table_section=table_section)

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
            component_id=COMPONENTS_IDS["pie_chart_button"], component_property='n_clicks_timestamp'),
        Input(
            component_id=COMPONENTS_IDS['bar_chart_button'], component_property='n_clicks_timestamp'),
        Input(
            component_id=COMPONENTS_IDS["show_database_button"], component_property='n_clicks_timestamp'),
    )
    def show_charts_dropdowns(pie_chart_button_n_clicks_timestamp, bar_chart_button_n_clicks_timestamp, show_database_button_n_clicks_timestamp):
        show_button_n_clicks_timestamp = pie_chart_button_n_clicks_timestamp
        if ctx.triggered[0]['prop_id'] == COMPONENTS_IDS["bar_chart_button"] + '.n_clicks_timestamp':
            show_button_n_clicks_timestamp = bar_chart_button_n_clicks_timestamp
        return show_section(show_button_n_clicks_timestamp=show_button_n_clicks_timestamp, hide_button_n_clicks_timestamp=show_database_button_n_clicks_timestamp)

    @app.callback(
        Output(
            component_id=COMPONENTS_IDS["date_picker_range"], component_property='style'),
        Input(
            component_id=COMPONENTS_IDS["pie_chart_button"], component_property='n_clicks_timestamp'),
        Input(
            component_id=COMPONENTS_IDS['bar_chart_button'], component_property='n_clicks_timestamp'),
        Input(
            component_id=COMPONENTS_IDS["show_database_button"], component_property='n_clicks_timestamp'),
    )
    def show_date_picker_range(pie_chart_button_n_clicks_timestamp, bar_chart_button_n_clicks_timestamp, show_database_button_n_clicks_timestamp):
        show_button_n_clicks_timestamp = pie_chart_button_n_clicks_timestamp
        if ctx.triggered[0]['prop_id'] == COMPONENTS_IDS["bar_chart_button"] + '.n_clicks_timestamp':
            show_button_n_clicks_timestamp = bar_chart_button_n_clicks_timestamp
        return show_section(show_button_n_clicks_timestamp=show_button_n_clicks_timestamp, hide_button_n_clicks_timestamp=show_database_button_n_clicks_timestamp)

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
        return update_selected_dimension(age_timestamp=age_timestamp, gender_timestamp=gender_timestamp, schooling_timestamp=schooling_timestamp, ethnicity_timestamp=ethnicity_timestamp, region_timestamp=region_timestamp, social_welfare_timestamp=social_welfare_timestamp, period_timestamp=period_timestamp)

    @app.callback(
        Output(
            component_id=COMPONENTS_IDS["first_dimension_dropdown"], component_property='label'),
        Input(
            component_id=STORE_IDS["first_dimension_label"], component_property='data'),
        Input(
            component_id=STORE_IDS["second_dimension_label"], component_property='data'),
    )
    def update_first_dimension_dropdown_label_callback(store_first_dimension_label, store_second_dimension_label):
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
    def update_second_dimension_dropdown_label_callback(store_first_dimension_label, store_second_dimension_label):
        selected_other_dimension = ctx.triggered[0]['prop_id'] == STORE_IDS["first_dimension_label"] + '.data'
        return update_dimension_dropdown_label(dimension_label=store_second_dimension_label, other_dimension_label=store_first_dimension_label, selected_other_dimension=selected_other_dimension)

    # @app.callback(
    #     Output(
    #         component_id=COMPONENTS_IDS["charts"], component_property='children'),
    #     Input(component_id=COMPONENTS_IDS['pie_chart_button'],
    #           component_property='n_clicks_timestamp'),
    #     Input(component_id=COMPONENTS_IDS['bar_chart_button'],
    #           component_property='n_clicks_timestamp'),
    #     Input(
    #         component_id=STORE_IDS["first_dimension"], component_property='data'),
    #     Input(
    #         component_id=STORE_IDS["second_dimension"], component_property='data'),
    #     Input(
    #         component_id=COMPONENTS_IDS["date_picker_range"], component_property='start_date'),
    #     Input(
    #         component_id=COMPONENTS_IDS["date_picker_range"], component_property='end_date'),
    #     Input(
    #         component_id=STORE_IDS["status"], component_property='data'),
    # )
    # def update_charts_callback(pie_chart_button_n_clicks_timestamp, bar_chart_button_n_clicks_timestamp, store_first_dimension, store_second_dimension, start_date, end_date, status):
    #     return update_charts(pie_chart_button_n_clicks_timestamp=pie_chart_button_n_clicks_timestamp, bar_chart_button_n_clicks_timestamp=bar_chart_button_n_clicks_timestamp, store_first_dimension=store_first_dimension, store_second_dimension=store_second_dimension, start_date=start_date, end_date=end_date)

    @app.callback(
        Output(component_id=COMPONENTS_IDS['pie_chart_button'],
               component_property='disabled'),
        Output(component_id=COMPONENTS_IDS['bar_chart_button'],
               component_property='disabled'),
        Output(
            component_id=COMPONENTS_IDS["first_dimension_dropdown"], component_property='disabled'),
        Output(
            component_id=COMPONENTS_IDS["second_dimension_dropdown"], component_property='disabled'),
        Output(
            component_id=COMPONENTS_IDS["date_picker_range"], component_property='disabled'),
        Input(
            component_id=COMPONENTS_IDS["select_chart_interval"], component_property='disabled'),
    )
    def disabled_charts_buttons(select_chart_interval_disabled):
        return not select_chart_interval_disabled, not select_chart_interval_disabled, not select_chart_interval_disabled, not select_chart_interval_disabled, not select_chart_interval_disabled

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
            component_id=COMPONENTS_IDS["select_chart_interval"], component_property='n_intervals'),
    )
    def update_charts_callback(pie_chart_button_n_clicks_timestamp, bar_chart_button_n_clicks_timestamp, store_first_dimension, store_second_dimension, start_date, end_date, select_chart_interval_n_intervals):
        return update_charts(pie_chart_button_n_clicks_timestamp=pie_chart_button_n_clicks_timestamp, bar_chart_button_n_clicks_timestamp=bar_chart_button_n_clicks_timestamp, store_first_dimension=store_first_dimension, store_second_dimension=store_second_dimension, start_date=start_date, end_date=end_date, select_chart_interval_n_intervals=select_chart_interval_n_intervals)


# @app.callback(
#         Output(
#             component_id=COMPONENTS_IDS["charts"], component_property='children'),
#         Input(component_id=COMPONENTS_IDS['pie_chart_button'],
#               component_property='n_clicks_timestamp'),
#         Input(component_id=COMPONENTS_IDS['bar_chart_button'],
#               component_property='n_clicks_timestamp'),
#         Input(
#             component_id=STORE_IDS["first_dimension"], component_property='data'),
#         Input(
#             component_id=STORE_IDS["second_dimension"], component_property='data'),
#         Input(
#             component_id=COMPONENTS_IDS["date_picker_range"], component_property='start_date'),
#         Input(
#             component_id=COMPONENTS_IDS["date_picker_range"], component_property='end_date'),
#         Input(
#             component_id=STORE_IDS["status"], component_property='data'),
#     )
#     def update_charts_callback(pie_chart_button_n_clicks_timestamp, bar_chart_button_n_clicks_timestamp, store_first_dimension, store_second_dimension, start_date, end_date, status):
#         return update_charts(pie_chart_button_n_clicks_timestamp=pie_chart_button_n_clicks_timestamp, bar_chart_button_n_clicks_timestamp=bar_chart_button_n_clicks_timestamp, store_first_dimension=store_first_dimension, store_second_dimension=store_second_dimension, start_date=start_date, end_date=end_date)

    #  @app.callback(
    #     Output(
    #         component_id=COMPONENTS_IDS["table_section"], component_property='style'),
    #     Input(
    #         component_id=COMPONENTS_IDS["show_database_button"], component_property='n_clicks_timestamp'),
    #     Input(
    #         component_id=COMPONENTS_IDS["show_charts_button"], component_property='n_clicks_timestamp'),
    # )
    # def show_table_section_callback(show_database_button_n_clicks_timestamp, show_charts_button_n_clicks_timestamp):
    #     return show_section(show_button_n_clicks_timestamp=show_database_button_n_clicks_timestamp, hide_button_n_clicks_timestamp=show_charts_button_n_clicks_timestamp)

    # @app.callback(
    #     Output(
    #         component_id=COMPONENTS_IDS["show_database_button"], component_property='disabled'),
    #     Input(
    #         component_id=COMPONENTS_IDS["select_table_interval"], component_property='disabled'),
    # )
    # def disabled_show_database_button_callback(select_table_interval_disabled):
    #     return not select_table_interval_disabled

    # @app.callback(
    #     Output(
    #         component_id=COMPONENTS_IDS["table_section"], component_property='children'),
    #     Output(
    #         component_id=COMPONENTS_IDS["select_table_interval"], component_property='disabled'),
    #     Input(
    #         component_id=COMPONENTS_IDS["table_section"], component_property='style'),
    #     Input(
    #         component_id=COMPONENTS_IDS["show_database_button"], component_property='n_clicks'),
    #     Input(
    #         component_id=COMPONENTS_IDS["select_table_interval"], component_property='n_intervals'),
    #     State(
    #         component_id=COMPONENTS_IDS["table_section"], component_property='children'),
    # )
    # def update_table_section_callback(table_section_style, show_database_button_n_clicks, select_table_interval_n_intervals, table_section):
    #     return update_table_section(table_section_style=table_section_style, show_database_button_n_clicks=show_database_button_n_clicks, select_table_interval_n_intervals=select_table_interval_n_intervals, table_section=table_section)

    return app
