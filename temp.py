# import pandas as pd


# # rua = pd.read_csv(r'C:\Users\gusta\OneDrive\Documentos\Curso - TBD\1º Semestre\Projeto\data_set_poprua_cadunico-07-2022.csv',
# #                   encoding='cp860', delimiter=';', usecols=[0, 1, 2, 3, 4, 5, 7, 8, 9, 10, 11, 12])
# # rua['Faixa_etaria'] = rua.apply(faixa_etaria, axis=1)
# # print(rua)

# # def map_homeless_data_range(mapped_data: list):
# #     """receive all mapped csv data from assets/csv/homeless
# #     headers: a list of homeless headers
# #     header: a set with distinct values from a homeless header

# #     return  {headers: list, [header]: set}
# #     """
# #
# #     month_years: set = set()
# #     ages: set = set()
# #     genders: set = set()
# #     birthdays: set = set()
# #     schoolings: set = set()
# #     ethinicities: set = set()
# #     regions: set = set()
# #     periods: set = set()
# #     social_welfares: set = set()
# #     for data in mapped_data:
# #         month_years.add(data[0])
# #         ages.add(data[1])
# #         genders.add(data[2])
# #         birthdays.add(data[3])
# #         schoolings.add(data[4])
# #         ethinicities.add(data[5])
# #         regions.add(data[6])
# #         periods.add(data[7])
# #         social_welfares.add(data[8])
# #     return {
# #         "headers": headers,
# #         "month_years": month_years,
# #         "ages": ages,
# #         "genders": genders,
# #         "birthdays": birthdays,
# #         "schoolings": schoolings,
# #         "ethinicities": ethinicities,
# #         "regions": regions,
# #         "periods": periods,
# #         "social_welfares": social_welfares,
# #     }


# # labels = ["US", "China", "European Union", "Russian Federation", "Brazil", "India",
# #           "Rest of World"]

# # # Create subplots: use 'domain' type for Pie subplot
# # fig = make_subplots(rows=1, cols=2, specs=[
# #                     [{'type': 'domain'}, {'type': 'domain'}]])
# # fig.add_trace(go.Pie(labels=labels, values=[16, 15, 12, 6, 5, 4, 42], name="GHG Emissions"),
# #               1, 1)
# # fig.add_trace(go.Pie(labels=labels, values=[27, 11, 25, 8, 1, 3, 25], name="CO2 Emissions"),
# #               1, 2)

# # # Use `hole` to create a donut-like pie chart
# # fig.update_traces(hole=.4, hoverinfo="label+percent+name")

# # fig.update_layout(
# #     title_text="Global Emissions 1990-2011",
# #     # Add annotations in the center of the donut pies.
# #     annotations=[dict(text='GHG', x=0.18, y=0.5, font_size=20, showarrow=False),
# #                  dict(text='CO2', x=0.82, y=0.5, font_size=20, showarrow=False)])


# # PIE_GRAPH = dcc.Graph(figure=fig, id="pie-graph", className="hide")


# # GRAPH_SECTION = [BAR_GRAPH, PIE_GRAPH]


# # table_query = get_query(first_column, second_column,
# #                             max_year, min_year, min_month, max_month)


# # def select_data(first_column: str = '', second_column: str = '', first_column_value: str = '', max_year: str = '', min_year: str = '', min_month: str = '', max_month: str = ''):
# #     """Calls select_table with default values.

# #     Args:
# #         first_column (str,): First column to group data.
# #         second_column (str,): Second column to group data.
# #         first_column_value (str): First column value to filter data.
# #         max_year (str): Max year to filter data.
# #         min_year (str): Min year to filter data.
# #         min_month (str): Min month to filter data.
# #         max_month (str): Max month to filter data.

# #     Yields:
# #         data (list): Data filtered from table
# #         success (str): Success message.
# #         loading (str): Loading message.
# #         error (str): Error message.
# #     """
# #     # yield None, '', lang('select_table_start'), ''
# #     table_query = get_query(first_column=first_column, second_column=second_column, first_column_value=first_column_value, max_year=max_year,
# #                             min_year=min_year, min_month=min_month, max_month=max_month)
# #     data, success, error = select_table(table_query=table_query)
# #     # print("success", success)
# #     # print("error", error)
# #     # print("data", data)
# #     return data
# #     # data, success, error = select_table(table_query=table_query)
# #     # yield data, success, '', error


# # # select_data = select_data_iterator()

# # max_select_data_iterations = 2


# # def update_column_dropdown_label(selected_column_label, other_column_label):
# #     sameLabel = selected_column_label == other_column_label
# #     is_selected = selected_column_label != lang("component_dropdown_label")
# #     if sameLabel and is_selected:
# #         return lang("component_dropdown_label")
# #     return other_column_label


# # def select_data_now(first_column: str = '', second_column: str = '', first_column_value: str = '', max_year: str = '', min_year: str = '', min_month: str = '', max_month: str = ''):
# #     table_query = get_query(first_column=first_column, second_column=second_column, first_column_value=first_column_value, max_year=max_year,
# #                             min_year=min_year, min_month=min_month, max_month=max_month)
# #     data, success, error = select_table(table_query=table_query)
# #     return data, success, error


# from dash import Dash, ctx
# from dash.dependencies import Input, Output, State

# from controller.callbacks import (disabled_start_app_interval, update_store, update_alert_section, show_start_app_button_spinner, update_start_app_button_text, disabled_start_app_button,
#                                   show_control_buttons, show_section, update_table_section, update_charts, update_column_dropdown_label, update_other_column_dropdown, update_selected_column)
# from view.constants import COMPONENTS_IDS, STORE_IDS
# from view.components import ALERT
# from database.constants import (
#     AGE_COLUMN,
#     BIRTHDAY_COLUMN,
#     ETHNICITY_COLUMN,
#     GENDER_COLUMN,
#     MONTH_YEAR_COLUMN,
#     PERIOD_COLUMN,
#     REGION_COLUMN,
#     SCHOOLING_COLUMN,
#     SOCIAL_WELFARE_COLUMN
# )


# def create_callbacks(app: Dash):

#     @app.callback(
#         Output(
#             component_id=COMPONENTS_IDS["start_app_interval"], component_property='disabled'),
#         Input(
#             component_id=STORE_IDS["status"], component_property='data'),
#     )
#     def disabled_start_app_interval_callback(store_status: str):
#         return disabled_start_app_interval(store_status)

#     @app.callback(
#         Output(
#             component_id=STORE_IDS["status"], component_property='data'),
#         Output(
#             component_id=STORE_IDS["success_message"], component_property='data'),
#         Output(
#             component_id=STORE_IDS["loading_message"], component_property='data'),
#         Output(
#             component_id=STORE_IDS["error_message"], component_property='data'),
#         Input(
#             component_id=COMPONENTS_IDS["start_app_interval"], component_property='n_intervals'),
#         Input(
#             component_id=COMPONENTS_IDS["start_app_button"], component_property='n_clicks'),
#     )
#     def update_store_callback(start_app_interval_n_intervals: int, start_app_button_n_clicks: int):
#         start_app_button_clicked = bool(start_app_button_n_clicks)
#         return update_store(start_app_interval_n_intervals=start_app_interval_n_intervals, start_app_button_clicked=start_app_button_clicked)

#     @app.callback(
#         Output(
#             component_id=COMPONENTS_IDS['alerts_section'], component_property='children'),
#         Input(
#             component_id=STORE_IDS["success_message"], component_property='data'),
#         Input(
#             component_id=STORE_IDS["error_message"], component_property='data'),
#         State(
#             component_id=COMPONENTS_IDS['alerts_section'], component_property='children'),
#     )
#     def update_alert_section_callback(store_success_message, store_error_message, alerts_section_children):
#         return update_alert_section(store_success_message=store_success_message, store_error_message=store_error_message, alerts_section_children=alerts_section_children)

#     @app.callback(
#         Output(
#             component_id=COMPONENTS_IDS['start_app_button_spinner'], component_property='style'),
#         Input(
#             component_id=STORE_IDS["status"], component_property='data'),
#     )
#     def show_start_app_button_spinner_callback(store_status):
#         return show_start_app_button_spinner(store_status)

#     @app.callback(
#         Output(
#             component_id=COMPONENTS_IDS['start_app_button_text'], component_property='children'),
#         Input(
#             component_id=STORE_IDS["status"], component_property='data'),
#         Input(
#             component_id=STORE_IDS["loading_message"], component_property='data'),
#     )
#     def update_start_app_button_text_callback(store_status, store_loading_message):
#         return update_start_app_button_text(store_status=store_status, store_loading_message=store_loading_message)

#     @app.callback(
#         Output(
#             component_id=COMPONENTS_IDS['start_app_button'], component_property='disabled'),
#         Input(
#             component_id=STORE_IDS["status"], component_property='data'),
#     )
#     def disabled_start_app_button_callback(store_status):
#         return disabled_start_app_button(store_status)

#     @app.callback(
#         Output(
#             component_id=COMPONENTS_IDS["control_buttons"], component_property='style'),
#         Input(
#             component_id=STORE_IDS["status"], component_property='data'),
#     )
#     def show_control_buttons_callback(store_status):
#         return {'display': 'flex'}
#         return show_control_buttons(store_status)

#     @app.callback(
#         Output(
#             component_id=COMPONENTS_IDS["table_section"], component_property='style'),
#         Input(
#             component_id=COMPONENTS_IDS["show_table_button"], component_property='n_clicks_timestamp'),
#         Input(
#             component_id=COMPONENTS_IDS["show_charts_button"], component_property='n_clicks_timestamp'),
#     )
#     def show_table_section_callback(show_table_button_n_clicks_timestamp, show_charts_button_n_clicks_timestamp):
#         return show_section(show_button_n_clicks_timestamp=show_table_button_n_clicks_timestamp, hide_button_n_clicks_timestamp=show_charts_button_n_clicks_timestamp)

#     @app.callback(
#         Output(
#             component_id=COMPONENTS_IDS["show_table_button"], component_property='disabled'),
#         Input(
#             component_id=COMPONENTS_IDS["select_table_interval"], component_property='disabled'),
#     )
#     def disabled_show_table_button_callback(select_table_interval_disabled):
#         return not select_table_interval_disabled

#     @app.callback(
#         Output(
#             component_id=COMPONENTS_IDS["table_section"], component_property='children'),
#         Output(
#             component_id=COMPONENTS_IDS["select_table_interval"], component_property='disabled'),
#         Input(
#             component_id=COMPONENTS_IDS["table_section"], component_property='style'),
#         Input(
#             component_id=COMPONENTS_IDS["show_table_button"], component_property='n_clicks'),
#         Input(
#             component_id=COMPONENTS_IDS["select_table_interval"], component_property='n_intervals'),
#         State(
#             component_id=COMPONENTS_IDS["table_section"], component_property='children'),
#     )
#     def update_table_section_callback(table_section_style, show_table_button_n_clicks, select_table_interval_n_intervals, table_section):
#         return update_table_section(table_section_style=table_section_style, show_table_button_n_clicks=show_table_button_n_clicks, select_table_interval_n_intervals=select_table_interval_n_intervals, table_section=table_section)

#     @app.callback(
#         Output(
#             component_id=COMPONENTS_IDS["charts_section"], component_property='style'),
#         Input(
#             component_id=COMPONENTS_IDS["show_charts_button"], component_property='n_clicks_timestamp'),
#         Input(
#             component_id=COMPONENTS_IDS["show_table_button"], component_property='n_clicks_timestamp'),
#     )
#     def show_charts_section_callback(charts_button_n_clicks_timestamp, show_table_button_n_clicks_timestamp):
#         return show_section(show_button_n_clicks_timestamp=charts_button_n_clicks_timestamp, hide_button_n_clicks_timestamp=show_table_button_n_clicks_timestamp)

#     @app.callback(
#         Output(
#             component_id=COMPONENTS_IDS["charts_dropdowns"], component_property='style'),
#         Input(
#             component_id=COMPONENTS_IDS["pie_chart_button"], component_property='n_clicks_timestamp'),
#         Input(
#             component_id=COMPONENTS_IDS['bar_chart_button'], component_property='n_clicks_timestamp'),
#         Input(
#             component_id=COMPONENTS_IDS["show_table_button"], component_property='n_clicks_timestamp'),
#     )
#     def show_charts_dropdowns(pie_chart_button_n_clicks_timestamp, bar_chart_button_n_clicks_timestamp, show_table_button_n_clicks_timestamp):
#         show_button_n_clicks_timestamp = pie_chart_button_n_clicks_timestamp
#         if ctx.triggered[0]['prop_id'] == COMPONENTS_IDS["bar_chart_button"] + '.n_clicks_timestamp':
#             show_button_n_clicks_timestamp = bar_chart_button_n_clicks_timestamp
#         return show_section(show_button_n_clicks_timestamp=show_button_n_clicks_timestamp, hide_button_n_clicks_timestamp=show_table_button_n_clicks_timestamp)

#     @app.callback(
#         Output(
#             component_id=COMPONENTS_IDS["date_picker_range"], component_property='style'),
#         Input(
#             component_id=COMPONENTS_IDS["pie_chart_button"], component_property='n_clicks_timestamp'),
#         Input(
#             component_id=COMPONENTS_IDS['bar_chart_button'], component_property='n_clicks_timestamp'),
#         Input(
#             component_id=COMPONENTS_IDS["show_table_button"], component_property='n_clicks_timestamp'),
#     )
#     def show_date_picker_range(pie_chart_button_n_clicks_timestamp, bar_chart_button_n_clicks_timestamp, show_table_button_n_clicks_timestamp):
#         show_button_n_clicks_timestamp = pie_chart_button_n_clicks_timestamp
#         if ctx.triggered[0]['prop_id'] == COMPONENTS_IDS["bar_chart_button"] + '.n_clicks_timestamp':
#             show_button_n_clicks_timestamp = bar_chart_button_n_clicks_timestamp
#         return show_section(show_button_n_clicks_timestamp=show_button_n_clicks_timestamp, hide_button_n_clicks_timestamp=show_table_button_n_clicks_timestamp)

#     @app.callback(
#         Output(
#             component_id=STORE_IDS["first_column"], component_property='data'),
#         Output(
#             component_id=STORE_IDS["first_column_label"], component_property='data'),
#         Input(component_id=AGE_COLUMN + '-' + COMPONENTS_IDS['first_column_dropdown'],
#               component_property="n_clicks_timestamp"),
#         Input(component_id=GENDER_COLUMN + '-' + COMPONENTS_IDS['first_column_dropdown'],
#               component_property="n_clicks_timestamp"),
#         Input(component_id=SCHOOLING_COLUMN + '-' + COMPONENTS_IDS['first_column_dropdown'],
#               component_property="n_clicks_timestamp"),
#         Input(component_id=ETHNICITY_COLUMN + '-' + COMPONENTS_IDS['first_column_dropdown'],
#               component_property="n_clicks_timestamp"),
#         Input(component_id=REGION_COLUMN + '-' + COMPONENTS_IDS['first_column_dropdown'],
#               component_property="n_clicks_timestamp"),
#         Input(component_id=SOCIAL_WELFARE_COLUMN + '-' + COMPONENTS_IDS['first_column_dropdown'],
#               component_property="n_clicks_timestamp"),
#         Input(component_id=PERIOD_COLUMN + '-' + COMPONENTS_IDS['first_column_dropdown'],
#               component_property="n_clicks_timestamp"),
#     )
#     def update_first_column(age_timestamp, gender_timestamp, schooling_timestamp, ethnicity_timestamp, region_timestamp, social_welfare_timestamp, period_timestamp):
#         return update_selected_column(age_timestamp=age_timestamp, gender_timestamp=gender_timestamp, schooling_timestamp=schooling_timestamp, ethnicity_timestamp=ethnicity_timestamp, region_timestamp=region_timestamp, social_welfare_timestamp=social_welfare_timestamp, period_timestamp=period_timestamp)

#     @app.callback(
#         Output(
#             component_id=STORE_IDS["second_column"], component_property='data'),
#         Output(
#             component_id=STORE_IDS["second_column_label"], component_property='data'),
#         Input(component_id=AGE_COLUMN + '-' + COMPONENTS_IDS['second_column_dropdown'],
#               component_property="n_clicks_timestamp"),
#         Input(component_id=GENDER_COLUMN + '-' + COMPONENTS_IDS['second_column_dropdown'],
#               component_property="n_clicks_timestamp"),
#         Input(component_id=SCHOOLING_COLUMN + '-' + COMPONENTS_IDS['second_column_dropdown'],
#               component_property="n_clicks_timestamp"),
#         Input(component_id=ETHNICITY_COLUMN + '-' + COMPONENTS_IDS['second_column_dropdown'],
#               component_property="n_clicks_timestamp"),
#         Input(component_id=REGION_COLUMN + '-' + COMPONENTS_IDS['second_column_dropdown'],
#               component_property="n_clicks_timestamp"),
#         Input(component_id=SOCIAL_WELFARE_COLUMN + '-' + COMPONENTS_IDS['second_column_dropdown'],
#               component_property="n_clicks_timestamp"),
#         Input(component_id=PERIOD_COLUMN + '-' + COMPONENTS_IDS['second_column_dropdown'],
#               component_property="n_clicks_timestamp"),
#     )
#     def update_second_column(age_timestamp, gender_timestamp, schooling_timestamp, ethnicity_timestamp, region_timestamp, social_welfare_timestamp, period_timestamp):
#         return update_selected_column(age_timestamp=age_timestamp, gender_timestamp=gender_timestamp, schooling_timestamp=schooling_timestamp, ethnicity_timestamp=ethnicity_timestamp, region_timestamp=region_timestamp, social_welfare_timestamp=social_welfare_timestamp, period_timestamp=period_timestamp)

#     @app.callback(
#         Output(
#             component_id=COMPONENTS_IDS["first_column_dropdown"], component_property='label'),
#         Input(
#             component_id=STORE_IDS["first_column_label"], component_property='data'),
#         Input(
#             component_id=STORE_IDS["second_column_label"], component_property='data'),
#     )
#     def update_first_column_dropdown_label_callback(store_first_column_label, store_second_column_label):
#         selected_other_column = ctx.triggered[0]['prop_id'] == STORE_IDS["second_column_label"] + '.data'
#         return update_column_dropdown_label(column_label=store_first_column_label, other_column_label=store_second_column_label, selected_other_column=selected_other_column)

#     @app.callback(
#         Output(
#             component_id=COMPONENTS_IDS["second_column_dropdown"], component_property='label'),
#         Input(
#             component_id=STORE_IDS["first_column_label"], component_property='data'),
#         Input(
#             component_id=STORE_IDS["second_column_label"], component_property='data'),
#     )
#     def update_second_column_dropdown_label_callback(store_first_column_label, store_second_column_label):
#         selected_other_column = ctx.triggered[0]['prop_id'] == STORE_IDS["first_column_label"] + '.data'
#         return update_column_dropdown_label(column_label=store_second_column_label, other_column_label=store_first_column_label, selected_other_column=selected_other_column)

#     # @app.callback(
#     #     Output(
#     #         component_id=COMPONENTS_IDS["charts"], component_property='children'),
#     #     Input(component_id=COMPONENTS_IDS['pie_chart_button'],
#     #           component_property='n_clicks_timestamp'),
#     #     Input(component_id=COMPONENTS_IDS['bar_chart_button'],
#     #           component_property='n_clicks_timestamp'),
#     #     Input(
#     #         component_id=STORE_IDS["first_column"], component_property='data'),
#     #     Input(
#     #         component_id=STORE_IDS["second_column"], component_property='data'),
#     #     Input(
#     #         component_id=COMPONENTS_IDS["date_picker_range"], component_property='start_date'),
#     #     Input(
#     #         component_id=COMPONENTS_IDS["date_picker_range"], component_property='end_date'),
#     #     Input(
#     #         component_id=STORE_IDS["status"], component_property='data'),
#     # )
#     # def update_charts_callback(pie_chart_button_n_clicks_timestamp, bar_chart_button_n_clicks_timestamp, store_first_column, store_second_column, start_date, end_date, status):
#     #     return update_charts(pie_chart_button_n_clicks_timestamp=pie_chart_button_n_clicks_timestamp, bar_chart_button_n_clicks_timestamp=bar_chart_button_n_clicks_timestamp, store_first_column=store_first_column, store_second_column=store_second_column, start_date=start_date, end_date=end_date)

#     @app.callback(
#         Output(component_id=COMPONENTS_IDS['pie_chart_button'],
#                component_property='disabled'),
#         Output(component_id=COMPONENTS_IDS['bar_chart_button'],
#                component_property='disabled'),
#         Output(
#             component_id=COMPONENTS_IDS["first_column_dropdown"], component_property='disabled'),
#         Output(
#             component_id=COMPONENTS_IDS["second_column_dropdown"], component_property='disabled'),
#         Output(
#             component_id=COMPONENTS_IDS["date_picker_range"], component_property='disabled'),
#         Input(
#             component_id=COMPONENTS_IDS["select_chart_interval"], component_property='disabled'),
#     )
#     def disabled_charts_buttons(select_chart_interval_disabled):
#         return not select_chart_interval_disabled, not select_chart_interval_disabled, not select_chart_interval_disabled, not select_chart_interval_disabled, not select_chart_interval_disabled

#     @app.callback(
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
#             component_id=COMPONENTS_IDS["select_chart_interval"], component_property='n_intervals'),
#     )
#     def update_charts_callback(pie_chart_button_n_clicks_timestamp, bar_chart_button_n_clicks_timestamp, store_first_column, store_second_column, start_date, end_date, select_chart_interval_n_intervals):
#         return update_charts(pie_chart_button_n_clicks_timestamp=pie_chart_button_n_clicks_timestamp, bar_chart_button_n_clicks_timestamp=bar_chart_button_n_clicks_timestamp, store_first_column=store_first_column, store_second_column=store_second_column, start_date=start_date, end_date=end_date, select_chart_interval_n_intervals=select_chart_interval_n_intervals)


# # @app.callback(
# #         Output(
# #             component_id=COMPONENTS_IDS["charts"], component_property='children'),
# #         Input(component_id=COMPONENTS_IDS['pie_chart_button'],
# #               component_property='n_clicks_timestamp'),
# #         Input(component_id=COMPONENTS_IDS['bar_chart_button'],
# #               component_property='n_clicks_timestamp'),
# #         Input(
# #             component_id=STORE_IDS["first_column"], component_property='data'),
# #         Input(
# #             component_id=STORE_IDS["second_column"], component_property='data'),
# #         Input(
# #             component_id=COMPONENTS_IDS["date_picker_range"], component_property='start_date'),
# #         Input(
# #             component_id=COMPONENTS_IDS["date_picker_range"], component_property='end_date'),
# #         Input(
# #             component_id=STORE_IDS["status"], component_property='data'),
# #     )
# #     def update_charts_callback(pie_chart_button_n_clicks_timestamp, bar_chart_button_n_clicks_timestamp, store_first_column, store_second_column, start_date, end_date, status):
# #         return update_charts(pie_chart_button_n_clicks_timestamp=pie_chart_button_n_clicks_timestamp, bar_chart_button_n_clicks_timestamp=bar_chart_button_n_clicks_timestamp, store_first_column=store_first_column, store_second_column=store_second_column, start_date=start_date, end_date=end_date)

#     #  @app.callback(
#     #     Output(
#     #         component_id=COMPONENTS_IDS["table_section"], component_property='style'),
#     #     Input(
#     #         component_id=COMPONENTS_IDS["show_table_button"], component_property='n_clicks_timestamp'),
#     #     Input(
#     #         component_id=COMPONENTS_IDS["show_charts_button"], component_property='n_clicks_timestamp'),
#     # )
#     # def show_table_section_callback(show_table_button_n_clicks_timestamp, show_charts_button_n_clicks_timestamp):
#     #     return show_section(show_button_n_clicks_timestamp=show_table_button_n_clicks_timestamp, hide_button_n_clicks_timestamp=show_charts_button_n_clicks_timestamp)

#     # @app.callback(
#     #     Output(
#     #         component_id=COMPONENTS_IDS["show_table_button"], component_property='disabled'),
#     #     Input(
#     #         component_id=COMPONENTS_IDS["select_table_interval"], component_property='disabled'),
#     # )
#     # def disabled_show_table_button_callback(select_table_interval_disabled):
#     #     return not select_table_interval_disabled

#     # @app.callback(
#     #     Output(
#     #         component_id=COMPONENTS_IDS["table_section"], component_property='children'),
#     #     Output(
#     #         component_id=COMPONENTS_IDS["select_table_interval"], component_property='disabled'),
#     #     Input(
#     #         component_id=COMPONENTS_IDS["table_section"], component_property='style'),
#     #     Input(
#     #         component_id=COMPONENTS_IDS["show_table_button"], component_property='n_clicks'),
#     #     Input(
#     #         component_id=COMPONENTS_IDS["select_table_interval"], component_property='n_intervals'),
#     #     State(
#     #         component_id=COMPONENTS_IDS["table_section"], component_property='children'),
#     # )
#     # def update_table_section_callback(table_section_style, show_table_button_n_clicks, select_table_interval_n_intervals, table_section):
#     #     return update_table_section(table_section_style=table_section_style, show_table_button_n_clicks=show_table_button_n_clicks, select_table_interval_n_intervals=select_table_interval_n_intervals, table_section=table_section)

#     return app

# def restart_app_iterator():
#     """Calls drop_database and close_connection with default values.

#     Yields:
#         success (str): Success message.
#         loading (str): Loading message.
#         error (str): Error message.
#     """
#     try:
#         yield '', lang('drop_database_start'), ''
#         success, error = drop_database()
#         yield success, '', error

#         yield '', lang('close_connection_start'), ''
#         success, error = close_connection()
#         yield success, '', error
#     except Exception as err:
#         yield '', '', lang("restart_app_error").format(err)


# restart_app = restart_app_iterator()
