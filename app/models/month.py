from decimal import Decimal

from sqlalchemy import Numeric, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base


class Month(Base):
    __tablename__ = "months"
    __table_args__ = (UniqueConstraint("year", "month"),)

    id: Mapped[int] = mapped_column(primary_key=True)
    year: Mapped[int]
    month: Mapped[int]
    contract_hours: Mapped[Decimal] = mapped_column(Numeric(6, 2), default=130)

    projects: Mapped[list["Project"]] = relationship(
        back_populates="month", cascade="all, delete-orphan"
    )