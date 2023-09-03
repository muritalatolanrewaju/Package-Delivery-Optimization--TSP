# Name: Muritala Olanrewaju
# Student ID: 010882332


# Import necessary modules and classes
import datetime
from file import File
from src import package_delivery
from src.distance import Distance
from src.package import Package
from src.package_delivery import PackageDelivery


# Function to load package data from a CSV file and return as a hash table
def load_package_data():
    package_data = File('../files/package/WGUPS_Package_File.csv')
    return package_data.parse_package_data()


# Function to load distance data from a CSV file and return as a list
def load_distance_table():
    distance_table = File('../files/package/WGUPS_Distance_Table.csv')
    raw_data = distance_table.parse_distance_data()
    return Distance(raw_data).clean_and_sort_data()


# Function to print text with ANSI color codes
def fancy_print(text, color_code):
    print(f"\033[{color_code}m{text}\033[0m")


# Function to add a package to the hash table
def add_package():
    try:
        # Collect package data from user
        package_id = int(input('Enter a package id:'))
        address = input('Street address:')
        city = input('City:')
        state = input('State:')
        zip_code = input('Zip code:')
        delivery_time = input('Delivery time:')
        weight = input('Weight:')
        status = input('Status:')
        notes = input('Notes:')

        # Create package object
        package = Package(str(package_id), address, city, state, zip_code, delivery_time, weight, status, notes)

        # Add package to hash table
        if package_hash_table.add(package_id, package):
            fancy_print('The following package has been created:\n', '92')
            fancy_print(package, '92')
            command_prompt()
        else:
            fancy_print('Please correct the issue and try again.', '91')
            command_prompt()
    except ValueError:
        fancy_print('ERROR: package id must be an integer.', '91')
        command_prompt()


# Function to inquire about a package
def inquire_package():
    try:
        package_id = int(input('Enter a package id:'))
        package = package_hash_table.get(package_id)
        if package:
            fancy_print(package, '92')
            command_prompt()
        else:
            fancy_print('Please correct the issue and try again.', '91')
            command_prompt()
    except ValueError:
        fancy_print('ERROR: package id must be an integer.', '91')
        command_prompt()


# Function to print package details at a specific time
def package_details_time():
    try:
        status = 't'
        package_id = int(input('Enter a package id:'))
        hour = int(input('Enter an hour between 1-24:'))
        minute = int(input('Enter a minute between 0-59:'))

        # Reload package and distance data
        new_package_hash_table = load_package_data()
        new_distance_data = load_distance_table()

        # Deliver packages and check status at specific time
        package_delivery.PackageDelivery.deliver_packages(new_package_hash_table, new_distance_data, status, hour,
                                                          minute,
                                                          package_id)
        command_prompt()
    except ValueError:
        fancy_print('ERROR: input must be an integer.', '91')
        command_prompt()


# Function to print all package details
def all_package_details():
    print("Printing all package details:")
    for i, pkg in enumerate(package_hash_table.list):
        if pkg:
            fancy_print(pkg, '92')
    command_prompt()


# Function to print all package info at a specific time
def all_package_info_time():
    try:
        status = 'ap'
        hour = int(input('Enter an hour between 1-24:'))
        minute = int(input('Enter a minute between 0-59:'))

        # Reload package and distance data
        new_package_hash_table = load_package_data()
        new_distance_data = load_distance_table()

        # Deliver packages and check status at specific time
        package_delivery.PackageDelivery.deliver_packages(new_package_hash_table, new_distance_data, status, hour,
                                                          minute)
        command_prompt()
    except ValueError:
        fancy_print('ERROR: input must be an integer.', '91')
        command_prompt()
    else:
        fancy_print('Please correct the issue and try again.', '91')
        command_prompt()


# Add this function to call the status check
def check_status_specific_time_t1():
    start_time = datetime.datetime(year=2023, month=9, day=2, hour=8, minute=35)
    end_time = datetime.datetime(year=2023, month=9, day=2, hour=9, minute=25)
    delivery.check_package_status_between_times(start_time, end_time)
    command_prompt()


# Add this function to call the status check for the morning time
def check_status_specific_time_t2():
    start_time = datetime.datetime(year=2023, month=9, day=2, hour=9, minute=35)
    end_time = datetime.datetime(year=2023, month=9, day=2, hour=10, minute=25)
    delivery.check_package_status_between_times(start_time, end_time)
    command_prompt()


# Add this function to call the status check for specific times
def check_status_specific_time_t3():
    start_time = datetime.datetime(year=2023, month=9, day=2, hour=12, minute=3)
    end_time = datetime.datetime(year=2023, month=9, day=2, hour=13, minute=12)
    delivery.check_package_status_between_times(start_time, end_time)
    command_prompt()


# Function to print the banner
def print_banner():
    fancy_print('++' + '=' * 52 + '++', '1;94')
    fancy_print('||' + ' ' * 4 + 'WESTERN GOVERNORS UNIVERSITY PARCEL SERVICE' + ' ' * 5 + '||', '1;30;44')
    fancy_print('||' + ' ' * 15 + 'COMMAND LINE INTERFACE' + ' ' * 15 + '||', '1;30;44')
    fancy_print('++' + '=' * 52 + '++', '1;94')


# Function to print the command menu
def print_command_menu():
    fancy_print('+' + '-' * 54 + '+', '94')
    fancy_print('|' + ' ' * 18 + '🛠️ COMMAND MENU 🛠️' + ' ' * 18 + '|', '30;47')
    fancy_print('+' + '-' * 54 + '+', '94')
    fancy_print('| a: Add a package                                     |', '93')
    fancy_print('| i: Package inquiry                                   |', '93')
    fancy_print('| t: Package details at a specific time                |', '93')
    fancy_print('| d: All package details                               |', '93')
    fancy_print('| ap: All package info at a specific time              |', '93')
    fancy_print('| t1: Status of all packages between 8:35-9:25 am      |', '93')
    fancy_print('| t2: Status of all packages between 9:35-10:25 am     |', '93')
    fancy_print('| t3: Status of all packages between 12:03-1:12 pm     |', '93')
    fancy_print('| q: Quit                                              |', '93')
    fancy_print('| h: Help                                              |', '93')
    fancy_print('+' + '-' * 54 + '+', '94')


# Function to handle user commands
def command_prompt():
    commands = {
        'a': add_package,
        'i': inquire_package,
        't': package_details_time,
        'd': all_package_details,
        'ap': all_package_info_time,
        't1': check_status_specific_time_t1,
        't2': check_status_specific_time_t2,
        't3': check_status_specific_time_t3
    }

    print_command_menu()
    fancy_print('|' + ' ' * 2 + 'Enter command:', '1;96')
    user_input = input().lower()

    if user_input in ('q', 'quit'):
        fancy_print('Thank you for using Western Governors University Parcel Service!', '92')
        exit()
    elif user_input in ('h', 'help'):
        command_prompt()
    elif user_input in commands:
        commands[user_input]()
    else:
        fancy_print('That command is not recognized, please try again.', '91')
        command_prompt()


# Main program execution begins here
print_banner()
package_hash_table = load_package_data()
distance_data = load_distance_table()
delivery = PackageDelivery(package_hash_table, distance_data)
delivery.deliver()
command_prompt()
