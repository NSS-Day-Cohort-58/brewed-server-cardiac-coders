from .employee_requests import get_single_employee
from .product_requests import get_single_product

ORDERS = [
    {
        "id": 1, "productId": 10, "employeeId": 5, "timestamp": 1613538111396
    }, {
        "id": 2, "productId": 5, "employeeId": 1, "timestamp": 1613038102396
    }, {
        "id": 3, "productId": 2, "employeeId": 7, "timestamp": 1612837112396
    }, {
        "id": 4, "productId": 8, "employeeId": 5, "timestamp": 1612836112396
    }, {
        "id": 5, "productId": 9, "employeeId": 7, "timestamp": 1612735112396
    }, {
        "id": 6, "productId": 4, "employeeId": 1, "timestamp": 1614528112396
    }, {
        "id": 7, "productId": 5, "employeeId": 8, "timestamp": 1614598112396
    }, {
        "id": 8, "productId": 2, "employeeId": 9, "timestamp": 1614630112396
    }, {
        "id": 9, "productId": 3, "employeeId": 2, "timestamp": 1612538112396
    }, {
        "id": 10, "productId": 9, "employeeId": 6, "timestamp": 1612438112396
    }, {
        "id": 11, "productId": 4, "employeeId": 1, "timestamp": 1612338112396
    }, {
        "id": 12, "productId": 6, "employeeId": 11, "timestamp": 1612238112396
    }, {
        "id": 13, "productId": 10, "employeeId": 8, "timestamp": 1630538112396
    }, {
        "id": 14, "productId": 9, "employeeId": 9, "timestamp": 1612738112396
    }, {
        "id": 15, "productId": 3, "employeeId": 3, "timestamp": 1612938112396
    }, {
        "id": 16, "productId": 4, "employeeId": 7, "timestamp": 1612638112396
    }, {
        "id": 17, "productId": 4, "employeeId": 10, "timestamp": 1612638112396
    }
]

def get_all_orders():
    return ORDERS

def get_single_order(id):

    requested_order = None

    for order in ORDERS:

        if order["id"] == id:
            requested_order = order
            matching_employee = get_single_employee(requested_order["employeeId"])
            requested_order["employee"] = matching_employee
            matching_product = get_single_product(requested_order["productId"])
            requested_order["product"] = matching_product
            requested_order.pop("employeeId", None)
            requested_order.pop("productId", None)
    return requested_order

def create_order(order):

    max_id = ORDERS[-1]["id"]
    new_id = max_id + 1
    order["id"] = new_id
    ORDERS.append(order)
    return order

def delete_order(id):

    order_index = -1
    for index, order in enumerate(ORDERS):
        if order["id"] == id:
            order_index = index

    if order_index >= 0:
        ORDERS.pop(order_index)

def update_order(id, new_order):

    for index, order in enumerate(ORDERS):
        if order["id"] == id:
            ORDERS[index] = new_order
            break