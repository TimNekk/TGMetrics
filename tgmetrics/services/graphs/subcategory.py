from tgmetrics.services.graphs.period import GraphPeriod


class GraphSubcategory:
    def __init__(self, name: str, repository, periods: list[GraphPeriod]):
        self.name = name
        self.periods = periods
        self._setup_periods(repository)

    def _setup_periods(self, repository):
        for period in self.periods:
            period.set_repository(repository)

    @property
    def periods_names(self) -> list[str]:
        return [period.name for period in self.periods]

    def get_period(self, period_name: str) -> GraphPeriod | None:
        for period in self.periods:
            if period.name == period_name:
                return period
        return None

