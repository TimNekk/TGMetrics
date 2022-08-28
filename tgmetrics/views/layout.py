from dash import html
import dash_bootstrap_components as dbc

from tgmetrics.views import header, cards


class LayoutView:
    def __init__(self,
                 header_view: header.HeaderView,
                 settings_card_view: cards.SettingsCardView,
                 graph_card_view: cards.GraphCardView) -> None:
        self.header_view = header_view
        self.settings_card_view = settings_card_view
        self.graph_card_view = graph_card_view

    @property
    def content(self) -> html.Div:
        return html.Div([
            self.header_view.content,
            html.Div(
                style={
                    "margin-top": "20px",
                },
                children=[
                    dbc.Row(
                        justify="center",
                        children=[
                            dbc.Col(self.settings_card_view.content, width=3),
                            dbc.Col(self.graph_card_view.content, width=8),
                        ]
                    )
                ]
            )
        ])
