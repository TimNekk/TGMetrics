from dash import Dash

from .settings import SettingsController
from .graph import GraphController
from .. import repositories
from .. import views


def register(app: Dash,
             graph_repository: repositories.GraphRepository,
             settings_card_view: views.cards.SettingsCardView,
             graph_card_view: views.cards.GraphCardView) -> None:
    SettingsController(graph_repository, settings_card_view).register_callbacks(app)
    GraphController(graph_repository, settings_card_view, graph_card_view).register_callbacks(app)
