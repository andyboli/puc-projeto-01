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
        interval=1*1000,
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


def COLUMN_SECTION(children: any = "", id=""):
    return html.Div(children, className='default-section default-column-section default-hide-section', id=id)


def ROW_SECTION(children: any = "", id=""):
    return html.Div(children, className='default-section default-row-section default-hide-section', id=id)


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


def DROPDOWN_ITEM(option: str):
    return dbc.DropdownMenuItem(option)


def DROPDOWN(options: list = [], id: str = ''):
    return dbc.DropdownMenu([*map(DROPDOWN_ITEM, options)], id=id, label=lang("dropdown_label"), class_name='default-border')
