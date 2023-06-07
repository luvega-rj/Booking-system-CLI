from sqlalchemy import create_engine, Column, Integer, Float
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///events.db')
Base = declarative_base()

Session = sessionmaker(bind=engine)
session = Session()


class BookingTable(Base):
    __tablename__ = 'bookingtable'

    id = Column(Integer, primary_key=True)
    eventid = Column(Integer)
    attendeesid = Column(Integer)
    tickets = Column(Integer)
    total_amount = Column(Float)


if __name__ == '__main__':
    engine = create_engine('sqlite:///events.db')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    booking1 = BookingTable(
        eventid=67,  # Use lowercase 'eventid' instead of 'EventId'
        attendeesid=1,
        tickets=2,
        total_amount=200.0
    )
    booking2 = BookingTable(
        eventid=58,
        attendeesid=2,
        tickets=4,
        total_amount=1000.0
    )
    booking3 = BookingTable(
        eventid=87,
        attendeesid=3,
        tickets=3,
        total_amount=500.0
    )
    booking4 = BookingTable(
        eventid=13,
        attendeesid=4,
        tickets=1,
        total_amount=100.0
    )

    session.add_all([booking1, booking2, booking3, booking4])
    session.commit()
