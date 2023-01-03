import sqlalchemy as sa

from ..crud import Base


class Model(Base):
    __abstract__ = True

    id = sa.Column(sa.Integer, primary_key=True)

    def __repr__(self) -> str:
        return self._repr(id=self.id)

    def _repr(self, **fields) -> str:
        field_strings = []
        at_least_one_attached_attribute = False
        for key, field in fields.items():
            try:
                field_strings.append(f'{key}={field!r}')
            except sa.orm.exc.DetachedInstanceError:
                field_strings.append(f'{key}=DetachedInstanceError')
            else:
                at_least_one_attached_attribute = True
        if at_least_one_attached_attribute:
            return f"<{self.__class__.__name__}({', '.join(field_strings)})>"
        return f"<{self.__class__.__name__} {id(self)}>"
