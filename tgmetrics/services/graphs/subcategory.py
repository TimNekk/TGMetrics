from typing import Callable

from plotly.graph_objs import Figure


class GraphSubcategory:
    def __init__(self, name: str, graph_function: Callable):
        self.name = name
        self.graph_function = graph_function
        self.repository = None

    def set_repository(self, repository):
        self.repository = repository

    def get_graph(self) -> Figure:
        return self.graph_function(self.repository)
