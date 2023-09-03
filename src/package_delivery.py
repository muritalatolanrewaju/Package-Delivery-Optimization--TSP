# Name: Muritala Olanrewaju
# Student ID: 010882332

# Import necessary modules and classes
from datetime import datetime, timedelta

from truck import Truck


# Print text with ANSI color codes.
def fancy_print(text, color_code):
    print(f"\033[{color_code}m{text}\033[0m")


# Function to optimize the delivery route using the 2-opt algorithm
def optimize(addresses_to_visit, distance_data):
    addresses_to_visit = ['HUB'] + addresses_to_visit + ['HUB']
    index = 2 if '4580 S 2300 E' in addresses_to_visit else 1
    optimal_route = addresses_to_visit
    optimal_cost = cost(optimal_route, distance_data)[0]

    # Initialize self-adjusting parameters
    exploration_threshold = 0.7  # Start with an exploration bias
    min_exploration_threshold = 0.3
    exploration_decrement = 0.05
    exploration_increment = 0.02

    while True:
        new_optimal_found = False
        for i in range(index, len(addresses_to_visit) - 1):
            for k in range(i + index, len(addresses_to_visit)):
                new_route = two_opt_swap(addresses_to_visit, i, k)
                new_cost = cost(new_route, distance_data)[0]
                if new_cost < optimal_cost:
                    optimal_route = new_route
                    optimal_cost = new_cost
                    new_optimal_found = True

                    # Adjust exploration threshold based on performance
                    if exploration_threshold > min_exploration_threshold:
                        exploration_threshold -= exploration_decrement
                else:
                    # Increase exploration threshold to encourage exploration
                    exploration_threshold += exploration_increment
        if not new_optimal_found:
            break
        addresses_to_visit = optimal_route

    return optimal_route


# Function to swap two addresses in the route for 2-opt optimization
def two_opt_swap(route, i, k):
    new_route = route.copy()
    new_route[i:k] = reversed(route[i:k])
    return new_route


# Calculate the time it takes to travel a mile.
def tick(mile, current_time):
    time_in_secs = (mile / 18) * 3600
    return current_time + timedelta(seconds=time_in_secs)


# Function to calculate the cost of a route in terms of distance
def cost(route, cost_data, current_time=None, pkg_data=None, check_time=0, package=None, pkg_search=False):
    distance_dict = {row[0]: {addr: float(dist) for addr, dist in row[1]} for row in cost_data}
    total_miles = 0

    for i in range(len(route) - 1):
        start_addr = route[i]
        end_addr = route[i + 1]
        total_miles += distance_dict[start_addr][end_addr]
        if current_time:
            current_time = tick(total_miles, current_time)
            if check_time and current_time >= check_time:
                if pkg_search:
                    return find_pkg_status(package, check_time, pkg_data)
                return True
            if pkg_data:
                update_pkg_status(end_addr, pkg_data, current_time)

    if check_time and pkg_search:
        return find_pkg_status(package, check_time, pkg_data)
    elif check_time:
        return False
    return [total_miles, current_time]


# Function to update the status of a package after delivery
def update_pkg_status(address, pkg_data, time):
    for _, pkg in pkg_data:
        if pkg.address == address:
            pkg.set_status(f'Delivered at {time.time()}')


# Function to find the status of a specific package
def find_pkg_status(package, check_time, pkg_data):
    for _, pkg in pkg_data:
        if pkg.pkg.package_id == package.pkg.package_id:
            print(f'\nAt {check_time.time()}\n\n{package}')
            return True
    return False


# Main class for PackageDelivery class
class PackageDelivery:

    # Function to perform the actual delivery
    def deliver_packages(self, distance_data, status, hour, minute, package_id=0):
        delivery = PackageDelivery(self, distance_data)

        # Load trucks and calculate optimal routes
        delivery.load_trucks()

        # Perform the actual delivery
        delivery.deliver(status, hour, minute, package_id)

    # Initialize PackageDelivery object with package and distance data
    def __init__(self, package_data, distance_data):
        self.package_data = package_data
        self.distance_data = distance_data

        # Get the current date and time
        current_datetime = datetime.now()

        # Set the date to the current date and specific times
        self.truck_times = [
            datetime(year=current_datetime.year, month=current_datetime.month, day=2, hour=8,
                     minute=35),
            datetime(year=current_datetime.year, month=current_datetime.month, day=2, hour=9,
                     minute=35),
            datetime(year=current_datetime.year, month=current_datetime.month, day=2, hour=12,
                     minute=3)
        ]

        self.trucks = [Truck() for _ in range(3)]
        self.addresses_to_visit = [[] for _ in range(3)]
        self.best_routes = []

    # Load trucks
    def load_trucks(self):
        for i, truck in enumerate(self.trucks[:2]):
            load_truck(truck, self.package_data, self.addresses_to_visit[i], i + 1, self.truck_times[i])

        # Update package 9 details before loading truck 3
        self.package_data.get(9).set_address('410 S State St')
        self.package_data.get(9).set_city('Salt Lake City')
        self.package_data.get(9).set_zipcode('84111')
        load_truck(self.trucks[2], self.package_data, self.addresses_to_visit[2], 3, self.truck_times[2])

        self.best_routes = [optimize(address, self.distance_data) for address in self.addresses_to_visit]

    # Deliver packages
    def deliver(self, status='normal', hour=0, minute=0, pkg_id=0):
        self.load_trucks()

        if status == 'normal':
            miles = [cost(route, self.distance_data, self.truck_times[i], truck.packages)
                     for i, (route, truck) in enumerate(zip(self.best_routes, self.trucks))]
            self.print_delivery_details(miles)

        elif status == 'ap':
            self.print_status_at_time(hour, minute)

        else:
            self.print_specific_package_status(hour, minute, pkg_id)

    # Print delivery details
    def print_delivery_details(self, miles):
        boundary_length = 54
        fancy_print('+' + '-' * boundary_length + '+', '1;92')

        # Center-align the title
        title = '🚚 Delivery Details 🚚'
        title_padding = ((boundary_length - len(title)) // 2)
        fancy_print('|' + ' ' * title_padding + title + ' ' * (boundary_length - title_padding - len(title) - 2) + '|',
                    '1;30;106')

        fancy_print('+' + '-' * boundary_length + '+', '1;92')

        for i, (mile, truck_time) in enumerate(zip(miles, self.truck_times)):
            fancy_print('|' + '-' * boundary_length + '|', '1;93')

            # Left-align the details
            line1 = f'Truck {i + 1} Delivered all its packages in {mile[0]:.2f} miles'
            line2 = f'Truck {i + 1} left the HUB at: {truck_time.time()}'
            line3 = f'Truck {i + 1} returned to the HUB at: {mile[1].time()}'

            fancy_print('|' + line1 + ' ' * (boundary_length - len(line1)) + '|', '1;94')
            fancy_print('|' + line2 + ' ' * (boundary_length - len(line2)) + '|', '1;94')
            fancy_print('|' + line3 + ' ' * (boundary_length - len(line3)) + '|', '1;94')

        fancy_print('|' + '-' * boundary_length + '|', '1;93')

        fancy_print('+' + '=' * boundary_length + '+', '1;94')

        # Center-align the total mileage
        total_mileage = f"Total Mileage: {sum(mile[0] for mile in miles):.2f}"
        total_mileage_padding = (boundary_length - len(total_mileage)) // 2
        fancy_print('|' + ' ' * total_mileage_padding + total_mileage + ' ' * (
                boundary_length - total_mileage_padding - len(total_mileage)) + '|', '1;30;44')

        fancy_print('+' + '-' * boundary_length + '+', '1;94')

    # Function to print the status of all packages at a specific time
    def print_status_at_time(self, hour, minute):
        time_to_check = datetime(year=2023, month=9, day=2, hour=hour, minute=minute)
        if hour < 1 or hour > 24 or minute < 0 or minute > 59:
            print('Time is out of range')
            return

        if time_to_check < self.truck_times[0]:
            self.print_packages_status(time_to_check)
            return

        for i, (route, truck_time, truck) in enumerate(zip(self.best_routes, self.truck_times, self.trucks)):
            if cost(route, self.distance_data, truck_time, truck.packages, time_to_check):
                self.print_packages_status(time_to_check)
                return

    # Print packages status
    def print_packages_status(self, time_to_check):
        print('Here is the status of all packages at', time_to_check.time(), '\n')
        for pkg in self.package_data.list:
            if pkg is not None:
                fancy_print(pkg[1], '92')

    # Function to print the status of a specific package at a specific time
    def print_specific_package_status(self, hour, minute, pkg_id):
        time_to_check = datetime(year=2023, month=9, day=2, hour=hour, minute=minute)
        package = self.package_data.get(pkg_id)
        if not package:
            return

        if time_to_check < self.truck_times[0]:
            print('No packages have been delivered or loaded yet. Try a time after 8:00 am.')
            print('Here is the package requested before it has left the HUB')
            print(package)
            return

        for i, (route, truck_time, truck) in enumerate(zip(self.best_routes, self.truck_times, self.trucks)):
            if cost(route, self.distance_data, truck_time, truck.packages, time_to_check, package, True):
                return

    # Function to check the status of all packages between two times
    def check_package_status_between_times(self, start_time, end_time):
        fancy_print(
            '|' + ' ' * 59 + f"STATUS OF ALL PACKAGES LOADED ONTO EACH TRUCK BETWEEN {start_time.time()} AND {end_time.time()}" + ' ' * 59 + '|',
            '30;44')

        for i, truck in enumerate(self.trucks):
            truck_leave_time = self.truck_times[i]
            fancy_print(
                '|' + ' ' * 20 + f"🚚 🚚  🚚   🚚    🚚     🚚      🚚       🚚        🚚         🚚 TRUCK {i + 1}          🚚         🚚        🚚       🚚      🚚     🚚    🚚   🚚  🚚 🚚" + ' ' * 20 + '|',
                '30;106')

            if truck_leave_time <= start_time:
                self.update_status_for_departed_truck(truck, start_time, end_time, i)
            else:
                self.update_status_for_hub_truck(truck)

    @staticmethod
    def print_package_info(pkg):
        fancy_print(
            f"Package Info - ID: {pkg[1].package_id}, ADDRESS: {pkg[1].address}, CITY: {pkg[1].city}, "
            f"STATE: {pkg[1].state}, ZIPCODE: {pkg[1].zipcode}, DELIVERY TIME: {pkg[1].delivery_time}, "
            f"WEIGHT: {pkg[1].weight}, STATUS: {pkg[1].status}, NOTES: {pkg[1].notes}, LOAD TIME: {pkg[1].load_time}",
            '92')

    def update_status_for_departed_truck(self, truck, start_time, end_time, truck_index):
        current_time = self.truck_times[truck_index]
        for pkg in truck.packages:
            delivery_time = cost([pkg[1].address, 'HUB'], self.distance_data, current_time)[1]

            if delivery_time <= end_time:
                pkg[1].status = f"Delivered at {delivery_time.time()}"
            else:
                pkg[1].status = "En route"

            self.print_package_info(pkg)
            current_time = delivery_time

    def update_status_for_hub_truck(self, truck):
        for pkg in truck.packages:
            pkg[1].status = "At HUB"
            self.print_package_info(pkg)


# Load a truck
def load_truck(truck, package_data, addresses_to_visit, truck_number, truck_start_time):
    """
    Load packages into the truck based on constraints and truck number.
    """
    count = 0
    truck_empty = True

    while truck_empty:
        for i in range(len(package_data.list)):
            pkg_data = package_data.list[i]
            if not pkg_data:
                continue

            pkg_id, pkg = pkg_data
            if truck.has_package(pkg) or pkg.status != 'At HUB':
                continue

                # Add this condition to ensure package 19 is loaded onto truck 1
            if pkg_id == 19 and truck_number == 1:
                load_package_to_truck(truck, pkg_data, addresses_to_visit,
                                      'At the HUB, it will be loaded ON TRUCK ONE', truck_start_time)
                continue

            if truck_number == 1 and should_load_truck_one(pkg, pkg_id, count, addresses_to_visit):
                load_package_to_truck(truck, pkg_data, addresses_to_visit,
                                      'At the HUB, it will be loaded  ON TRUCK ONE', truck_start_time)

            elif truck_number == 2 and should_load_truck_two(pkg, count, addresses_to_visit):
                load_package_to_truck(truck, pkg_data, addresses_to_visit,
                                      'At the HUB, it will be loaded  ON TRUCK TWO', truck_start_time)
            elif truck_number == 3 and count < 1:
                if pkg_id != 19:
                    load_package_to_truck(truck, pkg_data, addresses_to_visit, 'At the HUB, it will be loaded  ON TRUCK'
                                                                               'THREE', truck_start_time)

            if truck.package_count() == truck.capacity:
                truck_empty = False
                break

        count += 1
        if truck_number == 3 or count > 3:
            truck_empty = False

    return truck, addresses_to_visit


# Check if a package should be loaded on truck one
def should_load_truck_one(pkg, pkg_id, count, addresses_to_visit):
    if pkg.delivery_time == '9:00 AM':
        return True
    if pkg.address == '177 W Price Ave' and pkg.delivery_time == 'EOD':
        return True
    if pkg.address == '380 W 2880 S' and pkg.delivery_time == 'EOD':
        return False

    if count >= 1 and (pkg_id in [13, 14, 15, 16, 19, 20] or (
            pkg.delivery_time != 'EOD' and 'Delayed' not in pkg.notes and 'Wrong' not in pkg.notes)):
        return True
    if (count >= 2 and 'Delayed' not in pkg.notes and
            pkg.notes != 'Can only be on truck 2' and
            pkg.address in addresses_to_visit and
            'Wrong' not in pkg.notes):
        return True
    if count >= 3 and pkg.notes != 'Can only be on truck 2' and 'Delayed' not in pkg.notes and 'Wrong' not in pkg.notes:
        return True
    return False


# Check if a package should be loaded on truck two
def should_load_truck_two(pkg, count, addresses_to_visit):
    is_special_note = pkg.notes == 'Can only be on truck 2'
    is_address_in_list = pkg.address in addresses_to_visit
    is_wrong_address = 'Wrong' not in pkg.notes
    is_not_special_address = pkg.address != '2530 S 500 E'
    is_delayed = 'Delayed' in pkg.notes

    if is_special_note and is_not_special_address:
        return True
    if count >= 1 and is_address_in_list and is_not_special_address and is_wrong_address:
        return True
    if count >= 2 and (is_delayed or is_address_in_list) and is_not_special_address and is_wrong_address:
        return True
    return False


# Load a package to a truck
def load_package_to_truck(truck, pkg_data, addresses_to_visit, status, truck_start_time):
    truck.add_package(pkg_data)
    load_time = truck_start_time.strftime("%H:%M:%S")  # Use the truck's start time
    pkg_data[1].set_load_time(load_time)  # Set the load time
    pkg_data[1].set_status(status)  # Update the delivery status
    pkg_data[1].set_status(f"{status} at {load_time}")  # Update the status to include the load time
    if pkg_data[1].address not in addresses_to_visit:
        addresses_to_visit.append(pkg_data[1].address)  # Add the address to the list of addresses to visit
