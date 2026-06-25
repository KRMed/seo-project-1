import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from db import Base, DayLog, save_log, get_logs, get_log_by_date
import db

#To test, use pytest test.py -v

@pytest.fixture(autouse=True)
def test_db():
  test = create_engine("sqlite://") #this creates it in memory rather than a file
  Base.metadata.create_all(test)
  db.engine = test
  yield #test runs
  db.engine = create_engine("sqlite:///day_logs.db") #sets db back to og

def test_save_and_get():
  save_log("2026-06-25", "Super Busy day, good luck with that")
  log = get_log_by_date("2026-06-25")
  assert log.summary == "Super Busy day, good luck with that"

def test_missing_summary():
  assert get_log_by_date("1000-01-01") is None

def test_get_all():
  save_log("2026-06-25", "Summary 1")
  save_log("2026-06-25", "Summary 2")
  logs = get_logs()
  assert len(logs) == 2
  assert logs[0].date == "2026-06-25" 
  assert logs[0].summary == "Summary 1"
  assert logs[1].date == "2026-06-25"
  assert logs[1].summary == "Summary 2"
