from typing import Type

from sqlalchemy import func, desc

from tgmetrics.repositories.group_by import GroupBy
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

    def get_by_id(self, user_id: int) -> User | None:
        with Session() as session:
            return session.query(self._model).get(user_id)

    def get_count(self, group_by: GroupBy) -> list[tuple[int, str]]:
        match group_by:
            case GroupBy.MONTH:
                date, limit, format_ = "month", 12, "Mon YY"
            case GroupBy.DAY:
                date, limit, format_ = "day", 31, "DD Mon"
            case GroupBy.HOUR:
                date, limit, format_ = "hour", 24, "HH DD Mon"
            case _:
                date, limit, format_ = "", 0, ""

        with Session() as session:
            return session.query(
                func.count(self._model.id),
                func.to_char(func.date_trunc(date, self._model.join_date), format_)) \
                       .group_by(func.date_trunc(date, self._model.join_date)) \
                       .order_by(desc(func.date_trunc(date, self._model.join_date))) \
                       .limit(limit) \
                       .all()[::-1]
