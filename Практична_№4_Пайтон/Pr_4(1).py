class Product:
    def get_name(self):
        pass

class Salmon(Product):
    def get_name(self):
        return "Лосось"

class Caviar(Product):
    def get_name(self):
        return "Ікра"

class Nori(Product):
    def get_name(self):
        return "Норі"

class Crab(Product):
    def get_name(self):
        return "Краб"

class Rice(Product):
    def get_name(self):
        return "Рис"

class Tuna(Product):
    def get_name(self):
        return "Тунець"

class FirmoviHandler:
    def __init__(self, product):
        self.product = product

    def handle(self):
        return f"Продукт: {self.product.get_name()}"

class PhiladelphijaHandler:
    def __init__(self, product):
        self.product = product

    def handle(self):
        return f"Продукт: {self.product.get_name()}"

# Створення об'єктів для кожного класу
salmon = Salmon()
caviar = Caviar()
nori = Nori()
crab = Crab()
rice = Rice()
tuna = Tuna()

# Виклик обробників для класів "Фірмові" і "Філадельфія"
firmovi_handler = FirmoviHandler(salmon)
philadelphija_handler = PhiladelphijaHandler(caviar)

# Вивід повідомлень
print(firmovi_handler.handle())  # Повідомлення про назву продукту для "Фірмові"
print(philadelphija_handler.handle())  # Повідомлення про назву продукту для "Філадельфія"