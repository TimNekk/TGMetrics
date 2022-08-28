import dash_bootstrap_components as dbc
from dash import html, dcc


class SettingsCardView:
    def __init__(self,
                 category_dropdown_id: str = "category-dropdown",
                 subcategory_dropdown_id: str = "subcategory-dropdown"):
        self.category_dropdown_id = category_dropdown_id
        self.subcategory_dropdown_id = subcategory_dropdown_id

    @property
    def content(self) -> dbc.Card:
        return dbc.Card(
            dbc.CardBody([
                html.H4("Статистика", className="card-title"),
                html.Div(
                    children=[
                        dcc.Dropdown(
                            id=self.category_dropdown_id,
                            placeholder="Выберите категорию",
                            style={
                                "color": "black"
                            }
                        ),
                        dcc.Dropdown(
                            id=self.subcategory_dropdown_id,
                            placeholder="Выберите тип",
                            className="mt-2",
                            style={
                                "color": "black"
                            }
                        )
                    ]
                )
            ])
        )
