from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import Column, String, Integer, create_engine, DateTime
import datetime

Base = declarative_base()


DATABASE_PATH = "sqlite:///contact_db.sqlite3"
ENGINE = create_engine(DATABASE_PATH, future=True)


class Contact_info(Base):
    __tablename__ = "contact_info"
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    email = Column(String(100))
    subject = Column(String(100))
    message = Column(String(1000))
    datetime = Column(DateTime, default=datetime.datetime.utcnow)


Session = sessionmaker(bind=ENGINE)


def save_info(name, email, subject, message):
    data = Contact_info(name=name, email=email, subject=subject, message=message)
    session = Session()
    session.add(data)
    session.commit()
    session.close()
