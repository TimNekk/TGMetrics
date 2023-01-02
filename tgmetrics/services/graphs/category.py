from tgmetrics.services.graphs.subcategory import GraphSubcategory


class GraphCategory:
    def __init__(self, name, subcategories: list[GraphSubcategory]):
        self.name = name
        self.subcategories = subcategories

    @property
    def subcategories_names(self) -> list[str]:
        return [subcategory.name for subcategory in self.subcategories]

    def get_subcategory(self, subcategory_name: str) -> GraphSubcategory | None:
        for subcategory in self.subcategories:
            if subcategory.name == subcategory_name:
                return subcategory
        return None
