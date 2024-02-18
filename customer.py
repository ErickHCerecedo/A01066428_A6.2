"""
####################################################
# Customer.py                                      #
#                                                  #
# Autor: Erick de Jesus Hernandez Cerecedo         #
# Matricula: A01066428                             #
# Fecha: 18 de febrero de 2024                     #
####################################################
"""


class Customer:
    """
    Representa un cliente con información básica y funciones para
    gestionar reservas de habitaciones.
    """

    def __init__(self, name, email, address=None, phone=None):
        if not all([name, email]):
            raise ValueError("Please provide required information.")
        self.name = name
        self.email = email
        self.address = address
        self.phone = phone
        self.reservations = []

    def display_information(self):
        """
        Retorna un string que representa la información del cliente.

        Returns:
            str: Información formateada del cliente.
        """
        info = ""
        info += "┌──────────────────────────────────────────┐\n"
        info += "│          Customer Information            │\n"
        info += "├──────────────────────────────────────────┤\n"
        info += f"│  Name     │ {self.name: <28} │\n"
        info += f"│  Email    │ {self.email: <28} │\n"
        info += f"│  Address  │ {self.address: <28} │\n"
        info += f"│  Phone    │ {self.phone: <28} │\n"
        info += self.display_reservations()
        return info

    def modify_information(self, name=None, email=None,
                           address=None, phone=None):
        """
        Modifica la información de cliente según los argumentos proporcionados.

        Args:
            name (str, opcional): El nuevo nombre del cliente.
                                  Por defecto es None.
            email (str, opcional): El nuevo correo electrónico del cliente.
                                   Por defecto es None.
            address (str, opcional): La nueva dirección del cliente.
                                     Por defecto es None.
            phone (str, opcional): El nuevo número de teléfono del cliente.
                                   Por defecto es None.
        """
        if name:
            self.name = name
        else:
            raise ValueError("Please provide a name.")
        if email:
            self.email = email
        else:
            raise ValueError("Please provide an email.")
        if address:
            self.address = address
        if phone:
            self.phone = phone

    def create_reservation(self, hotel, check_in, check_out, room_number):
        """
        Crea una nueva reserva de habitación
        para el cliente en el hotel especificado.

        Args:
            hotel (Hotel): El objeto Hotel donde se realizará la reserva.
            check_in (str): La fecha de entrada para la reserva.
            check_out (str): La fecha de salida para la reserva.
            room_number (int): El número de habitación a reservar.

        Returns:
            Reservation: El objeto Reservation que
            representa la reserva creada.
        """
        return hotel.reserve_room(self, check_in, check_out, room_number)

    def cancel_reservation(self, hotel, room_number):
        """
        Cancela la reserva del cliente en el hotel
        para la habitación especificada.

        Args:
            hotel (Hotel):
                El objeto Hotel donde se realizó la reserva.
            room_number (int):
                El número de habitación de la reserva a cancelar.
        """
        hotel.cancel_reservation(self.name, room_number)

    def display_reservations(self):
        """
        Retorna un string que representa las reservas del cliente.

        Returns:
            str: Información formateada de las reservas del cliente.
        """
        info = ""
        if self.reservations:
            info += "├──────────────────────────────────────────┤\n"
            info += "│         Reservations Information         │\n"
            info += "├──────────────────────────────────────────┤\n"
            info += "│ Hotel     │ Check-in  │ Check-out │ Room │\n"
            for reservation in self.reservations:
                info += f"│ {reservation.hotel.name[:9]: <0}."\
                        f"│ {reservation.check_in: <0}"\
                        f"│ {reservation.check_out: <0}"\
                        f"│ {reservation.room_number: <4} │\n"
            info += "└──────────────────────────────────────────┘\n\n"
        else:
            info += "├──────────────────────────────────────────┤\n"
            info += "│       No Reservations Information        │\n"
            info += "└──────────────────────────────────────────┘\n\n"
        return info
