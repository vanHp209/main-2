class Product:
    def __init__(self, height=160):  # параметр по умолчанию
        self.name = ("milk")
        self.price = (20)
        self.quatity= (5)
    def calculate_total_price(self,price =20,quatity=5):
        print(self.price * self.quatity)

name = Product('milk')
price = Product(20)
quatity= Product(5)
