import unittest
from unittest import TestCase
from Cab_Hailing_service import UserCabManager


class TestCabHailingService(TestCase):
    def setUp(self) -> None:
        self.user_cab_manager = UserCabManager()

        # Creation of 6 users at random location
        self.user_cab_manager.create_users_at_random_location(1, 0, 0)
        self.user_cab_manager.create_users_at_random_location(2, 0, 2)
        self.user_cab_manager.create_users_at_random_location(3, 2, 0)
        self.user_cab_manager.create_users_at_random_location(4, 2, 2)
        self.user_cab_manager.create_users_at_random_location(5, 3, 3)
        self.user_cab_manager.create_users_at_random_location(6, 3, 2)

        # Creation of 5 cabs at random location
        self.user_cab_manager.create_cabs_at_random_location(1, 0, 0)
        self.user_cab_manager.create_cabs_at_random_location(2, 1, 0)
        self.user_cab_manager.create_cabs_at_random_location(3, 0, 1)
        self.user_cab_manager.create_cabs_at_random_location(4, 2, 1)
        self.user_cab_manager.create_cabs_at_random_location(5, 2, 2)

    def test_cab_manager(self):
        cab_id_mapping_first_user = self.user_cab_manager.book_my_cab(1, 5, 5)
        self.assertEqual(cab_id_mapping_first_user, 1)

        cab_id_mapping_second_user = self.user_cab_manager.book_my_cab(2, 0, 0)
        self.assertEqual(cab_id_mapping_second_user, 3)

        cab_id_mapping_third_user = self.user_cab_manager.book_my_cab(3, 0, 0)
        self.assertEqual(cab_id_mapping_third_user, 2)

        cab_id_mapping_fourth_user = self.user_cab_manager.book_my_cab(4, 0, 0)
        self.assertEqual(cab_id_mapping_fourth_user, 5)

        cab_id_mapping_fifth_user = self.user_cab_manager.book_my_cab(5, 0, 0)
        self.assertEqual(cab_id_mapping_fifth_user, 4)

        # Currently there are no cabs available , so it return None
        cab_id_mapping_sixth_user = self.user_cab_manager.book_my_cab(6, 2, 2)
        self.assertEqual(cab_id_mapping_sixth_user, None)

    def test_user_cab_details(self):
        active_users = len(self.user_cab_manager.get_active_users())
        self.assertEqual(active_users, 6)

        active_cabs = len(self.user_cab_manager.get_active_cabs())
        self.assertEqual(active_cabs, 5)


if __name__ == 'main':
    unittest.main()