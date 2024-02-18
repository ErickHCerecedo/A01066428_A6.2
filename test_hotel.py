import unittest
from hotel import Hotel
from customer import Customer
from reservation import Reservation

class TestHotel(unittest.TestCase):
    def setUp(self):
        # Creamos un hotel de ejemplo para las pruebas
        self.hotel = Hotel("Hotel Example", "Location Example", "1234567890", [101, 102, 103])

    # Pruebas positivas
    def test_display_information_positive(self):
        # Verificamos si la información del hotel se muestra correctamente
        info = ""
        info += "┌──────────────────────────────────────────┐\n"
        info += "│            Hotel Information             │\n"
        info += "├──────────────────────────────────────────┤\n"
        info += f"│ Name                 │ {self.hotel.name: <17} │\n"
        info += f"│ Location             │ {self.hotel.location: <17} │\n"
        info += f"│ Phone                │ {self.hotel.phone: <17} │\n"
        info += "│ Rooms Available      │ "
        if self.hotel.rooms_available:
            info += f"{', '.join(map(str, self.hotel.rooms_available)): <17} │\n"
        else:
            info += "None          │\n"
        info += "├──────────────────────────────────────────┤\n"
        info += "│           No reservations yet            │\n"
        info += "└──────────────────────────────────────────┘\n"
        self.assertEqual(self.hotel.display_information(), info)  # Se espera que devuelva None

    def test_modify_information_positive(self):
        # Modificamos la información del hotel y verificamos si los cambios se aplican correctamente
        self.hotel.modify_information(name="New Hotel Name", location="New Location", rooms_available=[201, 202])
        self.assertEqual(self.hotel.name, "New Hotel Name")
        self.assertEqual(self.hotel.location, "New Location")
        self.assertEqual(self.hotel.rooms_available, [201, 202])
 
    def test_reserve_room_positive(self):
        # Intentamos reservar una habitación disponible
        customer = Customer("John Doestination", "john@example.com", "123 Main St", "555-1234")
        reservation = self.hotel.reserve_room(customer, "2024-02-17", "2024-02-20", 101)
        self.assertIsNotNone(reservation)  # Se espera que la reserva no sea None
        self.assertNotIn(101, self.hotel.rooms_available)  # Se espera que la habitación reservada se elimine de las disponibles

    def test_cancel_reservation_positive(self):
        # Reservamos una habitación y luego cancelamos la reserva
        customer = Customer("John Doestination", "john@example.com", "123 Main St", "555-1234")
        self.hotel.reserve_room(customer, "2024-02-17", "2024-02-20", 101)
        self.hotel.cancel_reservation(customer.name, 101)
        self.assertIn(101, self.hotel.rooms_available)  # Se espera que la habitación reservada esté disponible nuevamente

    def test_cancel_reservation_negative(self):
        # Intentamos cancelar una reserva que no existe
        self.assertEqual(self.hotel.cancel_reservation("Nonexistent Customer", 101), None)
        self.assertEqual(self.hotel.cancel_reservation("John Doestination", 101), None)
        self.assertEqual(self.hotel.cancel_reservation("John Doestination", 102), None)

    # Pruebas negativas
    def test_reserve_room_negative(self):
        # Intentamos reservar una habitación no disponible
        customer = Customer("John Doestination", "john@example.com", "123 Main St", "555-1234")
        reservation = self.hotel.reserve_room(customer, "2024-02-17", "2024-02-20", 104)
        self.assertIsNone(reservation)  # Se espera que la reserva sea None
 
    def test_modify_information_negative(self):
        # Intentamos modificar la información del hotel con valores inválidos
        self.hotel.modify_information(name=None, location=None, rooms_available=None)
        self.assertNotEqual(self.hotel.name, None)  # Se espera que el nombre no sea None
        self.assertNotEqual(self.hotel.location, None)  # Se espera que la ubicación no sea None
        self.assertNotEqual(self.hotel.rooms_available, None)  # Se espera que las habitaciones disponibles no sean None

    def test_cancel_reservation_negative(self):
        # Intentamos cancelar una reserva con valores inválidos
        self.assertEqual(self.hotel.cancel_reservation("Customer Name", 104), None)

    def test_display_information_negative(self):
        # Intentamos mostrar la información del hotel con un objeto no válido
        try:
            invalid_hotel = Hotel(None, None, None, None)
            invalid_hotel.display_information()
        except Exception as e:
            # Verificamos que se haya producido una excepción
            self.assertIsInstance(e, ValueError)
        else:
            # Si no se produjo ninguna excepción, fallamos el test
            self.fail("No se generó ninguna excepción al mostrar información con datos inválidos")

if __name__ == '__main__':
    unittest.main()
