from dash import Dash, ctx
from dash.dependencies import Input, Output, State

from controller.callbacks import (disabled_start_app_interval, update_store, update_alert_section, display_start_app_button_spinner, update_start_app_button_text, disabled_start_app_button,
                                  display_control_buttons, display_section, update_table_section, update_column_dropdown_label, update_selected_column, get_pie_chart, disabled_create_graph_button, update_chart, get_bar_chart, hide_component)
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
            component_id=COMPONENTS_IDS['start_app_button_spinner'], component_property='style'),
        Input(
            component_id=STORE_IDS["status"], component_property='data'),
    )
    def display_start_app_button_spinner_callback(status):
        return display_start_app_button_spinner(status)

    @app.callback(
        Output(
            component_id=COMPONENTS_IDS['start_app_button'], component_property='disabled'),
        Input(
            component_id=STORE_IDS["status"], component_property='data'),
    )
    def disabled_start_app_button_callback(status):
        return disabled_start_app_button(status)

    @app.callback(
        Output(
            component_id=COMPONENTS_IDS['start_app_button_text'], component_property='children'),
        Input(
            component_id=STORE_IDS["status"], component_property='data'),
        Input(
            component_id=STORE_IDS["loading_message"], component_property='data'),
    )
    def update_start_app_button_text_callback(status, loading_message):
        return update_start_app_button_text(status=status, loading_message=loading_message)

    @app.callback(
        Output(
            component_id=COMPONENTS_IDS["start_app_interval"], component_property='disabled'),
        Input(
            component_id=STORE_IDS["status"], component_property='data'),
    )
    def disabled_start_app_interval_callback(status: str):
        return disabled_start_app_interval(status)

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
    def update_alert_section_callback(success_message, error_message, alerts_section):
        return update_alert_section(success_message=success_message, error_message=error_message, alerts_section=alerts_section)

    @app.callback(
        Output(
            component_id=COMPONENTS_IDS["control_buttons"], component_property='style'),
        Input(
            component_id=STORE_IDS["status"], component_property='data'),
    )
    def display_control_buttons_callback(status):
        return {'display': 'flex'}
        return display_control_buttons(status)

    @app.callback(
        Output(
            component_id=COMPONENTS_IDS["table_section"], component_property='style'),
        Input(
            component_id=COMPONENTS_IDS["show_table_button"], component_property='n_clicks_timestamp'),
        Input(
            component_id=COMPONENTS_IDS["show_charts_button"], component_property='n_clicks_timestamp'),
    )
    def display_table_section_callback(show_table_button_n_clicks_timestamp, show_charts_button_n_clicks_timestamp):
        return display_section(show_button_n_clicks_timestamp=show_table_button_n_clicks_timestamp, hide_button_n_clicks_timestamp=show_charts_button_n_clicks_timestamp)

    @app.callback(
        Output(
            component_id=COMPONENTS_IDS["table_section"], component_property='children'),
        Output(
            component_id=COMPONENTS_IDS["select_table_interval"], component_property='disabled'),
        Input(
            component_id=COMPONENTS_IDS["table_section"], component_property='style'),
        Input(
            component_id=COMPONENTS_IDS["show_table_button"], component_property='n_clicks'),
        Input(
            component_id=COMPONENTS_IDS["select_table_interval"], component_property='n_intervals'),
        State(
            component_id=COMPONENTS_IDS["table_section"], component_property='children'),
    )
    def update_table_section_callback(table_section_style, show_table_button_n_clicks, select_table_interval_n_intervals, table_section):
        return update_table_section(table_section_style=table_section_style, show_table_button_n_clicks=show_table_button_n_clicks, select_table_interval_n_intervals=select_table_interval_n_intervals, table_section=table_section)

    @app.callback(
        Output(
            component_id=COMPONENTS_IDS["show_table_button"], component_property='disabled'),
        Input(
            component_id=COMPONENTS_IDS["select_table_interval"], component_property='disabled'),
    )
    def disabled_show_table_button_callback(select_table_interval_disabled):
        return not select_table_interval_disabled

    @app.callback(
        Output(
            component_id=COMPONENTS_IDS["charts_section"], component_property='style'),
        Input(
            component_id=COMPONENTS_IDS["show_charts_button"], component_property='n_clicks_timestamp'),
        Input(
            component_id=COMPONENTS_IDS["show_table_button"], component_property='n_clicks_timestamp'),
    )
    def display_charts_section_callback(charts_button_n_clicks_timestamp, show_table_button_n_clicks_timestamp):
        return display_section(show_button_n_clicks_timestamp=charts_button_n_clicks_timestamp, hide_button_n_clicks_timestamp=show_table_button_n_clicks_timestamp)

    @app.callback(
        Output(
            component_id=COMPONENTS_IDS["charts_control_section"], component_property='style'),
        Input(
            component_id=COMPONENTS_IDS["pie_chart_button"], component_property='n_clicks_timestamp'),
        Input(
            component_id=COMPONENTS_IDS['bar_chart_button'], component_property='n_clicks_timestamp'),
        Input(
            component_id=COMPONENTS_IDS["show_table_button"], component_property='n_clicks_timestamp'),
    )
    def display_charts_dropdowns(pie_chart_button_n_clicks_timestamp, bar_chart_button_n_clicks_timestamp, show_table_button_n_clicks_timestamp):
        show_button_n_clicks_timestamp = pie_chart_button_n_clicks_timestamp
        if ctx.triggered[0]['prop_id'] == COMPONENTS_IDS["bar_chart_button"] + '.n_clicks_timestamp':
            show_button_n_clicks_timestamp = bar_chart_button_n_clicks_timestamp
        return display_section(show_button_n_clicks_timestamp=show_button_n_clicks_timestamp, hide_button_n_clicks_timestamp=show_table_button_n_clicks_timestamp)

    @app.callback(
        Output(
            component_id=STORE_IDS["first_column"], component_property='data'),
        Output(
            component_id=STORE_IDS["first_column_label"], component_property='data'),
        Input(component_id=AGE_COLUMN + '-' + COMPONENTS_IDS['first_column_dropdown'],
              component_property="n_clicks_timestamp"),
        Input(component_id=GENDER_COLUMN + '-' + COMPONENTS_IDS['first_column_dropdown'],
              component_property="n_clicks_timestamp"),
        Input(component_id=SCHOOLING_COLUMN + '-' + COMPONENTS_IDS['first_column_dropdown'],
              component_property="n_clicks_timestamp"),
        Input(component_id=ETHNICITY_COLUMN + '-' + COMPONENTS_IDS['first_column_dropdown'],
              component_property="n_clicks_timestamp"),
        Input(component_id=REGION_COLUMN + '-' + COMPONENTS_IDS['first_column_dropdown'],
              component_property="n_clicks_timestamp"),
        Input(component_id=SOCIAL_WELFARE_COLUMN + '-' + COMPONENTS_IDS['first_column_dropdown'],
              component_property="n_clicks_timestamp"),
        Input(component_id=PERIOD_COLUMN + '-' + COMPONENTS_IDS['first_column_dropdown'],
              component_property="n_clicks_timestamp"),
    )
    def update_first_column(age_timestamp, gender_timestamp, schooling_timestamp, ethnicity_timestamp, region_timestamp, social_welfare_timestamp, period_timestamp):
        return update_selected_column(age_timestamp=age_timestamp, gender_timestamp=gender_timestamp, schooling_timestamp=schooling_timestamp, ethnicity_timestamp=ethnicity_timestamp, region_timestamp=region_timestamp, social_welfare_timestamp=social_welfare_timestamp, period_timestamp=period_timestamp)

    @app.callback(
        Output(
            component_id=STORE_IDS["second_column"], component_property='data'),
        Output(
            component_id=STORE_IDS["second_column_label"], component_property='data'),
        Input(component_id=AGE_COLUMN + '-' + COMPONENTS_IDS['second_column_dropdown'],
              component_property="n_clicks_timestamp"),
        Input(component_id=GENDER_COLUMN + '-' + COMPONENTS_IDS['second_column_dropdown'],
              component_property="n_clicks_timestamp"),
        Input(component_id=SCHOOLING_COLUMN + '-' + COMPONENTS_IDS['second_column_dropdown'],
              component_property="n_clicks_timestamp"),
        Input(component_id=ETHNICITY_COLUMN + '-' + COMPONENTS_IDS['second_column_dropdown'],
              component_property="n_clicks_timestamp"),
        Input(component_id=REGION_COLUMN + '-' + COMPONENTS_IDS['second_column_dropdown'],
              component_property="n_clicks_timestamp"),
        Input(component_id=SOCIAL_WELFARE_COLUMN + '-' + COMPONENTS_IDS['second_column_dropdown'],
              component_property="n_clicks_timestamp"),
        Input(component_id=PERIOD_COLUMN + '-' + COMPONENTS_IDS['second_column_dropdown'],
              component_property="n_clicks_timestamp"),
    )
    def update_second_column(age_timestamp, gender_timestamp, schooling_timestamp, ethnicity_timestamp, region_timestamp, social_welfare_timestamp, period_timestamp):
        return update_selected_column(age_timestamp=age_timestamp, gender_timestamp=gender_timestamp, schooling_timestamp=schooling_timestamp, ethnicity_timestamp=ethnicity_timestamp, region_timestamp=region_timestamp, social_welfare_timestamp=social_welfare_timestamp, period_timestamp=period_timestamp)

    @app.callback(
        Output(
            component_id=COMPONENTS_IDS["first_column_dropdown"], component_property='label'),
        Input(
            component_id=STORE_IDS["first_column_label"], component_property='data'),
        Input(
            component_id=STORE_IDS["second_column_label"], component_property='data'),
    )
    def update_first_column_dropdown_label_callback(first_column_label, second_column_label):
        selected_other_column = ctx.triggered[0]['prop_id'] == STORE_IDS["second_column_label"] + '.data'
        return update_column_dropdown_label(column_label=first_column_label, other_column_label=second_column_label, selected_other_column=selected_other_column)

    @app.callback(
        Output(
            component_id=COMPONENTS_IDS["second_column_dropdown"], component_property='label'),
        Input(
            component_id=STORE_IDS["first_column_label"], component_property='data'),
        Input(
            component_id=STORE_IDS["second_column_label"], component_property='data'),
    )
    def update_second_column_dropdown_label_callback(first_column_label, second_column_label):
        selected_other_column = ctx.triggered[0]['prop_id'] == STORE_IDS["first_column_label"] + '.data'
        return update_column_dropdown_label(column_label=second_column_label, other_column_label=first_column_label, selected_other_column=selected_other_column)

    @app.callback(
        Output(
            component_id=COMPONENTS_IDS["bar_chart"], component_property='style'),
        Input(
            component_id=COMPONENTS_IDS["bar_chart_button"], component_property='n_clicks_timestamp'),
        Input(
            component_id=COMPONENTS_IDS["pie_chart_button"], component_property='n_clicks_timestamp'),
    )
    def display_bar_chart_callback(bar_chart_button_n_clicks_timestamp, pie_chart_button_n_clicks_timestamp):
        return display_section(show_button_n_clicks_timestamp=bar_chart_button_n_clicks_timestamp, hide_button_n_clicks_timestamp=pie_chart_button_n_clicks_timestamp)

    @app.callback(
        Output(
            component_id=COMPONENTS_IDS["pie_chart"], component_property='style'),
        Input(
            component_id=COMPONENTS_IDS["bar_chart_button"], component_property='n_clicks_timestamp'),
        Input(
            component_id=COMPONENTS_IDS["pie_chart_button"], component_property='n_clicks_timestamp'),
    )
    def display_pie_chart_callback(bar_chart_button_n_clicks_timestamp, pie_chart_button_n_clicks_timestamp):
        return display_section(show_button_n_clicks_timestamp=pie_chart_button_n_clicks_timestamp, hide_button_n_clicks_timestamp=bar_chart_button_n_clicks_timestamp)

    @app.callback(
        Output(
            component_id=COMPONENTS_IDS["create_graph_button"], component_property='disabled'),
        Input(
            component_id=STORE_IDS["first_column"], component_property='data'),
        Input(
            component_id=STORE_IDS["second_column"], component_property='data'),
        Input(
            component_id=COMPONENTS_IDS["date_picker_range"], component_property='start_date'),
        Input(
            component_id=COMPONENTS_IDS["date_picker_range"], component_property='end_date'),
    )
    def disabled_create_graph_button_callback(first_column, second_column, start_date, end_date):
        return disabled_create_graph_button(first_column=first_column, second_column=second_column, start_date=start_date, end_date=end_date)

    @app.callback(
        Output(
            component_id=COMPONENTS_IDS["bar_chart"], component_property='children'),
        Input(
            component_id=COMPONENTS_IDS["create_graph_button"], component_property='n_clicks'),
        State(
            component_id=STORE_IDS["first_column"], component_property='data'),
        State(
            component_id=STORE_IDS["second_column"], component_property='data'),
        State(
            component_id=COMPONENTS_IDS["date_picker_range"], component_property='start_date'),
        State(
            component_id=COMPONENTS_IDS["date_picker_range"], component_property='end_date'),
        State(
            component_id=COMPONENTS_IDS["bar_chart"], component_property='style'),
    )
    def update_bar_chart_callback(create_graph_button_n_clicks, first_column, second_column, start_date, end_date, bar_chart_style):
        if bar_chart_style == hide_component:
            return []
        return update_chart(create_graph_button_n_clicks=create_graph_button_n_clicks, first_column=first_column, second_column=second_column, start_date=start_date, end_date=end_date, chart_callback=get_bar_chart)

    @app.callback(
        Output(
            component_id=COMPONENTS_IDS["pie_chart"], component_property='children'),
        Input(
            component_id=COMPONENTS_IDS["create_graph_button"], component_property='n_clicks'),
        State(
            component_id=STORE_IDS["first_column"], component_property='data'),
        State(
            component_id=STORE_IDS["second_column"], component_property='data'),
        State(
            component_id=COMPONENTS_IDS["date_picker_range"], component_property='start_date'),
        State(
            component_id=COMPONENTS_IDS["date_picker_range"], component_property='end_date'),
        State(
            component_id=COMPONENTS_IDS["pie_chart"], component_property='style'),
    )
    def update_pie_chart_callback(create_graph_button_n_clicks, first_column, second_column, start_date, end_date, pie_chart_style):
        print("pie_chart_style == hide_component", pie_chart_style,
              pie_chart_style == hide_component)
        if pie_chart_style == hide_component:
            return []
        return update_chart(create_graph_button_n_clicks=create_graph_button_n_clicks, first_column=first_column, second_column=second_column, start_date=start_date, end_date=end_date, chart_callback=get_pie_chart)


# hello

    return app

    @app.callback(
        Output(
            component_id=COMPONENTS_IDS["bar_chart"], component_property='children'),
        Output(
            component_id=COMPONENTS_IDS["select_chart_interval"], component_property='disabled'),
        Output(
            component_id=COMPONENTS_IDS["charts_control_section"], component_property='disabled'),
        Input(
            component_id=COMPONENTS_IDS["select_chart_interval"], component_property='n_intervals'),
        Input(
            component_id=STORE_IDS["first_column"], component_property='data'),
        Input(
            component_id=STORE_IDS["second_column"], component_property='data'),
        Input(
            component_id=COMPONENTS_IDS["date_picker_range"], component_property='start_date'),
        Input(
            component_id=COMPONENTS_IDS["date_picker_range"], component_property='end_date'),
        State(
            component_id=COMPONENTS_IDS["select_chart_interval"], component_property='disabled'),
        State(
            component_id=COMPONENTS_IDS["bar_chart"], component_property='children'),
    )
    def update_bar_chart_callback(select_chart_interval_n_intervals, first_column, second_column, start_date, end_date, select_chart_interval_disabled, bar_chart):
        return update_bar_chart(select_chart_interval_n_intervals=select_chart_interval_n_intervals, first_column=first_column, second_column=second_column, start_date=start_date, end_date=end_date, select_chart_interval_disabled=select_chart_interval_disabled, bar_chart=bar_chart)

    @app.callback(
        Output(
            component_id=COMPONENTS_IDS["select_chart_interval"], component_property='disabled'),
        Input(
            component_id=STORE_IDS["first_column"], component_property='data'),
        Input(
            component_id=STORE_IDS["second_column"], component_property='data'),
        Input(
            component_id=COMPONENTS_IDS["date_picker_range"], component_property='start_date'),
        Input(
            component_id=COMPONENTS_IDS["date_picker_range"], component_property='end_date'),
        State(
            component_id=COMPONENTS_IDS["select_chart_interval"], component_property='disabled'),
    )
    def disabled_select_chart_interval_callback(first_column, second_column, start_date, end_date, select_chart_interval_disabled):
        return disabled_select_chart_interval(first_column=first_column, second_column=second_column, start_date=start_date, end_date=end_date, select_chart_interval_disabled=select_chart_interval_disabled)

    @app.callback(
        Output(
            component_id=COMPONENTS_IDS["date_picker_range"], component_property='style'),
        Input(
            component_id=COMPONENTS_IDS["pie_chart_button"], component_property='n_clicks_timestamp'),
        Input(
            component_id=COMPONENTS_IDS['bar_chart_button'], component_property='n_clicks_timestamp'),
        Input(
            component_id=COMPONENTS_IDS["show_table_button"], component_property='n_clicks_timestamp'),
    )
    def display_date_picker_range(pie_chart_button_n_clicks_timestamp, bar_chart_button_n_clicks_timestamp, show_table_button_n_clicks_timestamp):
        show_button_n_clicks_timestamp = pie_chart_button_n_clicks_timestamp
        if ctx.triggered[0]['prop_id'] == COMPONENTS_IDS["bar_chart_button"] + '.n_clicks_timestamp':
            show_button_n_clicks_timestamp = bar_chart_button_n_clicks_timestamp
        return display_section(show_button_n_clicks_timestamp=show_button_n_clicks_timestamp, hide_button_n_clicks_timestamp=show_table_button_n_clicks_timestamp)

    # @app.callback(
    #     Output(
    #         component_id=COMPONENTS_IDS["charts"], component_property='children'),
    #     Input(component_id=COMPONENTS_IDS['pie_chart_button'],
    #           component_property='n_clicks_timestamp'),
    #     Input(component_id=COMPONENTS_IDS['bar_chart_button'],
    #           component_property='n_clicks_timestamp'),
    #     Input(
    #         component_id=STORE_IDS["first_column"], component_property='data'),
    #     Input(
    #         component_id=STORE_IDS["second_column"], component_property='data'),
    #     Input(
    #         component_id=COMPONENTS_IDS["date_picker_range"], component_property='start_date'),
    #     Input(
    #         component_id=COMPONENTS_IDS["date_picker_range"], component_property='end_date'),
    #     Input(
    #         component_id=STORE_IDS["status"], component_property='data'),
    # )
    # def update_charts_callback(pie_chart_button_n_clicks_timestamp, bar_chart_button_n_clicks_timestamp, store_first_column, store_second_column, start_date, end_date, status):
    #     return update_charts(pie_chart_button_n_clicks_timestamp=pie_chart_button_n_clicks_timestamp, bar_chart_button_n_clicks_timestamp=bar_chart_button_n_clicks_timestamp, store_first_column=store_first_column, store_second_column=store_second_column, start_date=start_date, end_date=end_date)

    @app.callback(
        Output(component_id=COMPONENTS_IDS['pie_chart_button'],
               component_property='disabled'),
        Output(component_id=COMPONENTS_IDS['bar_chart_button'],
               component_property='disabled'),
        Output(
            component_id=COMPONENTS_IDS["first_column_dropdown"], component_property='disabled'),
        Output(
            component_id=COMPONENTS_IDS["second_column_dropdown"], component_property='disabled'),
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
            component_id=STORE_IDS["first_column"], component_property='data'),
        Input(
            component_id=STORE_IDS["second_column"], component_property='data'),
        Input(
            component_id=COMPONENTS_IDS["date_picker_range"], component_property='start_date'),
        Input(
            component_id=COMPONENTS_IDS["date_picker_range"], component_property='end_date'),
        Input(
            component_id=COMPONENTS_IDS["select_chart_interval"], component_property='n_intervals'),
    )
    def update_charts_callback(pie_chart_button_n_clicks_timestamp, bar_chart_button_n_clicks_timestamp, store_first_column, store_second_column, start_date, end_date, select_chart_interval_n_intervals):
        return update_charts(pie_chart_button_n_clicks_timestamp=pie_chart_button_n_clicks_timestamp, bar_chart_button_n_clicks_timestamp=bar_chart_button_n_clicks_timestamp, store_first_column=store_first_column, store_second_column=store_second_column, start_date=start_date, end_date=end_date, select_chart_interval_n_intervals=select_chart_interval_n_intervals)


# @app.callback(
#         Output(
#             component_id=COMPONENTS_IDS["charts"], component_property='children'),
#         Input(component_id=COMPONENTS_IDS['pie_chart_button'],
#               component_property='n_clicks_timestamp'),
#         Input(component_id=COMPONENTS_IDS['bar_chart_button'],
#               component_property='n_clicks_timestamp'),
#         Input(
#             component_id=STORE_IDS["first_column"], component_property='data'),
#         Input(
#             component_id=STORE_IDS["second_column"], component_property='data'),
#         Input(
#             component_id=COMPONENTS_IDS["date_picker_range"], component_property='start_date'),
#         Input(
#             component_id=COMPONENTS_IDS["date_picker_range"], component_property='end_date'),
#         Input(
#             component_id=STORE_IDS["status"], component_property='data'),
#     )
#     def update_charts_callback(pie_chart_button_n_clicks_timestamp, bar_chart_button_n_clicks_timestamp, store_first_column, store_second_column, start_date, end_date, status):
#         return update_charts(pie_chart_button_n_clicks_timestamp=pie_chart_button_n_clicks_timestamp, bar_chart_button_n_clicks_timestamp=bar_chart_button_n_clicks_timestamp, store_first_column=store_first_column, store_second_column=store_second_column, start_date=start_date, end_date=end_date)

    #  @app.callback(
    #     Output(
    #         component_id=COMPONENTS_IDS["table_section"], component_property='style'),
    #     Input(
    #         component_id=COMPONENTS_IDS["show_table_button"], component_property='n_clicks_timestamp'),
    #     Input(
    #         component_id=COMPONENTS_IDS["show_charts_button"], component_property='n_clicks_timestamp'),
    # )
    # def show_table_section_callback(show_table_button_n_clicks_timestamp, show_charts_button_n_clicks_timestamp):
    #     return show_section(show_button_n_clicks_timestamp=show_table_button_n_clicks_timestamp, hide_button_n_clicks_timestamp=show_charts_button_n_clicks_timestamp)

    # @app.callback(
    #     Output(
    #         component_id=COMPONENTS_IDS["show_table_button"], component_property='disabled'),
    #     Input(
    #         component_id=COMPONENTS_IDS["select_table_interval"], component_property='disabled'),
    # )
    # def disabled_show_table_button_callback(select_table_interval_disabled):
    #     return not select_table_interval_disabled

    # @app.callback(
    #     Output(
    #         component_id=COMPONENTS_IDS["table_section"], component_property='children'),
    #     Output(
    #         component_id=COMPONENTS_IDS["select_table_interval"], component_property='disabled'),
    #     Input(
    #         component_id=COMPONENTS_IDS["table_section"], component_property='style'),
    #     Input(
    #         component_id=COMPONENTS_IDS["show_table_button"], component_property='n_clicks'),
    #     Input(
    #         component_id=COMPONENTS_IDS["select_table_interval"], component_property='n_intervals'),
    #     State(
    #         component_id=COMPONENTS_IDS["table_section"], component_property='children'),
    # )
    # def update_table_section_callback(table_section_style, show_table_button_n_clicks, select_table_interval_n_intervals, table_section):
    #     return update_table_section(table_section_style=table_section_style, show_table_button_n_clicks=show_table_button_n_clicks, select_table_interval_n_intervals=select_table_interval_n_intervals, table_section=table_section)
