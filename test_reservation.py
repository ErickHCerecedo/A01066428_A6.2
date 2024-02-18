import unittest
from reservation import Reservation
from customer import Customer
from hotel import Hotel


class TestReservation(unittest.TestCase):

    def setUp(self):
        self.customer = Customer("John Doe", "john@example.com")
        self.hotel = Hotel("Hotel Example", "123 Example St", "555-1234", [101, 102])
        self.valid_reservation = Reservation(self.customer, self.hotel, "2024-03-01", "2024-03-05", 101)

    def test_create_reservation_positive(self):
        # Intentamos crear una reserva válida
        reservation = Reservation.create_reservation(self.customer, self.hotel, "2024-03-10", "2024-03-15", 102)
        self.assertIsNotNone(reservation)
        self.assertEqual(reservation.customer, self.customer)
        self.assertEqual(reservation.hotel, self.hotel)
        self.assertEqual(reservation.check_in, "2024-03-10")
        self.assertEqual(reservation.check_out, "2024-03-15")
        self.assertEqual(reservation.room_number, 102)
        self.assertFalse(reservation.is_cancelled)

    def test_cancel_reservation_positive(self):
        # Intentamos cancelar una reserva válida
        reservation = Reservation.create_reservation(self.customer, self.hotel, "2024-03-10", "2024-03-15", 102)
        reservation.cancel_reservation()
        self.assertTrue(reservation.is_cancelled)
        self.assertIn(102, self.hotel.rooms_available)
        self.assertNotIn(reservation, self.hotel.reservations)
        self.assertNotIn(reservation, self.customer.reservations)

    # Casos de prueba negativos

    def test_create_reservation_negative(self):
        # Intentamos crear una reserva para una habitación no disponible
        Reservation.create_reservation(self.customer, self.hotel, "2024-03-01", "2024-03-05", 101)
        reservation = Reservation.create_reservation(self.customer, self.hotel, "2024-03-01", "2024-03-05", 101)
        self.assertIsNone(reservation)
        # Intentamos crear una reserva con fechas inválidas
        reservation = Reservation.create_reservation(self.customer, self.hotel, "2024-03-10", "2023-03-05", 102)
        self.assertIsNone(reservation)

    def test_cancel_reservation_negative(self):
        # Intentamos cancelar una reserva inexistente
        reservation = Reservation(self.customer, self.hotel, "2024-03-10", "2024-03-15", 102)
        with self.assertRaises(ValueError):
            reservation.cancel_reservation()


if __name__ == "__main__":
    unittest.main()
