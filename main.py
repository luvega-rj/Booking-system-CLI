from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

# Create the database engine
engine = create_engine('sqlite:///events.db')
Base = declarative_base()

# Define the Event model
class Event(Base):
    __tablename__ = 'events'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    location = Column(String)
    cost_of_ticket = Column(Integer)
    organizers = relationship('User', secondary='bookings')

    def __repr__(self):
        return f"Event(id={self.id}, name='{self.name}', location='{self.location}', cost_of_ticket={self.cost_of_ticket})"


# Define the User model
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    events = relationship('Event', secondary='bookings', back_populates='users')

    def __repr__(self):
        return f"User(id={self.id}, name='{self.name}')"


# Define the Booking model
class Booking(Base):
    __tablename__ = 'bookings'

    event_id = Column(Integer, ForeignKey('events.id'), primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), primary_key=True)


# Create the tables in the database
def create_tables():
    Base.metadata.create_all(engine)


# Add a new event
def add_event(name, location, cost_of_ticket):
    session = Session()
    event = Event(name=name, location=location, cost_of_ticket=cost_of_ticket)
    session.add(event)
    session.commit()
    print("Event added successfully.")


# Get all events
def get_all_events():
    session = Session()
    events = session.query(Event).all()
    print("All events:")
    for event in events:
        print(event)


# Get events by name
def get_events_by_name(name):
    session = Session()
    events = session.query(Event).filter(Event.name == name).all()
    if events:
        print(f"Events with name '{name}':")
        for event in events:
            print(event)
    else:
        print(f"No events found with the name '{name}'.")


# Get events by organizers
def get_events_by_organizers(organizer):
    session = Session()
    events = session.query(Event).join(Event.organizers).filter(User.name == organizer).all()
    if events:
        print(f"Events organized by '{organizer}':")
        for event in events:
            print(event)
    else:
        print(f"No events found organized by '{organizer}'.")


# Book events
def book_events(event_names, user_id):
    session = Session()
    user = session.query(User).get(user_id)
    if user:
        events = session.query(Event).filter(Event.name.in_(event_names)).all()
        user.events.extend(events)
        session.commit()
        print("Events booked successfully.")
        return sum(event.cost_of_ticket for event in events)
    else:
        print(f"User with ID {user_id} does not exist.")


# Create a session
Session = sessionmaker(bind=engine)
