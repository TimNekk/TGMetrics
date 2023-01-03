from dash import Dash
import dash_bootstrap_components as dbc

from tgmetrics import controllers, repositories, views
from tgmetrics.services.graphs import GraphManager


def main():
    app = Dash(__name__,
               external_stylesheets=[dbc.themes.QUARTZ],
               meta_tags=[{
                   "name": "viewport",
                   "content": "width=device-width, initial-scale=1"
               }],
               title="TGMetrics"
               )

    layout_view = views.register(app)

    user_repository = repositories.register_user_repository()
    graph_manager = GraphManager(user_repository)
    graph_repository = repositories.register_graph_repository(graph_manager)

    controllers.register(app,
                         graph_repository=graph_repository,
                         settings_card_view=layout_view.settings_card_view,
                         graph_card_view=layout_view.graph_card_view)

    app.run_server(debug=True)


if __name__ == '__main__':
    main()
