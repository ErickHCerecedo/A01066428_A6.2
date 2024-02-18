from hotel import Hotel
from customer import Customer
from reservation import Reservation

if __name__ == "__main__":
    # Crear un hotel
    hotel = Hotel("Grand Hotel", "City Center", "222-1234", [101, 102, 103])

    # Mostrar información del hotel
    print(hotel.display_information())

    # Crear un cliente
    customer = Customer("John Doestination", "john@example.com", "123 Main St", "555-1234")

    # Mostrar información del cliente
    customer.display_information()

    # Crear una reserva para el cliente en el hotel
    reservation = Reservation.create_reservation(customer, hotel, "2024-02-17", "2024-02-20", 101)

    # Mostrar información actualizada del hotel y del cliente
    print(hotel.display_information())
    print(customer.display_information())

    # Cancelar la reserva del cliente en el hotel
    reservation.cancel_reservation()

    # Mostrar información actualizada del hotel y del cliente
    print(hotel.display_information())
    print(customer.display_information())

    # Reservar 
    hotel.reserve_room(customer, "2024-02-17", "2024-02-20", 101)

    # Mostrar información actualizada del hotel y del cliente
    print(hotel.display_information())
    print(customer.display_information())

    # Reservar 
    hotel.reserve_room(customer, "2024-02-17", "2024-02-20", 101)
