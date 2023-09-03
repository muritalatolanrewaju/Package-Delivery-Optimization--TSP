# Name: Muritala Olanrewaju
# Student ID: 010882332

class Truck:
    """A truck that can carry packages and deliver them."""

    # Initialization
    def __init__(self):
        self._packages = []
        self.speed = 18
        self.miles = 0
        self.capacity = 16
        self.status = 'At HUB'

    # Checks if the truck has a package
    def has_package(self, package):
        return package in self._packages

    # Add a package to the truck
    def add_package(self, package):
        if len(self._packages) < self.capacity:
            self._packages.append(package)
        else:
            raise ValueError("Truck is at full capacity!")

    # Returns the number of packages on the truck
    def package_count(self):
        return len(self._packages)

    # Remove a package from the truck
    def remove_package(self, package):
        if package in self._packages:
            self._packages.remove(package)
        else:
            raise ValueError("Package not found in the truck!")

    # Add miles to the truck's total mileage
    def add_miles(self, miles):
        if miles > 0:
            self.miles += miles
        else:
            raise ValueError("Miles should be a positive value!")

    # Set the truck's status
    def set_status(self, new_status):
        """Sets the status of the truck."""
        self.status = new_status

    # Get the truck's status
    @property
    def packages(self):
        return self._packages
