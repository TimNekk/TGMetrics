from tgmetrics.repositories import UserRepository
from tgmetrics.services.graphs.category import GraphCategory
from tgmetrics.services.graphs import crud
from tgmetrics.services.graphs.subcategory import GraphSubcategory


class GraphManager:
    def __init__(self, user_repository: UserRepository):
        self._user_repository = user_repository

        self.categories = [
            GraphCategory("Users", user_repository, [
                GraphSubcategory("Total", crud.get_users_total),
                # GraphSubcategory("New"),
                # GraphSubcategory("Activity"),
                # GraphSubcategory("Referral")
            ]),
            # GraphCategory("Messages and callbacks", None, [
            #     GraphSubcategory("Total"),
            #     GraphSubcategory("Commands")
            # ]),
            # GraphCategory("Revenue", None, [
            #     GraphSubcategory("Total"),
            #     GraphSubcategory("New"),
            #     GraphSubcategory("Referral")
            # ])
        ]

    @property
    def categories_names(self) -> list[str]:
        return [category.name for category in self.categories]

    def get_category(self, category_name: str) -> GraphCategory | None:
        for category in self.categories:
            if category.name == category_name:
                return category
        return None
