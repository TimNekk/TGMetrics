from tgmetrics.services.graphs.subcategory import GraphSubcategory


class GraphCategory:
    def __init__(self, name, repository, subcategories: list[GraphSubcategory]):
        self.name = name
        self.subcategories = subcategories
        self._setup_subcategories(repository)

    def _setup_subcategories(self, repository):
        for subcategory in self.subcategories:
            subcategory.set_repository(repository)

    @property
    def subcategories_names(self) -> list[str]:
        return [subcategory.name for subcategory in self.subcategories]

    def get_subcategory(self, subcategory_name: str) -> GraphSubcategory | None:
        for subcategory in self.subcategories:
            if subcategory.name == subcategory_name:
                return subcategory
        return None
