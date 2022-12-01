from dash import Dash
from dash.dependencies import Input, Output, State

from controller.orchestrator import start_app, start_app_iterations
from controller.reader import lang
from view.constants import COMPONENTS_IDS, STORE_STATE
from view.components import BAGDE


def create_callbacks(app: Dash):
    hide_component = {'display': 'none'}
    show_component = {'display': 'flex'}

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
        if done:
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
        Output(
            component_id=COMPONENTS_IDS["charts_buttons"], component_property='style'),
        Input(
            component_id=COMPONENTS_IDS["charts_button"], component_property='n_clicks_timestamp'),
        Input(
            component_id=COMPONENTS_IDS["hide_charts_button"], component_property='n_clicks_timestamp'),
    )
    def update_charts_section(charts_button_n_clicks_timestamp, hide_charts_button_n_clicks_timestamp):
        if charts_button_n_clicks_timestamp is None and hide_charts_button_n_clicks_timestamp is None:
            return hide_component, hide_component
        if charts_button_n_clicks_timestamp is not None and hide_charts_button_n_clicks_timestamp is None:
            return show_component, show_component
        if charts_button_n_clicks_timestamp is None and hide_charts_button_n_clicks_timestamp is not None:
            return hide_component, hide_component
        if charts_button_n_clicks_timestamp > hide_charts_button_n_clicks_timestamp:
            return show_component, show_component
        if charts_button_n_clicks_timestamp < hide_charts_button_n_clicks_timestamp:
            return hide_component, hide_component
        return hide_component, hide_component

    @app.callback(
        Output(
            component_id=COMPONENTS_IDS["pie_chart_dropdowns"], component_property='style'),
        Input(component_id='pie-chart-button',
              component_property='n_clicks_timestamp'),
        Input(component_id='bar-chart-button',
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
        Input(component_id='pie-chart-button',
              component_property='n_clicks_timestamp'),
        Input(component_id='bar-chart-button',
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

        # @app.callback(
        #     Output(
        #         component_id=STORE_STATE["homeless_data_range"], component_property='data'),
        #     Output(
        #         component_id=STORE_STATE["message"], component_property='data'),
        #     Output(
        #         component_id=STORE_STATE["error"], component_property='data'),
        #     Output(
        #         component_id=STORE_STATE["start_app_done"], component_property='data'),
        #     Output(
        #         component_id=COMPONENTS_IDS["app_interval"], component_property='disabled'),
        #     Input(
        #         component_id=COMPONENTS_IDS["app_interval"], component_property='n_intervals'),
        #     Input(
        #         component_id=COMPONENTS_IDS["end_app_button"], component_property='n_clicks'),
        #     Input(
        #         component_id=COMPONENTS_IDS["start_app_button"], component_property='n_clicks'),
        #     State(
        #         component_id=COMPONENTS_IDS["end_app_button"], component_property='disabled'),
        #     State(
        #         component_id=COMPONENTS_IDS["start_app_button"], component_property='disabled'),
        #     State(
        #         component_id=COMPONENTS_IDS["app_interval"], component_property='disabled'),
        #     State(
        #         component_id=STORE_STATE["homeless_data_range"], component_property='data'),
        #     State(
        #         component_id=STORE_STATE["message"], component_property='data'),
        #     State(
        #         component_id=STORE_STATE["error"], component_property='data'),
        #     State(
        #         component_id=STORE_STATE["start_app_done"], component_property='data'),
        # )
        # def update_store_and_interval(
        #     n_intervals,
        #     end_app_button_n_clicks,
        #     start_app_button_n_clicks,
        #     end_app_button_disabled,
        #     start_app_button_disabled,
        #     current_app_interval_disabled,
        #     current_homeless_data_range,
        #     current_message,
        #     current_error,
        #     current_start_app_done
        # ):
        #     data_range = current_homeless_data_range
        #     message = current_message
        #     error = current_error
        #     start_app_done = current_start_app_done
        #     app_interval_disabled = current_app_interval_disabled

        #     if start_app_button_n_clicks and not start_app_button_disabled:
        #         app_interval_disabled = False

        #     if end_app_button_n_clicks and not end_app_button_disabled:
        #         while True:
        #             try:
        #                 message, error = next(end_app)
        #                 if message:
        #                     print(message)
        #                 if error:
        #                     print(error)
        #             except StopIteration:
        #                 break
        #         data_range = ''
        #         message = ''
        #         error = ''
        #         start_app_done = False
        #         app_interval_disabled = True

        #     if n_intervals and not app_interval_disabled:

        #         try:
        #             homeless_data_range, start_app_message, start_app_error = next(
        #                 start_app)

        #             if start_app_message:
        #                 message = start_app_message
        #             if start_app_error:
        #                 error = start_app_error
        #             if homeless_data_range:
        #                 data_range = str(homeless_data_range)
        #         except StopIteration:
        #             start_app_done = True
        #             app_interval_disabled = True
        #         except ValueError:
        #             start_app_done = False
        #             app_interval_disabled = True
        #     print(message, current_message, n_intervals)
        #     return data_range, message, error, start_app_done, app_interval_disabled

        # @app.callback(
        #     Output(
        #         component_id=COMPONENTS_IDS["start_app_button_text"], component_property='children'),
        #     Output(
        #         component_id=COMPONENTS_IDS["start_app_button"], component_property='color'),
        #     Input(
        #         component_id=STORE_STATE["message"], component_property='data'),
        #     Input(
        #         component_id=STORE_STATE["error"], component_property='data'),
        # )
        # def update_start_app_button(message, error):
        #     print('button', message)
        #     if message:
        #         return message, 'primary'
        #     if error:
        #         return error, 'danger'
        #     return lang('start_app'), 'primary'

        # @app.callback(
        #     Output(
        #         component_id=COMPONENTS_IDS["start_app_button"], component_property='disabled'),
        #     Input(
        #         component_id=STORE_STATE["start_app_done"], component_property='data'),
        # )
        # def update_start_app_button_disabled(start_app_done):
        #     return start_app_done

        # @app.callback(

        #     Input(
        #         component_id=COMPONENTS_IDS["start_app_button"], component_property='disabled'),
        # )
        # def update_buttons_disabled(start_app_button_disabled):
        #     return not start_app_button_disabled, not start_app_button_disabled

        # @app.callback(
        #     Output(
        #         component_id=COMPONENTS_IDS["start_app_button"], component_property='disabled'),
        #     Input(
        #         component_id=COMPONENTS_IDS["start_app_button"], component_property='n_clicks'),
        #     State(
        #         component_id=COMPONENTS_IDS["start_app_button"], component_property='disabled'),

        # )
        # def update_start_button_by_click(start_app_button_n_clicks, start_app_button_disabled):
        #     if start_app_button_disabled:
        #         return True
        #     if start_app_button_n_clicks is None:
        #         return False

        # @app.callback(
        #     Output(
        #         component_id=COMPONENTS_IDS["start_app_button"], component_property='children'),
        #     Output(
        #         component_id=COMPONENTS_IDS["start_app_button"], component_property='disabled'),
        #     Input(
        #         component_id=COMPONENTS_IDS["app_interval"], component_property='n_intervals'),
        # )
        # def update_start_button_by_interval(n_intervals):
        #     if n_intervals:
        #         try:
        #             homeless_data_range, connection, message, error = next(
        #                 start_app)
        # #                 bar_chart_button_disabled = True
        # #                 pie_chart_button_disabled = True
        # #                 if message is not None:
        # #                     button_text = message
        # #                     interval_disabled = False
        # #                     spinner_style = {'display': 'block'}
        # #                 if error is not None:
        # #                     button_text = error
        # #                     button_color = 'danger'
        #         except StopIteration:
        #             #                 button_text = lang('show_database')
        #         finally:
        #             #                 return button_text, spinner_style, interval_disabled, button_color, bar_chart_button_disabled, pie_chart_button_disabled
        #         return
        #     return

    return app

    #     @app.callback(
    #         Output(component_id='main-button-text', component_property='children'),
    #         Output(component_id='primary-button-spinner',
    #                component_property='style'),
    #         Output(component_id='interval-component',
    #                component_property='disabled'),
    #         Output(component_id='main-button', component_property='color'),
    #         Output(component_id='bar-chart-button', component_property='disabled'),
    #         Output(component_id='pie-chart-button', component_property='disabled'),
    #         Input(component_id='interval-component',
    #               component_property='n_intervals'),
    #         Input(component_id='main-button', component_property='n_clicks'),
    #         State(component_id='main-button-text', component_property='children')
    #     )
    #     def update_main_button(n_intervals, n_clicks, current_children):
    #         button_text = lang('show_database')
    #         spinner_style = {'display': 'none'}
    #         interval_disabled = True
    #         button_color = 'success'
    #         bar_chart_button_disabled = False
    #         pie_chart_button_disabled = False

    #         button_not_clicked = n_clicks is None

    #         if button_not_clicked:
    #             button_text = lang('start')
    #             bar_chart_button_disabled = True
    #             pie_chart_button_disabled = True
    #             return button_text, spinner_style, interval_disabled, button_color, bar_chart_button_disabled, pie_chart_button_disabled

    #         finished = current_children == lang('show_database')

    #         if finished:
    #             return current_children, spinner_style, interval_disabled, button_color, bar_chart_button_disabled, pie_chart_button_disabled

    #         button_first_click = n_clicks is not None and n_intervals == 0

    #         if button_first_click:
    #             button_text = lang('loading')
    #             spinner_style = {'display': 'block'}
    #             interval_disabled = False
    #             bar_chart_button_disabled = True
    #             pie_chart_button_disabled = True
    #             return button_text, spinner_style, interval_disabled, button_color, bar_chart_button_disabled, pie_chart_button_disabled

    #         on_intervals = n_intervals != 0

    #         if on_intervals:
    #             try:
    #                 message, error = next(start_app)
    #                 bar_chart_button_disabled = True
    #                 pie_chart_button_disabled = True
    #                 if message is not None:
    #                     button_text = message
    #                     interval_disabled = False
    #                     spinner_style = {'display': 'block'}
    #                 if error is not None:
    #                     button_text = error
    #                     button_color = 'danger'
    #             except StopIteration:
    #                 button_text = lang('show_database')
    #             finally:
    #                 return button_text, spinner_style, interval_disabled, button_color, bar_chart_button_disabled, pie_chart_button_disabled

    #         return button_text, spinner_style, interval_disabled, button_color, bar_chart_button_disabled, pie_chart_button_disabled
    #     return app
