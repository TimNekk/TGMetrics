from plotly.graph_objs import Figure

from tgmetrics.services.graphs.manager import GraphManager


class GraphRepository:
    def __init__(self, graph_manager: GraphManager):
        self._graph_manager = graph_manager

    @property
    def categories(self) -> list[str]:
        return self._graph_manager.categories_names

    def get_subcategories(self, category_name: str) -> list[str]:
        category = self._graph_manager.get_category(category_name)

        if not category:
            return []

        return category.subcategories_names

    def get_graph(self, category_name: str, subcategory_name: str) -> Figure | None:
        category = self._graph_manager.get_category(category_name)

        if not category:
            return None

        subcategory = category.get_subcategory(subcategory_name)

        if not subcategory:
            return None

        return subcategory.get_graph()
