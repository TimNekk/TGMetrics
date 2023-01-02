from tgmetrics.repositories import UserRepository
from tgmetrics.repositories.group_by import GroupBy
from tgmetrics.services.graphs.category import GraphCategory
from tgmetrics.services.graphs import crud
from tgmetrics.services.graphs.subcategory import GraphSubcategory
from tgmetrics.services.graphs.period import GraphPeriod


class GraphManager:
    def __init__(self, user_repository: UserRepository):
        self._user_repository = user_repository

        self.categories = [
            GraphCategory("Users", [
                GraphSubcategory("Total", user_repository, [
                    GraphPeriod("Months", crud.get_users_total, GroupBy.MONTH),
                    GraphPeriod("Days", crud.get_users_total, GroupBy.DAY),
                    GraphPeriod("Hours", crud.get_users_total, GroupBy.HOUR),
                ])
            ])
        ]

    @property
    def categories_names(self) -> list[str]:
        return [category.name for category in self.categories]

    def get_category(self, category_name: str) -> GraphCategory | None:
        for category in self.categories:
            if category.name == category_name:
                return category
        return None
