from typing import Optional
from datetime import datetime
from sqlalchemy import String, create_engine, select
from sqlalchemy.orm import Session, DeclarativeBase, Mapped, mapped_column, relationship

class Base(DeclarativeBase):
  pass

class DayLog(Base):
  __tablename__ = "day_logs"
  id: Mapped[int] = mapped_column(primary_key=True)
  date: Mapped[str] = mapped_column(String(10))
  summary: Mapped[str]

engine = create_engine("sqlite:///day_logs.db")
Base.metadata.create_all(engine)

def save_log(date, summary):
  with Session(engine) as session:
    session.add(DayLog(date=date, summary=summary))
    session.commit()

def get_logs():
  with Session(engine) as session:
    stmt = select(DayLog)
    return session.scalars(stmt).all()