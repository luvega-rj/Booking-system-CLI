from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///events.db')
Base = declarative_base()

Session = sessionmaker(bind=engine)
session = Session()


class Attendees(Base):
    __tablename__ = 'attendees'

    Id = Column(Integer, primary_key=True)
    Firstname = Column(String(50))
    PhoneNumber = Column(String(20))
    Email = Column(String(100))
    EventId = Column(Integer)


if __name__ == '__main__':
    engine = create_engine('sqlite:///events.db')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    attendee1 = Attendees(
        Firstname="Ronald",
        PhoneNumber="1234567890",
        Email="ronald@gmail.com",
        EventId=1
    )
    attendee2 = Attendees(
        Firstname="Mike",
        PhoneNumber="9876543210",
        Email="mike@gmail.com",
        EventId=2
    )
    attendee3 = Attendees(
        Firstname="Bob",
        PhoneNumber="5555555555",
        Email="bob@gmail.com",
        EventId=3
    )

    session.add_all([attendee1, attendee2, attendee3])
    session.commit()
