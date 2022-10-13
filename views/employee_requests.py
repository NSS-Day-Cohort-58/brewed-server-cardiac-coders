
EMPLOYEES = [
    {
        id: 1,
        "name": "Alphonse Meron",
        "email": "ameron0@mashable.com",
        "hourlyRate": 11.50

    }, {
        id: 2,
        "name": "Damara Pentecust",
        "email": "dpentecust1@apache.org",
        "hourlyRate": 10.75

    }, {
        id: 3,
        "name": "Anna Bowton",
        "email": "abowton2@wisc.edu",
        "hourlyRate": 12.30

    }, {
        id: 4,
        "name": "Hunfredo Drynan",
        "email": "hdrynan3@bizjournals.com",
        "hourlyRate": 12.00

    }, {
        id: 5,
        "name": "Elmira Bick",
        "email": "ebick4@biblegateway.com",
        "hourlyRate": 12.30

    }, {
        id: 6,
        "name": "Bernie Dreger",
        "email": "bdreger5@zimbio.com",
        "hourlyRate": 11.50

    }, {
        id: 7,
        "name": "Rolando Gault",
        "email": "rgault6@google.com",
        "hourlyRate": 11.80

    }, {
        id: 8,
        "name": "Tiffanie Tubby",
        "email": "ttubby7@intel.com",
        "hourlyRate": 21.00

    }, {
        id: 9,
        "name": "Tomlin Cutill",
        "email": "tcutill8@marketwatch.com",
        "hourlyRate": 12.10

    }, {
        id: 10,
        "name": "Arv Biddle",
        "email": "abiddle9@cafepress.com",
        "hourlyRate": 13.00

    }
]


def get_all_employees():
    return EMPLOYEES


# Function with a single parameter


def get_single_employee(id):
    # Variable to hold the found animal, if it exists
    requested_employee = None

    #? Iterate the EMPLOYEES list above. Very similar to the
    #? for..of loops you used in JavaScript.
    for employee in EMPLOYEES:
        #? Dictionaries in Python use [] notation to find a key
        # instead of the dot notation that JavaScript used.
        if employee["id"] == id:
            requested_employee = employee

    return requested_employee


def create_employee(employee):
    # Get the id value of the last animal in the list
    max_id = EMPLOYEES[-1]["id"]

    # Add 1 to whatever that number is
    new_id = max_id + 1

    # Add an `id` property to the animal dictionary
    employee["id"] = new_id

    # Add the animal dictionary to the list
    EMPLOYEES.append(employee)

    # Return the dictionary with `id` property added
    return employee


def delete_employee(id):
    # Initial -1 value for animal index, in case one isn't found
    employee_index = -1

    # Iterate the ANIMALS list, but use enumerate() so that you
    # can access the index value of each item
    for index, employee in enumerate(EMPLOYEES):
        if employee["id"] == id:
            # Found the animal. Store the current index.
            employee_index = index

    # If the animal was found, use pop(int) to remove it from list
    if employee_index >= 0:
        EMPLOYEES.pop(employee_index)


def update_employee(id, updated_employee):
    # Iterate the ANIMALS list, but use enumerate() so that
    # you can access the index value of each item.
    for index, employee in enumerate(EMPLOYEES):
        if employee["id"] == id:
            # Found the animal. Update the value.
            EMPLOYEES[index] = updated_employee
            break
