import unittest
from unittest import TestCase
from Cab_Hailing_service import UserCabManager


class TestCabHailingService(TestCase):
    def setUp(self) -> None:
        self.user_cab_manager = UserCabManager()

    def test_cab_manager(self):
        self.user_cab_manager.create_users_at_random_location(1, 0, 0)
        self.user_cab_manager.create_users_at_random_location(2, 1, 1)
        self.user_cab_manager.create_users_at_random_location(3, 6, 6)

        self.user_cab_manager.create_cabs_at_random_location(1, 0, 0)
        self.user_cab_manager.create_cabs_at_random_location(2, 0, 0)

        cab_id_mapping_first_user = self.user_cab_manager.book_my_cab(1, 5, 5)
        self.assertEqual(cab_id_mapping_first_user, 1)
        cab_id_mapping_second_user = self.user_cab_manager.book_my_cab(2, 3, 3)
        self.assertEqual(cab_id_mapping_second_user, 2)

        # Currently there are no cabs available , so it return None
        cab_id_mapping_third_user = self.user_cab_manager.book_my_cab(3,0,0)
        self.assertEqual(cab_id_mapping_third_user, None)

if __name__ == 'main':
    unittest.main()