# Parent class1

class Item():
    def __init__(self,sku):
        self.sku = sku

    def print_sku(self):
        print("The sku is {}.".format(self.sku))
# Parent class2
class Garment():
    def __init__(self, section, type):
        self.section = section
        self.type = type

    def print_garment(self):
        print("The garment is in section {} and is a {}.".format(self.section, self.type))

# Child class
class Shirt(Item, Garment):
    def __init__(self, sku, section, type, name, color):
        Item.__init__(self, sku)
        Garment.__init__(self, section, type)
        self.color = color
        self.name = name

Blouse = Shirt("0001", "Tops", "Blouse", "Silk Blouse", "White")
Blouse.print_sku()
Blouse.print_garment()
print("The {} is {}.".format(Blouse.name, Blouse.color))