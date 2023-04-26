class Menu:
    menuItems = {
        'Chicken Biryani': 150,
        'Mutton Biryani': 200,
        'Starter': 100,
        'Meals': 100,
        'Sprite': 20
    }

    def get_menu(self):
        print("********* Menu Items *********")
        count = 1
        for name, price in Menu.menuItems.items():
            print(count, ")", name, ":", price, "/-")
            count += 1

    def add_menu_item(self):
        new_item_name = input("Enter item name:")
        new_item_price = int(input("Enter item price:"))
        if new_item_name not in Menu.menuItems:
            Menu.menuItems[new_item_name] = new_item_price
            self.get_menu()
        else:
            print("Oops!!!, Item already exist")
