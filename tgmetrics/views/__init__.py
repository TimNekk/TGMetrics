from dash import Dash

from .layout import LayoutView, cards, header


def register(app: Dash) -> LayoutView:
    header_view = header.HeaderView()
    settings_card_view = cards.SettingsCardView()
    graph_card_view = cards.GraphCardView()

    layout_view = LayoutView(header_view, settings_card_view, graph_card_view)
    app.layout = layout_view.content

    return layout_view

