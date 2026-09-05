from sqlalchemy.orm import Mapped, mapped_column

from core.models import Base
from core.models.mixins.int_id_pk import IntIdPKMixin


class User(IntIdPKMixin, Base):
    username: Mapped[str] = mapped_column(unique=True)
