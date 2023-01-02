from datetime import datetime

import sqlalchemy as sa

from .base import Model


class User(Model):
    __tablename__ = 'users'

    join_date = sa.Column(sa.DateTime, default=datetime.now())
    deep_link = sa.Column(sa.String(255))

    def __repr__(self) -> str:
        return self._repr(id=self.id,
                          join_date=self.join_date,
                          deep_link=self.deep_link)
