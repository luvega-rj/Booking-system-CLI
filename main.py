import orga

def menu():
    print("1. Register User")
    print("2. Add Event")
    print("3. View All Events")
    print("4. View Events by Name")
    print("5. Book Events")
    print("6. Quit")

    while True:
        selection = input("Your selection: ")
        if selection == "1":
            register_user()
        elif selection == "2":
            add_event()
        elif selection == "3":
            view_all_events()
        elif selection == "4":
            view_events_by_name()
        elif selection == "5":
            book_events()
        elif selection == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid selection. Please try again.")

def register_user():
    print("Enter user details:")
    name = input("Enter user's name: ")
    phone_number = input("Enter user's phone number: ")
    email = input("Enter user's email: ")
    orga.add_user(name, phone_number, email)
    print()

def add_event():
    print("Enter event details:")
    name = input("Enter event name: ")
    location = input("Enter event location: ")
    cost_of_ticket = int(input("Enter event cost of ticket: "))
    orga.add_event(name, location, cost_of_ticket)
    print()

def view_all_events():
    orga.get_all_events()
    print()

def view_events_by_name():
    name = input("Enter event name: ")
    orga.get_events_by_name(name)
    print()

def book_events():
    event_names = input("Enter event names to book (comma-separated): ").split(",")
    ticket_counts = input("Enter the number of tickets for each event (comma-separated): ").split(",")
    user_id = int(input("Enter your user ID: "))
    total_cost = orga.book_events(event_names, ticket_counts, user_id)
    print(f"Total cost of booked events: {total_cost}")
    print()

# Run the menu
menu()

