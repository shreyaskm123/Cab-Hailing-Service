from collections import defaultdict
import math


class Location(object):
    """
    Creates a location objects with the given co-ordinates,
    Also updates it to new co-ordinates once moved to different position
    """

    def __init__(self, x, y):
        self.X_coordinate = x
        self.Y_coordinate = y

    def get_location(self):
        current_location = (self.X_coordinate, self.Y_coordinate)
        return current_location

    def update_location(self, new_x, new_y):
        self.X_coordinate = new_x
        self.Y_coordinate = new_y


class User(object):
    def __init__(self):
        """
        Store the users information with key as user_id and value as location object
        """
        self.all_users = defaultdict()

    def create_user(self, user_id, x_value, y_value):
        my_location = Location(x_value, y_value)
        self.all_users[user_id] = my_location

    def update_user_location(self, user_id, new_x, new_y):
        my_location = self.all_users[user_id]
        my_location.update_location(new_x, new_y)

    def get_current_user_location(self, user_id):
        location_details = self.all_users[user_id]
        user_location = (location_details.X_coordinate, location_details.Y_coordinate)
        return user_location


class CabDetails(object):
    def __init__(self, x_value, y_value):
        self.is_free = True
        self.cab_location = self.initialize_location(x_value, y_value)

    @staticmethod
    def initialize_location(x_value, y_value):
        cab_current_location = Location(x_value, y_value)
        return cab_current_location

    def get_cab_location(self):
        return self.cab_location.get_location()

    def update_cab_location(self, new_x, new_y):
        self.cab_location.update_location(new_x, new_y)

    def update_is_free(self, value):
        self.is_free = value


class Cab(object):
    def __init__(self):
        """
        Stores the cab information with key as cab_id and value as CabDetails object
        """
        self.all_cabs = defaultdict()
        self.available_cabs = []

    def create_cab(self, cab_id, x_value, y_value):
        cab_details = CabDetails(x_value, y_value)
        self.all_cabs[cab_id] = cab_details
        self.available_cabs.append(cab_id)

    def update_cab_location(self, cab_id, new_x, new_y):
        my_cab_details = self.all_cabs[cab_id]
        my_cab_details.update_cab_location(new_x, new_y)

    def update_is_free(self, cab_id, value):
        my_cab_details = self.all_cabs[cab_id]
        my_cab_details.update_is_free(value)

    def get_available_cabs(self):
        return self.available_cabs

    def get_cab_details(self, cab_id):
        return self.all_cabs[cab_id]

    def remove_cab_id_from_available_cabs(self, cab_id):
        self.available_cabs.remove(cab_id)


class UserCabManager(object):
    def __init__(self):
        self.my_user = User()
        self.my_cab = Cab()

    # This function can also be moved to an independent utility function
    @staticmethod
    def get_cartesian_distance(first_x, first_y, second_x, second_y):
        x_eval = pow((first_x - second_x), 2)
        y_eval = pow((first_y - second_y), 2)
        distance = math.sqrt(x_eval + y_eval)
        return distance

    def create_cabs_at_random_location(self, cab_id, x_value, y_value):
        self.my_cab.create_cab(cab_id, x_value, y_value)

    def create_users_at_random_location(self, user_id, x_value, y_value):
        self.my_user.create_user(user_id, x_value, y_value)

    def get_active_users(self):
        return self.my_user.all_users

    def get_active_cabs(self):
        return self.my_cab.all_cabs

    def get_nearest_cab(self, available_cabs, user_location):
        minimum_distance = float('inf')
        nearest_cab_id = None
        for i in range(len(available_cabs)):
            current_cab_id = available_cabs[i]
            cab_details = self.my_cab.get_cab_details(current_cab_id)
            cab_location = cab_details.get_cab_location()
            current_distance = self.get_cartesian_distance(user_location[0], user_location[1], cab_location[0],
                                                           cab_location[1])
            if current_distance < minimum_distance:
                minimum_distance = current_distance
                nearest_cab_id = current_cab_id

        return nearest_cab_id

    def update_details_for_cab(self, cab_id, destination_x, destination_y):
        """
        Following data has to be updated to successfully book a cab
        1. Remove the current cab_id from available_cabs list
        2. Update the current cab_id location to the destination location
        3. Update the is_free parameter in the CabDetails to False
        """

        self.my_cab.remove_cab_id_from_available_cabs(cab_id)
        self.my_cab.update_cab_location(cab_id, destination_x, destination_y)
        self.my_cab.update_is_free(cab_id, False)

    def book_my_cab(self, user_id, destination_x, destination_y):
        available_cabs = self.my_cab.get_available_cabs()
        current_user_location = self.my_user.get_current_user_location(user_id)
        cab_id = self.get_nearest_cab(available_cabs, current_user_location)
        if cab_id is None:
            print('Sorry! No cabs available for your current location')
            return
        self.update_details_for_cab(cab_id, destination_x, destination_y)
        return cab_id
