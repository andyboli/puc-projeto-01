from dash import html, dcc
import dash_bootstrap_components as dbc

from controller.reader import lang


def SPINNER(id: str):
    return html.Div(dbc.Spinner(size="sm"), id=id, className="default-hide-section")


def BUTTON(children: any, id: str, color: str = "primary"):
    return dbc.Button(
        children=children,
        class_name='default-section default-row-section default-border',
        color=color,
        id=id,
    )


def INTERVAL(id: str, max_intervals: int):
    return dcc.Interval(
        disabled=True,
        id=id,
        interval=2*1000,
        n_intervals=0,
        max_intervals=max_intervals
    )


def BAGDE(children: any = "", color: str = "white", text_color: str = "success"):
    return dbc.Badge(
        children=children,
        color=color,
        text_color=text_color
    )


def STORE(id: str):
    return dcc.Store(id=id)


def COLUMN_SECTION(children: any = "", id="", hide=False):
    if hide:
        return html.Div(children, className='default-section default-column-section default-hide-section', id=id)
    return html.Div(children, className='default-section default-column-section', id=id)


def ROW_SECTION(children: any = "", id="", hide=False):
    if hide:
        return html.Div(children, className='default-section default-row-section default-hide-section', id=id)
    return html.Div(children, className='default-section default-row-section', id=id)


def MAIN_SECTION(children: any = ""):
    return html.Div(children, className='main-section default-column-section')


def MAIN_TITLE():
    return html.H1(lang('main_title'), className='default-typography main-title')


def TEXT(key: str, id: str = ''):
    return html.P(lang(key), className='default-typography', id=id)


def BOLD_TEXT(key: str):
    return html.P(lang(key), className='default-bold-typography')


def LINK(key: str, href: str):
    return html.A(lang(key), href=href, className='default-typography', target='_blank')


def CARD(children):
    return html.Div(children, className='default-section default-white-section default-border')


def DROPDOWN_ITEM(option: tuple, id):
    key, value = option
    return dbc.DropdownMenuItem(value, id=key + '-' + id)


def DROPDOWN(options: dict = {}, id: str = ''):
    return dbc.DropdownMenu([*map(lambda option: DROPDOWN_ITEM(option=option, id=id), options.items())], id=id, label=lang("dropdown_label"), class_name='default-border',)


def BAR_GRAPH(id: str = ''):
    return dcc.Graph(
        figure={
            'data': [
                {'x': [3, 4, 5], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
                {'x': [1, 2, 3], 'y': [2, 4, 5],
                 'type': 'bar', 'name': u'Montréal'},
            ],
            'layout': {
                'title': 'Dash Data Visualization'
            }
        },
        id=id,
    )
