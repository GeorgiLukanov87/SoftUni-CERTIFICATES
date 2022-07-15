class Catalogue:

    def __init__(self, name: str):
        self.name = name
        self.products = []

    def add_product(self, product_name: str):
        self.products.append(product_name)

    def get_by_letter(self, first_letter: str):
        by_letter = []
        for letter in self.products:
            if letter[0] == first_letter:
                by_letter.append(letter)
        return by_letter

    def __repr__(self):
        sorted_products = sorted(self.products)
        result2 = '\n'.join(sorted_products)
        return f"Items in the {self.name} catalogue:{result2}"


catalogue = Catalogue("Furniture")
catalogue.add_product("Sofa")
catalogue.add_product("Mirror")
catalogue.add_product("Desk")
catalogue.add_product("Chair")
catalogue.add_product("Carpet")
print(catalogue.get_by_letter("C"))
print(catalogue)
