from sqlalchemy.orm import Mapped, mapped_column

from .db import Base


class ResultOrm(Base):
    __tablename__ = "data"

    id: Mapped[int] = mapped_column(primary_key=True)
    competence: Mapped[float]
    network_ability: Mapped[float]
    promoted: Mapped[bool]
