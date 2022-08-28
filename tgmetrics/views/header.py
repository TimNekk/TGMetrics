import dash_bootstrap_components as dbc


class HeaderView:
    @property
    def content(self) -> dbc.NavbarSimple:
        return dbc.NavbarSimple(
            brand="TGMetrics",
            color="primary",
            dark=True,
            children=[
                dbc.DropdownMenu(
                    nav=True,
                    in_navbar=True,
                    label="Боты",
                    direction="left",
                    children=[
                        dbc.DropdownMenuItem("DreamPowerBot", class_name="text-secondary"),
                        dbc.DropdownMenuItem("PerfectPowerBot", class_name="text-secondary"),
                    ]
                )
            ]
        )
