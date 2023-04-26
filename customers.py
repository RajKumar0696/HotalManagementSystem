def check_and_add_customer():
    is_existing_customer = input("Do you have customer Id? [y/n]:")
    if is_existing_customer == 'y':
        return input("Enter your customer Id: ")
    else:
        customer = Customers()
        customer.add_customer()
        print("Customer added with ", customer.id)
        return customer.id


class Customers:
    customer_order_map = {}  # {customer_id : order_id}
    customer_id = 0

    def __init__(self):
        self.id = None
        self.name = None

    def add_customer(self):
        self.name = input("Enter Customer Name:")
        self.id = Customers.customer_id + 1
        Customers.customer_id += 1

    def get_customer(self):
        print("Name:", self.name)
        print("Id:", self.id)
