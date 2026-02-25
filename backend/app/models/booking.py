import enum
import uuid
from datetime import datetime
from decimal import Decimal
from typing import TYPE_CHECKING

from sqlalchemy import DateTime, Enum, Integer, Numeric, String, func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.database import Base

if TYPE_CHECKING:
    from app.models.member import BookingMember
    from app.models.payment import Payment


class BookingStatus(str, enum.Enum):
    DRAFT = "DRAFT"
    PENDING_PAYMENT = "PENDING_PAYMENT"
    PAID = "PAID"
    FAILED = "FAILED"
    CANCELLED = "CANCELLED"


class TicketCategory(str, enum.Enum):
    STUDENT = "STUDENT"
    STANDARD = "STANDARD"


TICKET_PRICES: dict[TicketCategory, Decimal] = {
    TicketCategory.STUDENT: Decimal("200.00"),
    TicketCategory.STANDARD: Decimal("300.00"),
}


def calculate_totals(ticket_category: TicketCategory, members_count: int) -> tuple[int, Decimal, Decimal]:
    if members_count < 0:
        raise ValueError("members_count cannot be negative")

    total_attendees = 1 + members_count
    price_per_ticket = TICKET_PRICES[ticket_category]
    total_amount = (price_per_ticket * total_attendees).quantize(Decimal("0.01"))
    return total_attendees, price_per_ticket, total_amount


class Booking(Base):
    __tablename__ = "bookings"

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    status: Mapped[BookingStatus] = mapped_column(
        Enum(BookingStatus, name="booking_status"),
        nullable=False,
        default=BookingStatus.DRAFT,
        server_default=BookingStatus.DRAFT.value,
    )
    ticket_category: Mapped[TicketCategory] = mapped_column(
        Enum(TicketCategory, name="ticket_category"),
        nullable=False,
    )
    currency: Mapped[str] = mapped_column(String(8), nullable=False, default="USD", server_default="USD")
    price_per_ticket: Mapped[Decimal] = mapped_column(Numeric(10, 2), nullable=False)
    total_attendees: Mapped[int] = mapped_column(Integer, nullable=False)
    total_amount: Mapped[Decimal] = mapped_column(Numeric(10, 2), nullable=False)

    group_lead_prefix: Mapped[str | None] = mapped_column(String(20), nullable=True)
    group_lead_first_name: Mapped[str] = mapped_column(String(80), nullable=False)
    group_lead_last_name: Mapped[str] = mapped_column(String(80), nullable=False)
    company_name: Mapped[str] = mapped_column(String(140), nullable=False)
    designation: Mapped[str | None] = mapped_column(String(120), nullable=True)
    group_lead_email: Mapped[str] = mapped_column(String(254), nullable=False)

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        server_default=func.now(),
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        server_default=func.now(),
        onupdate=func.now(),
    )

    members: Mapped[list["BookingMember"]] = relationship(
        back_populates="booking",
        cascade="all, delete-orphan",
        passive_deletes=True,
    )
    payments: Mapped[list["Payment"]] = relationship(
        back_populates="booking",
        cascade="all, delete-orphan",
        passive_deletes=True,
    )
