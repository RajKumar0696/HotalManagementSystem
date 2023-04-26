from employees import Employees
from customers import Customers
from menu import Menu
from orders import place_order, generate_order_bill


def actions():
    print("\n***********  Welcome To RHM Hotel  ***********")
    print("\t1) Add Employee")
    print("\t2) Add Customer")
    print("\t3) Show Menu Card")
    print("\t4) Add Menu Item")
    print("\t5) Place Order")
    print("\t6) Generate Bill")

    option = int(input("Select action:"))

    if option == 1:
        employee = Employees()
        employee.add_employee()
        print("Employee created successfully")
        employee.get_employee()

    elif option == 2:
        customer = Customers()
        customer.add_customer()
        print("Customer created successfully")
        customer.get_customer()

    elif option == 3:
        menu = Menu()
        menu.get_menu()

    elif option == 4:
        menu = Menu()
        menu.add_menu_item()

    elif option == 5:
        order_id = place_order()
        print("Order placed with id:", order_id)

    elif option == 6:
        generate_order_bill()


if __name__ == '__main__':
    choice = 'y'

    while choice == 'y':
        actions()
        choice = input("Do you want to continue?[y/n]:")
