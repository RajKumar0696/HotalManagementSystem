from menu import Menu
from customers import Customers, check_and_add_customer


def get_orderid():
    Orders.lats_order_id += 1
    return Orders.lats_order_id


def place_order():
    menu = Menu()
    menu.get_menu()
    item_number = int(input("Select your item from menu:"))
    customer_id = check_and_add_customer()
    employee_id = int(input("Select employee to server order:"))
    order = Orders(item_number, customer_id, employee_id)
    Customers.customer_order_map[customer_id] = order.id
    return order.id


def generate_order_bill():
    customer_id = int(input("Enter your customer Id:"))
    if customer_id in Customers.customer_order_map:
        order_id = Customers.customer_order_map[customer_id]
        order_details = Orders.orders_dict[order_id]
        menu = Menu()
        item = list(Menu.menuItems)[order_details.item_number - 1]
        amount = Menu.menuItems[item]
        print("Your bill amount: ", amount, "/-")
        print("Thank you !!! visit again :)")
    else:
        print("Sorry, no orders found for you")


class Orders:
    orders_dict = {}  # {order_id : ord_obj}
    lats_order_id = 0

    def __init__(self, item_number, customer_id, employee_id):
        self.id = Orders.lats_order_id + 1
        Orders.lats_order_id += 1
        self.customer_id = customer_id
        self.employee_id = employee_id
        self.item_number = item_number
        Orders.orders_dict[self.id] = self
