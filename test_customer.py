import unittest
from customer import Customer
from hotel import Hotel
from reservation import Reservation


class TestCustomer(unittest.TestCase):

    def setUp(self):
        self.valid_customer = Customer("John Doe", "john@example.com", "123 Main St", "555-1234")
        self.hotel = Hotel("Hotel Example", "123 Example St", "555-5678", [101, 102])

    # Casos de prueba positivos

    def test_display_information_positive(self):
        info = self.valid_customer.display_information()
        self.assertIsInstance(info, str)

    def test_modify_information_positive(self):
        self.valid_customer.modify_information(name="Jane Doe", email="jane@example.com", address="456 Elm St", phone="555-4321")
        self.assertEqual(self.valid_customer.name, "Jane Doe")
        self.assertEqual(self.valid_customer.email, "jane@example.com")
        self.assertEqual(self.valid_customer.address, "456 Elm St")
        self.assertEqual(self.valid_customer.phone, "555-4321")

    def test_create_reservation_positive(self):
        reservation = self.valid_customer.create_reservation(self.hotel, "2024-03-01", "2024-03-05", 101)
        self.assertIsInstance(reservation, Reservation)

    def test_cancel_reservation_positive(self):
        reservation = self.valid_customer.create_reservation(self.hotel, "2024-03-01", "2024-03-05", 101)
        self.valid_customer.cancel_reservation(self.hotel, 101)
        self.assertEqual(len(self.valid_customer.reservations), 0)

    def test_display_reservations_positive(self):
        info = self.valid_customer.display_reservations()
        self.assertIsInstance(info, str)

    # Casos de prueba negativos

    def test_display_information_negative(self):
        # Intentamos mostrar la información de un cliente con valores nulos
        with self.assertRaises(ValueError):
            invalid_customer = Customer(None, None, None, None)

    def test_modify_information_negative(self):
        # Intentamos modificar la información de un cliente con valores nulos
        with self.assertRaises(ValueError):
            self.valid_customer.modify_information(name=None, email=None, address=None, phone=None)

    def test_display_reservations_negative(self):
        # Intentamos mostrar las reservas de un cliente sin reservas
        info = self.valid_customer.display_reservations()
        self.assertIsNotNone(info)
        self.assertIn("No Reservations Information", info) 


if __name__ == "__main__":
    unittest.main()
