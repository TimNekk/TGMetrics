from dash import Output, Input, Dash

from tgmetrics import repositories, views


class SettingsController:
    def __init__(self,
                 graph_repository: repositories.GraphRepository,
                 settings_card_view: views.cards.SettingsCardView) -> None:
        self._graph_repository = graph_repository
        self._settings_card_view = settings_card_view

    def register_callbacks(self, app: Dash) -> None:
        app.callback(
            Output(self._settings_card_view.category_dropdown_id, "options"),
            Input(self._settings_card_view.category_dropdown_id, "value"),
        )(self.update_category_dropdown_options)

        app.callback(
            Output(self._settings_card_view.subcategory_dropdown_id, "options"),
            Input(self._settings_card_view.category_dropdown_id, "value"),
        )(self.update_subcategory_dropdown_options)

        app.callback(
            Output(self._settings_card_view.period_dropdown_id, "options"),
            Input(self._settings_card_view.category_dropdown_id, "value"),
            Input(self._settings_card_view.subcategory_dropdown_id, "value"),
        )(self.update_period_dropdown_options)

    def update_category_dropdown_options(self, category_name):
        return self._graph_repository.categories

    def update_subcategory_dropdown_options(self, category_name):
        return self._graph_repository.get_subcategories(category_name)

    def update_period_dropdown_options(self, category_name, subcategory_name):
        return self._graph_repository.get_periods(category_name, subcategory_name)
