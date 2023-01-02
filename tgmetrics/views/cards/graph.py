import dash_bootstrap_components as dbc
from dash import dcc


class GraphCardView:
    def __init__(self, graph_id: str = "graph") -> None:
        self.graph_id = graph_id

    @property
    def content(self) -> dbc.Card:
        return dbc.Card(
            dcc.Graph(id=self.graph_id, figure={}),
            body=True
        )
