class CoffeeShop:
    """My Coffee Shop"""

    def __init__(self, name, coffee_type, size, price):
        self.name = name
        self.coffee_type = coffee_type
        self.size = size
        self.price = price

    def show_info_user(self):
        """Show user info"""
        message = f"Hello | Name: {self.name} | Coffee type: {self.coffee_type} | Size: {self.size} | Price: {self.price}"
        print(message.title())

    def show_list(self):
        message1 = "Espresso small medium large price 2$"
        print(message1.title())
        message2 = "Latte small medium large price 10$"
        print(message2.title())
        message3 = "Americano small medium large price 20$"
        print(message3.title())

    def pricee(self, price_coffee):
        self.price_coffee = price_coffee
        if price_coffee == "small":
            print(
                f"Your coffee {self.coffee_type} | {self.size} {self.price_coffee}\n")
        elif price_coffee == "medium":
            print(
                f"Your coffee {self.coffee_type} | {self.size} {self.price_coffee}\n")
        elif price_coffee == "large":
            print(
                f"Your coffee {self.coffee_type} | {self.size} {self.price_coffee}\n")


flag = True
while flag:
    name_user = input("Your name: ".title())
    coffee_type = input("Your coffee type: ".title())
    size_user_coffee = input("Your coffee size: ".title())

    list_user_coffee = CoffeeShop(
        name=name_user, coffee_type=coffee_type, size=size_user_coffee, price="")
    list_user_coffee.show_list()
    list_user_coffee.show_info_user()

    message = input("Confirm? (yes/no): ".title())
    if message.lower() == 'no':
        flag = False
        msg = "Your order has been placed 🟩"
        print(msg.title())
    else:
        flag = True
