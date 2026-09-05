from sqlalchemy.orm import mapped_column, Mapped


class IntIdPKMixin:
    id: Mapped[int] = mapped_column(primary_key=True)
