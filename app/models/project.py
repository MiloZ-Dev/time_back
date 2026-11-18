from decimal import Decimal

from sqlalchemy import ForeignKey, Numeric, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base


class Project(Base):
    __tablename__ = "projects"

    id: Mapped[int] = mapped_column(primary_key=True)
    month_id: Mapped[int] = mapped_column(ForeignKey("months.id", ondelete="CASCADE"))
    name: Mapped[str] = mapped_column(String(120))
    budget_hours: Mapped[Decimal] = mapped_column(Numeric(6, 2))

    month: Mapped["Month"] = relationship(back_populates="projects")
    entries: Mapped[list["TimeEntry"]] = relationship(
        back_populates="project", cascade="all, delete-orphan"
    )