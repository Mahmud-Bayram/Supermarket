from supermarket import *

while(True):
    reply = input("Are you worker or costumer?")
    if reply == "worker":
        password = input("Enter your password, please")
        if password == "wrk12":
            print("""------------------------------------------
            Welcome our supermarket app 

            In our app:

            1- Add product
            2- Search Product
            3- Delete product
            4- Raise price
            5- Change quantity
            6- Show expiration date
            7- Show products which has 

----------------------------------
            """)
            order = int(input("Select the number of the transaction you want to do"))
            if order == 1:
                product = input("Which is product?")
                price = input("How much?")
                quantity = input("How many is quantity?")
                expirationDate = input("What is expiration date?")
                product2 = superMarket(product, price, quantity, expirationDate)
                print(product2)
                orders.add_product(product2)
            elif order == 2:
                product = input("Which is product?")
                orders.search_Product(product)
            elif order == 3:
                product = input("Which is product?")
                orders.delete_product(product)
            elif order == 4:
                product = input("Which is product?")
                percent = int(input("What percent?"))
                orders.raise_price(product, percent)
            elif order == 5:
                product = input("Which is product?")
                quantity = int(input("How many is quantity?"))
                orders.change_quantity(product, quantity)
            elif order == 6:
                product = input("Which is product?")
                orders.show_expirationDate(product)
            elif order == 7:
                orders.hasProducts()
            else:
                print("There is no such transaction")
        else:
            print("Enter correct password, please")
    else:
        print("""------------------------------------------
                Welcome our supermarket app 

                In our app:

                1- Search Product
                2- Show expiration date
                3- Show products which has

-------------------------------
                """)
        order = int(input("Select the number of the transaction you want to do"))
        if order == 1:
            product = input("Which is product?")
            orders.search_Product(product)
        elif order == 2:
            product = input("Which is product?")
            orders.show_expirationDate(product)
        elif order == 3:
            orders.hasProducts()
















