from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///events.db')
Base = declarative_base()

Session = sessionmaker(bind=engine)
session = Session()


class Organisers(Base):
    __tablename__ = 'organisers'

    Id = Column(Integer, primary_key=True)
    Name = Column(String(50))
    Contact = Column(String(20))
    EventInCharge = Column(Integer)


if __name__ == '__main__':
    engine = create_engine('sqlite:///events.db')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    organiser1 = Organisers(
        Name="Dmitri Auba",
        Contact="1234567890",
        EventInCharge=1
    )
    organiser2 = Organisers(
        Name="Loftus Cheek",
        Contact="9876543210",
        EventInCharge=2
    )
    organiser3 = Organisers(
        Name="Mason Mount",
        Contact="5555555555",
        EventInCharge=3
    )
    organiser4 = Organisers(
        Name="Ngolo Kante",
        Contact="768765789",
        EventInCharge=4,
    )

    session.add_all([organiser1, organiser2, organiser3, organiser4])
    session.commit()
