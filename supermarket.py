import  sqlite3, time

class superMarket:
    def __init__(self, productName, expirationDate, price, quantity):
        self.productName = productName
        self.expirationDate = expirationDate
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return "Product name: {}\nPrice: {}\nQuantity: {}\nexpirationDate: {}\n".format(self.productName, self.price, self.quantity, self.expirationDate)

class orders:
    def __init__(self):
        self.form_connection()

    def form_connection(self):
        self.connect = sqlite3.connect("supermarket.db")
        self.c = self.connect.cursor()
        self.c.execute("Create Table If not exists products('Products_name TEXT', 'Prices INT', 'Quantities INT', 'Expiration_dates TEXT')")
        self.connect.commit()

    def breaked_connection(self):
        self.connect.close()

    def hasProducts(self):
        self.c.execute("Select * From products")
        products = self.c.fetchall()
        if(len(products) == 0):
            print("Can't find any product")
        else:
            for i in products:
                product = superMarket(i[0]," ", i[1]," ", i[2], " ", i[3])
                print(product)

    def add_product(self, product):
        self.c.executemany("Insert into products Values(?,?,?,?)", product)
        self.connect.commit()

    def search_Product(self, product):
        self.c.execute("Select * From products Where productName = (?)", product)
        product = self.c.fetchall()
        if (product == null):
            print("There is no such product")
        else:
            product2 = superMarket(product[0], product[1], product[2], product[3])
            print(product2)
        self.connect.commit()

    def delete_product(self, product):
        self.c.execute("Delete From products Where productName = (?)", product)
        self.connect.commit()

    def raise_price(self, product, percent):
        self.c.execute("Select * From products Where productName = (?)", product)
        price = self.c.fetchall()[1]
        if (price == null):
            print("There is no such product")
        else:
            price = price + (price/100) * percent
            self.c.execute("Update superMarket.db Set price = (?) Where product = (?)", price, product)
        self.connect.commit()

    def change_quantity(self, product, quantity):
        self.c.execute("Select * From products")
        productName = self.c.fetchall()[0][0]
        if productName == null:
            print("There is no such product")
        else:
            self.c.execute("Update superMarket.db Set quantity = (?) Where product = (?)", quantity, product)
        self.connect.commit()

    def show_expirationDate(self, product):
        self.c.execute("Select * From products")
        productName = self.c.fetchall()[0][0]
        if productName == null:
            print("There is no such product")
        else:
            self.c.execute("Select * From products Where product = (?)", product)
            expirationDate = self.c.fetchall()[3]
            print(expirationDate)
        self.connect.commit()


class Costumer(orders):
    pass