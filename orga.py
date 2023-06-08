import main

# Menu function
def menu():
    print("-- Event Booking App --")
    print("\nSelect one of these options:")
    print("1) Add a new event.")
    print("2) See all events.")
    print("3) Find event by name.")
    print("4) See event organizers.")
    print("5) Book events.")
    print("6) Quit.")

    while True:
        try:
            selection = int(input("\nYour selection: "))
            if selection == 1:
                add_new_event()
            elif selection == 2:
                get_all_events()
            elif selection == 3:
                find_event_by_name()
            elif selection == 4:
                see_event_organizers()
            elif selection == 5:
                book_event()
            elif selection == 6:
                print("Thank you for using the Event Booking App. Goodbye!")
                break
            else:
                print("Invalid selection. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

# Add a new event
def add_new_event():
    print("\nEnter event details:")
    name = input("Enter event name: ")
    location = input("Enter event location: ")
    cost_of_ticket = int(input("Enter the cost of the ticket: "))

    main.add_event(name, location, cost_of_ticket)

# Get all events
def get_all_events():
    main.get_all_events()

# Find event by name
def find_event_by_name():
    name = input("\nEnter event name to find: ")
    main.get_events_by_name(name)

# See event organizers
def see_event_organizers():
    name = input("\nEnter event name to see organizers: ")
    main.get_events_by_organizers(name)

# Book events
def book_event():
    event_names = input("\nEnter event names to book (comma-separated): ").split(",")
    total_cost = main.book_events(event_names)
    print(f"\nTotal cost of booked events: {total_cost}")

# Call the menu function
menu()
