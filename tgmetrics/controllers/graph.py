from dash import Output, Input, Dash

from tgmetrics import repositories, views


class GraphController:
    def __init__(self,
                 graph_repository: repositories.GraphRepository,
                 settings_card_view: views.cards.SettingsCardView,
                 graph_card_view: views.cards.GraphCardView) -> None:
        self._graph_repository = graph_repository
        self._settings_card_view = settings_card_view
        self._graph_card_view = graph_card_view

    def register_callbacks(self, app: Dash) -> None:
        app.callback(
            Output(self._graph_card_view.graph_id, "figure"),
            [Input(self._settings_card_view.category_dropdown_id, "value"),
             Input(self._settings_card_view.subcategory_dropdown_id, "value")]
        )(self.update_graph)

    def update_graph(self, category_value, subcategory_value):
        graph = self._graph_repository.get_graph(category_value, subcategory_value)
        if graph:
            return graph
        return {}
