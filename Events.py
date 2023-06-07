from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///events.db')
Base = declarative_base()

Session = sessionmaker(bind=engine)
session = Session()


class Event(Base):
    __tablename__ = 'events'

    EventId = Column(Integer, primary_key=True)
    EventName = Column(String(50))
    EventDate = Column(Integer())
    EventTime = Column(Integer())
    Location = Column(String(100))
    TicketCost = Column(Float)


if __name__ == '__main__':
    engine = create_engine('sqlite:///events.db')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    event1 = Event(
        EventId=67,
        EventName="Sauti Sol Fest",
        EventDate=2023,
        EventTime=6,
        Location="Ngong Race Course",
        TicketCost=10000.0
    )
    event2 = Event(
        EventId=58,
        EventName="Nairobi Rugby Sevens",
        EventDate=2023,
        EventTime=5,
        Location="Ruaraka Grounds",
        TicketCost=5000.0
    )
    event3 = Event(
        EventId=87,
        EventName="Financial Bill Kamkunji",
        EventDate=2023,
        EventTime=9,
        Location="Jevanjee Gardens",
        TicketCost=7500.0
    )
    event4 = Event(
        EventId=13,
        EventName="Maandamano Mondays",
        EventDate=2023,
        EventTime=10,
        Location="Kanairo CBD",
        TicketCost=2500.0
    )

    session.add_all([event1, event2, event3, event4])
    session.commit()
