# Name: Muritala Olanrewaju
# Student ID: 010882332

class Package:

    # A package that can be delivered.

    # Initialization
    def __init__(self, package_id='', address='', city='', state='',
                 zipcode='', delivery_time='', weight='', status='', notes=''):
        # Identification
        self.package_id = package_id

        # Location Information
        self.address = address
        self.city = city
        self.state = state
        self.zipcode = zipcode

        # Delivery Details
        self.delivery_time = delivery_time
        self.weight = weight
        self.status = status

        # Additional Information
        self.notes = notes

        # Load time
        self.load_time = None

    # Set the package's ID
    def set_id(self, package_id):
        self.package_id = package_id

    # Set the package's address
    def set_address(self, address):
        self.address = address

    # Set the package's city
    def set_city(self, city):
        self.city = city

    # Set the package's state
    def set_state(self, state):
        self.state = state

    # Set the package's zipcode
    def set_zipcode(self, zipcode):
        self.zipcode = zipcode

    # Set the package's delivery time
    def set_delivery_time(self, delivery_time):
        self.delivery_time = delivery_time

    # Set the package's status
    def set_status(self, status):
        self.status = status

    # Set the package's notes
    def set_notes(self, notes):
        self.notes = notes

    def set_load_time(self, load_time):
        self.load_time = load_time

    # Representation
    def __repr__(self):
        return (
            f"Package Info - "
            f"ID: {self.package_id}, "
            f"ADDRESS: {self.address}, "
            f"CITY: {self.city}, "
            f"STATE: {self.state}, "
            f"ZIP: {self.zipcode}, "
            f"DELIVERY TIME: {self.delivery_time}, "
            f"WEIGHT: {self.weight}, "
            f"STATUS: {self.status}, "
            f"NOTES: {self.notes},"
            f"LOAD TIME: {self.load_time}"
        )
