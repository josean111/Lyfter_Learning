# Cree una clase Product con:
# Nombre, precio y cantidad
# Cree una clase Inventory que:
# Guarde productos en una lista
# Tenga métodos para:
# Agregar un producto
# Mostrar todos los productos
# Calcular el valor total del inventario
# Ejemplo:
# Entrada:
# product1 = Product("Mouse", 5000, 3)
# product2 = Product("Teclado", 8000, 2)
# Salida:
# print(product.calculate_total_value_of_inventory) #34000

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

class Inventory:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def show_products(self):
        for product in self.products:
            print(f"\nProduct Name: {product.name}")
            print(f"Product Price: {product.price}")
            print(f"Product Quantity: {product.quantity}")

    def calculate_total_value_of_inventory(self):
        total = 0
        for product in self.products:
            total += product.price * product.quantity

        return total

def main():
    product1 = Product("Mouse", 5000, 3)
    product2 = Product("Teclado", 8000, 2)

    inventory = Inventory()
    inventory.add_product(product1)
    inventory.add_product(product2)
    inventory.show_products()
    print(f"\nInventory Total: {inventory.calculate_total_value_of_inventory()}")

if __name__ == "__main__":
    main()
