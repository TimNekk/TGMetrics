from typing import Type

from sqlalchemy import func, desc

from tgmetrics.services.db import Session
from tgmetrics.services.db.models import User


class UserRepository:
    def __init__(self, user: Type[User]) -> None:
        self._model = user

    @property
    def model(self) -> Type[User]:
        return self._model

    def get_all(self) -> list[User]:
        with Session() as session:
            return session.query(self._model).all()

    def get_by_id(self, id: int) -> User | None:
        with Session() as session:
            return session.query(self._model).get(id)

    def get_count_by_month(self, month_format: str = "Mon YY") -> list[tuple[int, str]]:
        with Session() as session:
            return session.query(
                func.count(self._model.id),
                func.to_char(func.date_trunc("month", self._model.join_date), month_format)) \
                .group_by(func.date_trunc("month", self._model.join_date)) \
                .order_by(func.date_trunc("month", self._model.join_date)) \
                .all()
