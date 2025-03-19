
class Flight:
    def __init__(self, flight_number, destination, capacity):
        self.flight_number = flight_number
        self.destination = destination
        self.capacity = capacity
        self.passenger_list = []

    def book_seat(self, passenger):
        if len(self.passenger_list) < self.capacity:
            self.passenger_list.append(passenger)
            print(f"Seat booked successfully for {passenger.name} on Flight {self.flight_number}.")
        else:
            print("Sorry, no available seats on this flight.")

    def cancel_booking(self, passenger_id):
        for passenger in self.passenger_list:
            if passenger.passenger_id == passenger_id:
                self.passenger_list.remove(passenger)
                print(f"Booking canceled for {passenger.name}.")
                return
        print("Passenger not found on this flight.")

    def display_passenger_list(self):
        if not self.passenger_list:
            print(f"No passengers on Flight {self.flight_number}.")
        else:
            print(f"Passengers for Flight {self.flight_number} to {self.destination}:")
            for passenger in self.passenger_list:
                print(f"- {passenger.name}, ID: {passenger.passenger_id}")

    def is_seat_available(self):
        return len(self.passenger_list) < self.capacity


class Passenger:
    def __init__(self, passenger_id, name, contact_info):
        self.passenger_id = passenger_id
        self.name = name
        self.contact_info = contact_info

    def update_details(self, name=None, contact_info=None):
        if name:(3, "Prashanth", "charlie@example.com")
            self.name = name
        if contact_info:
            self.contact_info = contact_info
        print("Passenger details updated.")


class AirlineBookingSystem:
    def __init__(self):
        self.flights = []

    def add_flight(self, flight):
        self.flights.append(flight)
        print(f"Flight {flight.flight_number} added to the system.")

    def find_flight(self, flight_number):
        for flight in self.flights:
            if flight.flight_number == flight_number:
                return flight
        return None

    def display_all_flights(self):
        if not self.flights:
            print("No flights available.")
        else:
            print("Available Flights:")
            for flight in self.flights:
                print(f"- {flight.flight_number} to {flight.destination}, Capacity: {flight.capacity - len(flight.passenger_list)} seats left")


# Example usage
if __name__ == "__main__":
    # Create an airline booking system
    booking_system = AirlineBookingSystem()

    # Add flights
    flight1 = Flight("AI101", "New York", 2)
    flight2 = Flight("AI202", "London", 3)

    booking_system.add_flight(flight1)
    booking_system.add_flight(flight2)

    # Create passengers
    passenger1 = Passenger(1, "Ahmad", "ahmad@example.com")
    passenger2 = Passenger(2, "Amit", "amit@example.com")
    passenger3 = Passenger

    # Book flights
    flight1.book_seat(passenger1)
    flight1.book_seat(passenger2)
    flight1.book_seat(passenger3)  # This will indicate no available seats

    # Display passenger list
    flight1.display_passenger_list()

    # Cancel a booking
    flight1.cancel_booking(1)

    # Display passenger list again
    flight1.display_passenger_list()

    # Update passenger details
    passenger2.update_details(name="Ahmad", contact_info="Ahmad@example.com")

    # Check flight availability
    if flight1.is_seat_available():
        print("Seats are available on this flight.")
    else:
        print("No seats available on this flight.")

    # Display all flights
    booking_system.display_all_flights()

