from typing import Callable

from plotly.graph_objs import Figure


class GraphPeriod:
    def __init__(self, name: str, graph_function: Callable, *args, **kwargs):
        self.name = name
        self.graph_function = graph_function
        self.repository = None
        self.args = args
        self.kwargs = kwargs

    def set_repository(self, repository):
        self.repository = repository

    def get_graph(self) -> Figure:
        return self.graph_function(self.repository, *self.args, **self.kwargs)
