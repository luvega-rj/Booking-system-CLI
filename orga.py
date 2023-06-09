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

    def __repr__(self):
        return f"Event(id={self.id}, name='{self.name}', location='{self.location}', cost_of_ticket={self.cost_of_ticket})"


# Define the User model
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    phone_number = Column(String)
    email = Column(String)

    def __repr__(self):
        return f"User(id={self.id}, name='{self.name}', phone_number='{self.phone_number}', email='{self.email}')"


# Define the Booking model
class Booking(Base):
    __tablename__ = 'bookings'

    event_id = Column(Integer, ForeignKey('events.id'), primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), primary_key=True)
    ticket_count = Column(Integer)

    event = relationship('Event')
    user = relationship('User')

    def __repr__(self):
        return f"Booking(event_id={self.event_id}, user_id={self.user_id}, ticket_count={self.ticket_count})"


# Create the tables in the database
def create_tables():
    Base.metadata.create_all(engine)


# Add a new event
def add_event(name, location, cost_of_ticket):
    Session = sessionmaker(bind=engine)
    session = Session()
    event = Event(name=name, location=location, cost_of_ticket=cost_of_ticket)
    session.add(event)
    session.commit()
    print("Event added successfully.")


# Get all events
def get_all_events():
    Session = sessionmaker(bind=engine)
    session = Session()
    events = session.query(Event).all()
    print("All events:")
    for event in events:
        print(event)


# Get events by name
def get_events_by_name(name):
    Session = sessionmaker(bind=engine)
    session = Session()
    events = session.query(Event).filter(Event.name == name).all()
    if events:
        print(f"Events with name '{name}':")
        for event in events:
            print(event)
    else:
        print(f"No events found with the name '{name}'.")


# Book events
def book_events(event_names, ticket_counts, user_id):
    Session = sessionmaker(bind=engine)
    session = Session()
    user = session.query(User).get(user_id)
    if user:
        total_cost = 0
        for event_name, ticket_count in zip(event_names, ticket_counts):
            event = session.query(Event).filter(Event.name == event_name).first()
            if event:
                booking = Booking(event=event, user=user, ticket_count=int(ticket_count))
                session.add(booking)
                total_cost += event.cost_of_ticket * int(ticket_count)
        session.commit()
        print("Events booked successfully.")
        return total_cost
    else:
        print(f"User with ID {user_id} does not exist.")
        return None


# Add a new user
def add_user(name, phone_number, email):
    Session = sessionmaker(bind=engine)
    session = Session()
    user = User(name=name, phone_number=phone_number, email=email)
    session.add(user)
    session.commit()
    print("User added successfully.")


# Create tables in the database
create_tables()


