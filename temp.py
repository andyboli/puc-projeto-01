import pandas as pd


# rua = pd.read_csv(r'C:\Users\gusta\OneDrive\Documentos\Curso - TBD\1º Semestre\Projeto\data_set_poprua_cadunico-07-2022.csv',
#                   encoding='cp860', delimiter=';', usecols=[0, 1, 2, 3, 4, 5, 7, 8, 9, 10, 11, 12])
# rua['Faixa_etaria'] = rua.apply(faixa_etaria, axis=1)
# print(rua)

# def map_homeless_data_range(mapped_data: list):
#     """receive all mapped csv data from assets/csv/homeless
#     headers: a list of homeless headers
#     header: a set with distinct values from a homeless header

#     return  {headers: list, [header]: set}
#     """
#
#     month_years: set = set()
#     ages: set = set()
#     genders: set = set()
#     birthdays: set = set()
#     schoolings: set = set()
#     ethinicities: set = set()
#     regions: set = set()
#     periods: set = set()
#     social_welfares: set = set()
#     for data in mapped_data:
#         month_years.add(data[0])
#         ages.add(data[1])
#         genders.add(data[2])
#         birthdays.add(data[3])
#         schoolings.add(data[4])
#         ethinicities.add(data[5])
#         regions.add(data[6])
#         periods.add(data[7])
#         social_welfares.add(data[8])
#     return {
#         "headers": headers,
#         "month_years": month_years,
#         "ages": ages,
#         "genders": genders,
#         "birthdays": birthdays,
#         "schoolings": schoolings,
#         "ethinicities": ethinicities,
#         "regions": regions,
#         "periods": periods,
#         "social_welfares": social_welfares,
#     }


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


# GRAPH_SECTION = [BAR_GRAPH, PIE_GRAPH]


# table_query = get_query(first_column, second_column,
#                             max_year, min_year, min_month, max_month)


# def select_data(first_column: str = '', second_column: str = '', first_column_value: str = '', max_year: str = '', min_year: str = '', min_month: str = '', max_month: str = ''):
#     """Calls select_table with default values.

#     Args:
#         first_column (str,): First column to group data.
#         second_column (str,): Second column to group data.
#         first_column_value (str): First column value to filter data.
#         max_year (str): Max year to filter data.
#         min_year (str): Min year to filter data.
#         min_month (str): Min month to filter data.
#         max_month (str): Max month to filter data.

#     Yields:
#         data (list): Data filtered from table
#         success (str): Success message.
#         loading (str): Loading message.
#         error (str): Error message.
#     """
#     # yield None, '', lang('select_table_start'), ''
#     table_query = get_query(first_column=first_column, second_column=second_column, first_column_value=first_column_value, max_year=max_year,
#                             min_year=min_year, min_month=min_month, max_month=max_month)
#     data, success, error = select_table(table_query=table_query)
#     # print("success", success)
#     # print("error", error)
#     # print("data", data)
#     return data
#     # data, success, error = select_table(table_query=table_query)
#     # yield data, success, '', error


# # select_data = select_data_iterator()

# max_select_data_iterations = 2


# def update_dimension_dropdown_label(selected_dimension_label, other_dimension_label):
#     sameLabel = selected_dimension_label == other_dimension_label
#     is_selected = selected_dimension_label != lang("component_dropdown_label")
#     if sameLabel and is_selected:
#         return lang("component_dropdown_label")
#     return other_dimension_label
