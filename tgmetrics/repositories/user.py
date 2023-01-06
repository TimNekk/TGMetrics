from typing import Type

from sqlalchemy import func, Integer
from sqlalchemy.orm import Query

from tgmetrics.repositories.group_by import GroupBy
from tgmetrics.services.db import Session
from tgmetrics.services.db.models import User


class UserRepository:
    def __init__(self, user: Type[User]) -> None:
        self._model = user
        self._hour = func.date_trunc("hour", self._model.join_date)
        self._day = func.date_trunc("day", self._model.join_date)
        self._month = func.date_trunc("month", self._model.join_date)
        self._year = func.date_part("year", self._model.join_date)

    @property
    def model(self) -> Type[User]:
        return self._model

    def get_all(self) -> list[User]:
        with Session() as session:
            return session.query(self._model).all()

    def get_by_id(self, user_id: int) -> User | None:
        with Session() as session:
            return session.query(self._model).get(user_id)

    def get_count_query(self, group_by: GroupBy) -> Query:
        match group_by:
            case GroupBy.MONTH:
                return self._get_count_by_month()
            case GroupBy.DAY:
                return self._get_count_by_day()
            case GroupBy.HOUR:
                return self._get_count_by_hour()

    def _get_count_by_month(self) -> Query:
        with Session() as session:
            return (
                session.query(
                    func.count(self._model.id),
                    func.to_char(self._month, "Mon"),
                    func.cast(self._year, Integer)
                )
                .group_by(self._month, self._year)
                .order_by(self._month)
                .all()
            )

    def _get_count_by_day(self) -> Query:
        with Session() as session:
            return (
                session.query(
                    func.count(self._model.id),
                    func.to_char(self._day, "DD"),
                    func.to_char(self._month, "Mon")
                )
                .filter(self._year == func.date_part("year", func.now()))
                .group_by(self._day, self._month)
                .order_by(self._day)
                .all()
            )

    def _get_count_by_hour(self) -> Query:
        with Session() as session:
            return (
                session.query(
                    func.count(self._model.id),
                    func.to_char(self._hour, "HH24"),
                    func.to_char(self._day, "DD"),
                )
                .filter(self._month == func.date_trunc("month", func.now()))
                .filter(self._year == func.date_part("year", func.now()))
                .group_by(self._hour, self._day)
                .order_by(self._hour)
                .all()
            )
