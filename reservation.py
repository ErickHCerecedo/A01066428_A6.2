"""
####################################################
# Reservation.py                                   #
#                                                  #
# Autor: Erick de Jesus Hernandez Cerecedo         #
# Matricula: A01066428                             #
# Fecha: 18 de febrero de 2024                     #
####################################################
"""
from datetime import datetime


class Reservation:
    """
    Representa un medio de reservaciones con información básica
    y funciones para gestionar reservas de habitaciones.
    """

    def __init__(self, customer, hotel, check_in,
                 check_out, room_number):  # pylint: disable=too-many-arguments
        self.customer = customer
        self.hotel = hotel
        self.check_in = check_in
        self.check_out = check_out
        self.room_number = room_number
        self.is_cancelled = False

    @classmethod
    def create_reservation(cls, customer, hotel, check_in, check_out,
                           room_number):  # pylint: disable=too-many-arguments
        """
        Crea una nueva reserva y la añade al hotel y cliente correspondientes.

        Args:
            cls: La clase Reservation.
            customer (Customer): El cliente que realiza la reserva.
            hotel (Hotel): El hotel donde se realiza la reserva.
            check_in (str): La fecha de entrada para la reserva.
            check_out (str): La fecha de salida para la reserva.
            room_number (int): El número de habitación a reservar.

        Returns:
            Reservation: El objeto Reservation que representa la
            reserva creada, o None si la habitación no está disponible.
        """
        # Verificar si las fechas están en el formato correcto
        try:
            check_in_date = datetime.strptime(check_in, '%Y-%m-%d')
            check_out_date = datetime.strptime(check_out, '%Y-%m-%d')
        except ValueError:
            print("┌──────────────────────────────────────────┐")
            print("│                                          │")
            print("│    Invalid date format. Please use       │")
            print("│    the format YYYY-MM-DD for dates.      │")
            print("│                                          │")
            print("└──────────────────────────────────────────┘\n")
            return None

        # Verificar si las fechas son válidas
        if check_in_date >= check_out_date:
            print("┌──────────────────────────────────────────┐")
            print("│                                          │")
            print("│    Check-in date must be before          │")
            print("│    check-out date.                       │")
            print("│                                          │")
            print("└──────────────────────────────────────────┘\n")
            return None

        if room_number in hotel.rooms_available:
            reservation = cls(customer, hotel, check_in,
                              check_out, room_number)
            hotel.rooms_available.remove(room_number)
            hotel.reservations.append(reservation)
            customer.reservations.append(reservation)
            print("┌──────────────────────────────────────────┐")
            print("│                                          │")
            print("│     Reservation created successfully!    │")
            print("│                                          │")
            print("└──────────────────────────────────────────┘\n")
            return reservation
        print("┌──────────────────────────────────────────┐")
        print("│                                          │")
        print("│    Room not available for reservation.   │")
        print("│                                          │")
        print("└──────────────────────────────────────────┘\n")
        return None

    def cancel_reservation(self):
        """
        Cancela la reserva y libera la habitación reservada.
        """
        if not self.is_cancelled:
            self.hotel.rooms_available.append(self.room_number)
            self.hotel.reservations.remove(self)
            self.customer.reservations.remove(self)
            self.is_cancelled = True
            print("┌──────────────────────────────────────────┐")
            print("│                                          │")
            print("│    Reservation canceled successfully!    │")
            print("│                                          │")
            print("└──────────────────────────────────────────┘\n")
        else:
            print("┌──────────────────────────────────────────┐")
            print("│                                          │")
            print("│     Reservation is already canceled.     │")
            print("│                                          │")
            print("└──────────────────────────────────────────┘\n")
