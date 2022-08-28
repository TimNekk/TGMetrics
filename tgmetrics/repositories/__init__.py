from .user import UserRepository
from .graph import GraphRepository
from ..services.db import models
from ..services.graphs import GraphManager


def register_user_repository() -> UserRepository:
    return UserRepository(models.User)


def register_graph_repository(graph_manager: GraphManager) -> GraphRepository:
    return GraphRepository(graph_manager)
