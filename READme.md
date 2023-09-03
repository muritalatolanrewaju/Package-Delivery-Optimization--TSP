# Package Delivery Optimization using TSP (Traveling Salesman Problem)

## Overview
This project aims to solve a real-world package delivery problem using the Traveling Salesman Problem (TSP) as a basis. The goal is to optimize the delivery routes for a truck fleet to minimize the distance traveled while meeting various constraints such as delivery time windows, truck capacities, and special package requirements.

## Features
- **Route Optimization:** Utilizes the 2-opt algorithm to find the most efficient route for each truck.
- **Time Complexity:** Efficiently calculates the time taken for each route and updates package statuses in real-time.
- **Dynamic Loading:** Packages are dynamically loaded onto trucks based on various constraints.
- **User Interface:** Provides a colorful terminal interface to display package statuses and delivery details.
- **Time-based Queries:** Allows users to query the status of all packages at a specific time or within a time range.
- **Package-specific Queries:** Allows users to query the status of a specific package at a specific time.

## Project Assumptions
- Each truck can carry up to 16 packages.
- Trucks travel at an average speed of 18 mph.
- Three trucks and two drivers are available.
- Drivers leave the hub by 8:00 a.m.
- Delivery and loading times are instantaneous.
- The delivery address for package #9 will be corrected at 10:20 a.m.
- Distances are equal regardless of the direction traveled.
- The day ends when all 40 packages have been delivered.

## Dependencies
- Python 3.x

## How to Run
- Clone the repository.
- Navigate to the project directory.
- Run python main.py to start the program.

## User Command Line Interface

```commandline
++====================================================++
||    WESTERN GOVERNORS UNIVERSITY PARCEL SERVICE     ||
||               COMMAND LINE INTERFACE               ||
++====================================================++
+------------------------------------------------------+
|                 🚚 Delivery Details 🚚              |
+------------------------------------------------------+
|------------------------------------------------------|
|Truck 1 Delivered all its packages in 31.20 miles     |
|Truck 1 left the HUB at: 08:35:00                     |
|Truck 1 returned to the HUB at: 21:22:40              |
|------------------------------------------------------|
|Truck 2 Delivered all its packages in 33.10 miles     |
|Truck 2 left the HUB at: 09:35:00                     |
|Truck 2 returned to the HUB at: 18:31:40              |
|------------------------------------------------------|
|Truck 3 Delivered all its packages in 44.70 miles     |
|Truck 3 left the HUB at: 12:03:00                     |
|Truck 3 returned to the HUB at: 08:20:40              |
|------------------------------------------------------|
+======================================================+
|                Total Mileage: 109.00                 |
+------------------------------------------------------+
+------------------------------------------------------+
|                  🛠️ COMMAND MENU 🛠️                 |
+------------------------------------------------------+
| a: Add a package                                     |
| i: Package inquiry                                   |
| t: Package details at a specific time                |
| d: All package details                               |
| ap: All package info at a specific time              |
| t1: Status of all packages between 8:35-9:25 am      |
| t2: Status of all packages between 9:35-10:25 am     |
| t3: Status of all packages between 12:03-1:12 pm     |
| q: Quit                                              |
| h: Help                                              |
+------------------------------------------------------+
|  Enter command:
```

## Code Structure
- **`fancy_print(text, color_code):`** Prints text with ANSI color codes.
- **`optimize(addresses_to_visit, distance_data):`** Optimizes the delivery route using the 2-opt algorithm.
- **`two_opt_swap(route, i, k):`** Swaps two addresses in the route for optimization.
- **`tick(mile, current_time):`** Calculates the time it takes to travel a mile.
- **`cost(route, cost_data, ...):`** Calculates the cost of a route in terms of distance.
- **`update_pkg_status(address, pkg_data, time):`** Updates the status of a package after delivery.
- **`find_pkg_status(package, check_time, pkg_data):`** Finds the status of a specific package.
- **`PackageDelivery`**: Main class for package delivery.
- **`__init__(self, package_data, distance_data):`** Initializes the object.
- **`load_trucks(self):`** Loads trucks with packages.
- **`deliver(self, status, ...):`** Performs the actual delivery.
- **`print_delivery_details(self, miles):`** Prints delivery details.
- **`print_status_at_time(self, hour, minute):`** Prints package statuses at a specific time.
- **`print_specific_package_status(self, hour, minute, pkg_id):`** Prints the status of a specific package.
- **`check_package_status_between_times(self, start_time, end_time):`** Checks the status of all packages between two times.

## Contributing
Feel free to fork the project and submit a pull request with your changes!

## License
This project is licensed under the GNU License.
