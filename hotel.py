"""
####################################################
# Hotel.py                                         #
#                                                  #
# Autor: Erick de Jesus Hernandez Cerecedo         #
# Matricula: A01066428                             #
# Fecha: 18 de febrero de 2024                     #
####################################################
"""
from reservation import Reservation


class Hotel:
    """
    Representa un hotel con información básica y funciones para
    gestionar reservas de habitaciones.
    """

    def __init__(self, name, location, phone, rooms_available):
        if not all([name, location, phone, rooms_available]):
            raise ValueError("All parameters must have a valid value")
        self.name = name
        self.location = location
        self.phone = phone
        self.rooms_available = rooms_available
        self.reservations = []

    def display_information(self):
        """Muestra la información del hotel.

        Returns:
            str: Información formateada del hotel.
        """
        info = ""
        info += "┌──────────────────────────────────────────┐\n"
        info += "│            Hotel Information             │\n"
        info += "├──────────────────────────────────────────┤\n"
        info += f"│ Name                 │ {self.name: <17} │\n"
        info += f"│ Location             │ {self.location: <17} │\n"
        info += f"│ Phone                │ {self.phone: <17} │\n"
        info += "│ Rooms Available      │ "
        if self.rooms_available:
            info += f"{', '.join(map(str, self.rooms_available)): <17} │\n"
        else:
            info += "None          │\n"
        info += self.display_reserved_rooms()
        return info

    def display_reserved_rooms(self):
        """Muestra la información de las habitaciones reservadas.

        Returns:
            str: Información formateada de las habitaciones reservadas.
        """
        info = ""
        if self.reservations:
            info += "├──────────────────────────────────────────┤\n"
            info += "│        Reserved Rooms Information        │\n"
            info += "├──────────────────────────────────────────┤\n"
            info += "│ Customer  │ Check-in  │ Check-out │ Room │\n"

            for reservation in self.reservations:
                info += f"│ {reservation.customer.name[:9]: <1}."\
                        f"│ {reservation.check_in: <0}"\
                        f"│ {reservation.check_out: <0}"\
                        f"│ {reservation.room_number: <5}│\n"
            info += "└──────────────────────────────────────────┘\n"
        else:
            info += "├──────────────────────────────────────────┤\n"
            info += "│           No reservations yet            │\n"
            info += "└──────────────────────────────────────────┘\n"

        return info

    def modify_information(self, name=None, location=None,
                           rooms_available=None):
        """Modifica la información del hotel.

        Args:
            name (str, optional): Nuevo nombre del hotel.
            location (str, optional): Nueva ubicación del hotel.
            rooms_available (list, optional):
            Nueva lista de habitaciones disponibles.

        """
        if name:
            self.name = name
        if location:
            self.location = location
        if rooms_available:
            self.rooms_available = rooms_available

    def reserve_room(self, customer, check_in, check_out, room_number):
        """Reserva una habitación en el hotel.

        Args:
            customer (Customer): Cliente que realiza la reserva.
            check_in (str): Fecha de entrada.
            check_out (str): Fecha de salida.
            room_number (int): Número de habitación a reservar.

        Returns:
            Reservation: La reserva creada, si es exitosa;
            None si la habitación no está disponible.
        """
        if room_number in self.rooms_available:
            reservation = Reservation.create_reservation(
                customer, self, check_in, check_out, room_number)
            if reservation:
                print("┌──────────────────────────────────────────┐")
                print("│                                          │")
                print("│        Room reserved successfully!       │")
                print("│                                          │")
                print("└──────────────────────────────────────────┘\n")
                return reservation
        else:
            print("┌──────────────────────────────────────────┐")
            print("│                                          │")
            print("│            Room not available.           │")
            print("│                                          │")
            print("└──────────────────────────────────────────┘\n")
        return None

    def cancel_reservation(self, customer_name, room_number):
        """Cancela una reserva en el hotel.

        Args:
            customer_name (str):
                Nombre del cliente cuya reserva se va a cancelar.
            room_number (int):
                Número de habitación de la reserva a cancelar.
        """
        for reservation in self.reservations:
            if (not reservation.is_cancelled and
                reservation.customer.name == customer_name and
                reservation.room_number == room_number): # noqa
                reservation.cancel_reservation()
                return
        print("┌──────────────────────────────────────────┐")
        print("│                                          │")
        print("│     No active reservation found for      │")
        print("│     this customer and room number.       │")
        print("│                                          │")
        print("└──────────────────────────────────────────┘\n")
