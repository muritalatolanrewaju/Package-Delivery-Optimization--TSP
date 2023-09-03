# WGUPS Routing Program 

## Introduction

This project aims to solve a real-world problem using algorithms and data structures. Specifically, the task is to implement a routing program for the Western Governors University Parcel Service (WGUPS) to ensure that all packages are delivered on time while minimizing the distance traveled by the delivery trucks. This project can be a valuable addition to your portfolio and may also help you in technical interviews.

## Scenario

WGUPS is facing challenges in delivering packages on time. The Salt Lake City route has three trucks, two drivers, and an average of 40 packages to deliver daily. Each package has specific delivery requirements. The objective is to develop an algorithm and write code to ensure that all 40 packages are delivered on time while keeping the total distance traveled under 140 miles for two trucks.

## Assumptions

- Each truck can carry up to 16 packages.
- Trucks travel at an average speed of 18 mph.
- Three trucks and two drivers are available.
- Drivers leave the hub by 8:00 a.m.
- Delivery and loading times are instantaneous.
- The delivery address for package #9 will be corrected at 10:20 a.m.
- Distances are equal regardless of the direction traveled.
- The day ends when all 40 packages have been delivered.

## Requirements

- A. Develop a hash table for package information. [hash table](src/hash_table.py)

- B. Implement a look-up function for package details. [look-up function](src/package.py)

- C. Write the main program to deliver all packages. [main program](src/main.py)

- D. Provide an intuitive user interface. [User Interface](#user-interface)
  - [Package status between 8:35 a.m. and 9:25 a.m.](files/screenshot/package_status_at_specific_time_d1.png)
  - [Package status between 9:35 a.m. and 10:25 a.m.](files/screenshot/package_status_at_specific_time_d2.png)
  - [Package status between 12:03 p.m. and 1:12 p.m.](files/screenshot/package_status_at_specific_time_d3.png)

- E. Screenshots showing successful completion of the code. [Screenshots](files/screenshot/package_status_at_delivery_completion.png)

- F. Justify the package delivery algorithm used in the solution as written in the original program.

- G.  Describe what you would do differently, other than the two algorithms identified.

- H.  Verify that the data structure used in the solution meets all requirements in the scenario.


## Installation

1. Clone the repository

```commandline
git clone repo_url
```

2. Navigate to the project directory

```commandline
cd WGUPS-Routing-Program
```

3. Install the dependencies

- On Windows, download and install [Python 3.9.0](https://www.python.org/downloads/release/python-390/)

- On Mac, download and install [Python 3.9.0](https://www.python.org/downloads/release/python-390/)

- On Linux CLI, install Python 3.9.0

    ```bash
    sudo apt-get install python3.9.0
    ```


- Create a virtual environment

    ```commandline
    python -m venv venv
    ```

## Usage

Run the program

```commandline
python main.py
```

## User Interface

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
