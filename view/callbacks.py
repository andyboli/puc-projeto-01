from dash import Dash
from dash.dependencies import Input, Output, State

from controller.orchestrator import start_app, start_app_iterations, map_date, select_app_iterator
from controller.reader import lang
from view.constants import COMPONENTS_IDS, STORE_STATE
from view.components import BAGDE
from database.constants import TABLES
from database.connection import select_table


def create_callbacks(app: Dash):
    hide_component = {'display': 'none'}
    show_component = {'display': 'flex'}
    dropdown_options = TABLES['homeless']['headers_label']
    ranges = TABLES['homeless']['headers_ranges']

    @app.callback(
        Output(
            component_id=COMPONENTS_IDS["app_interval"], component_property='disabled'),
        Output(
            component_id=COMPONENTS_IDS['start_app_button_spinner'], component_property='style'),
        Input(
            component_id=COMPONENTS_IDS["start_app_button"], component_property='n_clicks'),
        Input(
            component_id=STORE_STATE["done"], component_property='data'),
    )
    def update_interval(start_app_button_n_clicks, done):
        if not start_app_button_n_clicks or done:
            return True, hide_component
        return False, show_component

    @app.callback(
        Output(
            component_id=STORE_STATE["success"], component_property='data'),
        Output(
            component_id=STORE_STATE["loading"], component_property='data'),
        Output(
            component_id=STORE_STATE["error"], component_property='data'),
        Output(
            component_id=STORE_STATE["done"], component_property='data'),
        Input(
            component_id=COMPONENTS_IDS["app_interval"], component_property='n_intervals'),
    )
    def update_store(n_intervals):
        success = ''
        loading = ''
        error = ''
        done = False
        if n_intervals:
            try:
                success, loading, error = next(start_app)
                if n_intervals == start_app_iterations:
                    done = True
            except StopIteration:
                done = True
        return success, loading, error, done

    @app.callback(
        Output(
            component_id=COMPONENTS_IDS['status_section'], component_property='children'),
        Input(
            component_id=STORE_STATE["success"], component_property='data'),
        State(
            component_id=COMPONENTS_IDS['status_section'], component_property='children'),
    )
    def update_status_section(success, current_status_section_children):
        if success and not current_status_section_children:
            return [BAGDE(success)]
        if success and current_status_section_children:
            return [*current_status_section_children, BAGDE(success)]
        return current_status_section_children

    @app.callback(
        Output(
            component_id=COMPONENTS_IDS["start_app_button_text"], component_property='children'),
        Output(
            component_id=COMPONENTS_IDS["start_app_button"], component_property='color'),
        Output(
            component_id=COMPONENTS_IDS["start_app_button"], component_property='disabled'),
        Input(
            component_id=STORE_STATE["success"], component_property='data'),
        Input(
            component_id=STORE_STATE["loading"], component_property='data'),
        Input(
            component_id=STORE_STATE["error"], component_property='data'),
        Input(
            component_id=STORE_STATE["done"], component_property='data'),
    )
    def update_start_app_button(success, loading, error, done):
        start_app_button_text = lang("start_app")
        start_app_button_color = 'primary'
        start_app_button_disabled = False
        if loading:
            start_app_button_text = loading
        if success:
            start_app_button_text = success
        if error:
            start_app_button_text = error
            start_app_button_color = 'danger'
        if done:
            start_app_button_disabled = True
        return start_app_button_text, start_app_button_color, start_app_button_disabled

    @app.callback(
        Output(
            component_id=COMPONENTS_IDS["app_buttons"], component_property='style'),
        Input(
            component_id=STORE_STATE["done"], component_property='data'),
    )
    def update_app_buttons(done):
        # monitoring
        if not done:
            return show_component
        return hide_component

    @app.callback(
        Output(
            component_id=COMPONENTS_IDS["control_section"], component_property='style'),
        Input(
            component_id=COMPONENTS_IDS["charts_button"], component_property='n_clicks_timestamp'),
        Input(
            component_id=COMPONENTS_IDS["hide_charts_button"], component_property='n_clicks_timestamp'),
    )
    def update_control_section(charts_button_n_clicks_timestamp, hide_charts_button_n_clicks_timestamp):
        if charts_button_n_clicks_timestamp is None and hide_charts_button_n_clicks_timestamp is None:
            return show_component
        if charts_button_n_clicks_timestamp is not None and hide_charts_button_n_clicks_timestamp is None:
            return hide_component
        if charts_button_n_clicks_timestamp is None and hide_charts_button_n_clicks_timestamp is not None:
            return show_component
        if charts_button_n_clicks_timestamp > hide_charts_button_n_clicks_timestamp:
            return hide_component
        if charts_button_n_clicks_timestamp < hide_charts_button_n_clicks_timestamp:
            return show_component
        return show_component

    @app.callback(
        Output(
            component_id=COMPONENTS_IDS["charts_section"], component_property='style'),
        Input(
            component_id=COMPONENTS_IDS["charts_button"], component_property='n_clicks_timestamp'),
        Input(
            component_id=COMPONENTS_IDS["hide_charts_button"], component_property='n_clicks_timestamp'),
    )
    def update_charts_section(charts_button_n_clicks_timestamp, hide_charts_button_n_clicks_timestamp):
        if charts_button_n_clicks_timestamp is None and hide_charts_button_n_clicks_timestamp is None:
            return hide_component
        if charts_button_n_clicks_timestamp is not None and hide_charts_button_n_clicks_timestamp is None:
            return show_component
        if charts_button_n_clicks_timestamp is None and hide_charts_button_n_clicks_timestamp is not None:
            return hide_component
        if charts_button_n_clicks_timestamp > hide_charts_button_n_clicks_timestamp:
            return show_component
        if charts_button_n_clicks_timestamp < hide_charts_button_n_clicks_timestamp:
            return hide_component
        return hide_component

    @app.callback(
        Output(
            component_id=COMPONENTS_IDS["pie_chart_dropdowns"], component_property='style'),
        Input(component_id=COMPONENTS_IDS['pie_chart_button'],
              component_property='n_clicks_timestamp'),
        Input(component_id=COMPONENTS_IDS['bar_chart_button'],
              component_property='n_clicks_timestamp'),
    )
    def update_pie_chart_dropdowns(pie_chart_dropdown_click, bar_chart_dropdown_click):
        if pie_chart_dropdown_click is None and bar_chart_dropdown_click is None:
            return hide_component
        if pie_chart_dropdown_click is not None and bar_chart_dropdown_click is None:
            return show_component
        if pie_chart_dropdown_click is None and bar_chart_dropdown_click is not None:
            return hide_component
        if pie_chart_dropdown_click > bar_chart_dropdown_click:
            return show_component
        if pie_chart_dropdown_click < bar_chart_dropdown_click:
            return hide_component
        return hide_component

    @app.callback(
        Output(
            component_id=COMPONENTS_IDS["bar_chart_dropdowns"], component_property='style'),
        Input(component_id=COMPONENTS_IDS['pie_chart_button'],
              component_property='n_clicks_timestamp'),
        Input(component_id=COMPONENTS_IDS['bar_chart_button'],
              component_property='n_clicks_timestamp'),
    )
    def update_bar_chart_dropdowns(pie_chart_dropdown_click, bar_chart_dropdown_click):
        if bar_chart_dropdown_click is None and pie_chart_dropdown_click is None:
            return hide_component
        if bar_chart_dropdown_click is not None and pie_chart_dropdown_click is None:
            return show_component
        if bar_chart_dropdown_click is None and pie_chart_dropdown_click is not None:
            return hide_component
        if bar_chart_dropdown_click > pie_chart_dropdown_click:
            return show_component
        if bar_chart_dropdown_click < pie_chart_dropdown_click:
            return hide_component
        return hide_component

    @app.callback(
        Output(
            component_id=COMPONENTS_IDS["bar_chart"], component_property='style'),
        Input(component_id=COMPONENTS_IDS['pie_chart_button'],
              component_property='n_clicks_timestamp'),
        Input(component_id=COMPONENTS_IDS['bar_chart_button'],
              component_property='n_clicks_timestamp'),
    )
    def update_bar_chart(pie_chart_dropdown_click, bar_chart_dropdown_click):
        if bar_chart_dropdown_click is None and pie_chart_dropdown_click is None:
            return hide_component
        if bar_chart_dropdown_click is not None and pie_chart_dropdown_click is None:
            return show_component
        if bar_chart_dropdown_click is None and pie_chart_dropdown_click is not None:
            return hide_component
        if bar_chart_dropdown_click > pie_chart_dropdown_click:
            return show_component
        if bar_chart_dropdown_click < pie_chart_dropdown_click:
            return hide_component
        return hide_component

    @app.callback(
        Output(
            component_id=STORE_STATE["first_dimension"], component_property='data'),
        Output(
            component_id=STORE_STATE["first_dimension_label"], component_property='data'),
        Input(component_id='age' '-' + COMPONENTS_IDS['bar_chart_first_dimension_dropdown'],
              component_property="n_clicks_timestamp"),
        Input(component_id="gender" + '-' + COMPONENTS_IDS['bar_chart_first_dimension_dropdown'],
              component_property="n_clicks_timestamp"),
        Input(component_id="schooling" + '-' + COMPONENTS_IDS['bar_chart_first_dimension_dropdown'],
              component_property="n_clicks_timestamp"),
        Input(component_id="ethnicity" + '-' + COMPONENTS_IDS['bar_chart_first_dimension_dropdown'],
              component_property="n_clicks_timestamp"),
        Input(component_id="region" + '-' + COMPONENTS_IDS['bar_chart_first_dimension_dropdown'],
              component_property="n_clicks_timestamp"),
        Input(component_id="social_welfare" + '-' + COMPONENTS_IDS['bar_chart_first_dimension_dropdown'],
              component_property="n_clicks_timestamp"),
    )
    def update_first_dimension(age_timestamp, gender_timestamp, schooling_timestamp, ethnicity_timestamp, region_timestamp, social_welfare_timestamp):
        selected_field = list(filter(lambda dimension: dimension is not None, [age_timestamp, gender_timestamp, schooling_timestamp, ethnicity_timestamp,
                                                                               region_timestamp, social_welfare_timestamp]))
        current_timestamp = 0

        if len(selected_field):
            current_timestamp = max(selected_field)

        if current_timestamp == age_timestamp:
            return "age", dropdown_options["age"]
        if current_timestamp == gender_timestamp:
            return "gender", dropdown_options["gender"],
        if current_timestamp == schooling_timestamp:
            return "schooling", dropdown_options["schooling"],
        if current_timestamp == ethnicity_timestamp:
            return "ethnicity", dropdown_options["ethnicity"],
        if current_timestamp == region_timestamp:
            return "region", dropdown_options["region"],
        if current_timestamp == social_welfare_timestamp:
            return "social_welfare", dropdown_options["social_welfare"]

        # if current_timestamp == period_timestamp:
        #     return "period", dropdown_options["period"], "region"

        return "empty", lang("dropdown_label")

    @ app.callback(
        Output(
            component_id=STORE_STATE["second_dimension"], component_property='data'),
        Output(
            component_id=STORE_STATE["second_dimension_label"], component_property='data'),
        Input(component_id='age' '-' + COMPONENTS_IDS['bar_chart_second_dimension_dropdown'],
              component_property="n_clicks_timestamp"),
        Input(component_id="gender" + '-' + COMPONENTS_IDS['bar_chart_second_dimension_dropdown'],
              component_property="n_clicks_timestamp"),
        Input(component_id="schooling" + '-' + COMPONENTS_IDS['bar_chart_second_dimension_dropdown'],
              component_property="n_clicks_timestamp"),
        Input(component_id="ethnicity" + '-' + COMPONENTS_IDS['bar_chart_second_dimension_dropdown'],
              component_property="n_clicks_timestamp"),
        Input(component_id="region" + '-' + COMPONENTS_IDS['bar_chart_second_dimension_dropdown'],
              component_property="n_clicks_timestamp"),
        Input(component_id="social_welfare" + '-' + COMPONENTS_IDS['bar_chart_second_dimension_dropdown'],
              component_property="n_clicks_timestamp"),
    )
    def update_second_dimension(age_timestamp, gender_timestamp, schooling_timestamp, ethnicity_timestamp, region_timestamp, social_welfare_timestamp):
        selectec_field = list(filter(lambda dimension: dimension is not None, [age_timestamp, gender_timestamp, schooling_timestamp, ethnicity_timestamp,
                                                                               region_timestamp, social_welfare_timestamp]))
        current_timestamp = 0

        if len(selectec_field):
            current_timestamp = max(selectec_field)

        if current_timestamp == age_timestamp:
            return "age", dropdown_options["age"]
        if current_timestamp == gender_timestamp:
            return "gender", dropdown_options["gender"],
        if current_timestamp == schooling_timestamp:
            return "schooling", dropdown_options["schooling"],
        if current_timestamp == ethnicity_timestamp:
            return "ethnicity", dropdown_options["ethnicity"],
        if current_timestamp == region_timestamp:
            return "region", dropdown_options["region"],
        if current_timestamp == social_welfare_timestamp:
            return "social_welfare", dropdown_options["social_welfare"]

        return "empty", lang("dropdown_label")

    @ app.callback(
        Output(
            component_id=COMPONENTS_IDS["bar_chart_first_dimension_dropdown"], component_property='label'),
        Input(
            component_id=STORE_STATE["first_dimension_label"], component_property='data'),
        Input(
            component_id=STORE_STATE["second_dimension_label"], component_property='data'),
        # State(
        #     component_id=COMPONENTS_IDS["bar_chart_first_dimension_dropdown"], component_property='label'),
    )
    def update_bar_chart_first_dimension_dropdown_label(first_dimension_label, second_dimension_label):
        sameLabel = first_dimension_label == second_dimension_label
        selected_second_dimension = second_dimension_label != lang(
            "dropdown_label")
        # print('sameLabel', sameLabel)
        # print('selected_second_dimension', selected_second_dimension)
# or sameLabel and first_dimension_label == lang("dropdown_label"):
        if sameLabel and selected_second_dimension:
            return lang("dropdown_label")

        return first_dimension_label

    @ app.callback(
        Output(
            component_id=COMPONENTS_IDS["bar_chart_second_dimension_dropdown"], component_property='label'),
        Input(
            component_id=STORE_STATE["first_dimension_label"], component_property='data'),
        Input(
            component_id=STORE_STATE["second_dimension_label"], component_property='data'),
        # State(
        #     component_id=COMPONENTS_IDS["bar_chart_second_dimension_dropdown"], component_property='label'),
    )
    def update_bar_chart_second_dimension_dropdown_label(first_dimension_label, second_dimension_label):
        sameLabel = first_dimension_label == second_dimension_label
        selected_first_dimension = first_dimension_label != lang(
            "dropdown_label")
        if sameLabel and selected_first_dimension:
            return lang("dropdown_label")
        return second_dimension_label

    def hide_option(child, value):
        if child['props']['children'] == value:
            child['props']['class_name'] = 'default-hide-section'
        else:
            child['props']['class_name'] = 'default-show-section'
        return child

    @app.callback(
        Output(
            component_id=COMPONENTS_IDS["bar_chart_second_dimension_dropdown"], component_property='children'),
        Input(
            component_id=STORE_STATE["first_dimension_label"], component_property='data'),
        State(
            component_id=COMPONENTS_IDS["bar_chart_second_dimension_dropdown"], component_property='children'),
    )
    def update_bar_chart_second_dimension_dropdown(first_dimension_label, second_dimension_children):
        return list(map(lambda child: (hide_option(child=child, value=first_dimension_label)), second_dimension_children))

    @app.callback(
        Output(
            component_id=COMPONENTS_IDS["bar_chart_first_dimension_dropdown"], component_property='children'),
        Input(
            component_id=STORE_STATE["second_dimension_label"], component_property='data'),
        State(
            component_id=COMPONENTS_IDS["bar_chart_first_dimension_dropdown"], component_property='children'),
    )
    def update_bar_chart_first_dimension_dropdown(second_dimension_label,  first_dimension_children):
        return list(map(lambda child: (hide_option(child=child, value=second_dimension_label)), first_dimension_children))

    def map_data(data):
        dimensions = {}
        mapped_data = []
        for amout, first_dimension, second_dimension in data:
            if first_dimension not in dimensions.keys():
                dimensions[first_dimension] = {}
            if second_dimension not in dimensions[first_dimension].keys():
                dimensions[first_dimension][second_dimension] = amout
            else:
                dimensions[first_dimension][second_dimension] = [
                    *dimensions[first_dimension][second_dimension], amout]
        for first_dimension in dimensions.keys():
            second_dimensions = dimensions[first_dimension].keys()
            amouts = dimensions[first_dimension].values()
            mapped_data.append(
                {'type': 'bar', 'name': first_dimension, 'x': list(second_dimensions), 'y': list(amouts)})
        return mapped_data

    @ app.callback(
        Output(
            component_id=COMPONENTS_IDS["bar_chart"], component_property='figure'),
        Input(
            component_id=STORE_STATE["first_dimension"], component_property='data'),
        Input(
            component_id=STORE_STATE["second_dimension"], component_property='data'),
        Input(
            component_id=COMPONENTS_IDS["date_range"], component_property='start_date'),
        Input(
            component_id=COMPONENTS_IDS["date_range"], component_property='end_date'),
        # State(
        #     component_id=COMPONENTS_IDS["bar_chart_first_dimension_dropdown"], component_property='children'),
    )
    def update_bar_chart(first_dimension, second_dimension, start_date, end_date):
        data = []

        filledFilters = first_dimension != 'empty' and second_dimension != 'empty' and start_date and end_date

        if filledFilters:
            min_year, min_month = map_date(start_date)
            max_year, max_month = map_date(end_date)
            data_raw = select_app_iterator(column_1=first_dimension, column_2=second_dimension,
                                           max_month=max_month, max_year=max_year, min_year=min_year, min_month=min_month)
            print('data_raw', data_raw)
            data = map_data(data_raw)

        return {"data": data}

    return app
