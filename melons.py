class SuperMelon(object):

    def get_base_price(self):
        return 5.00

    def get_price(self, qty):
        total = self.get_base_price() * qty

        if self.imported == True:
            total = total * 1.5 
            return total

        if self.shape == "square":
            total = total * 2
            return total

        if self.name == "Cantaloupe":
            total = 0.50 * total
            return total

        if self.name == "Watermelon":
            total = 0.75 * total
            return total

    def __init__(self):
        if type(self) == SuperMelon:
            raise Exception("You cannot create an instance of this class")

class Cantaloupe(SuperMelon):
    name =  "Cantaloupe"
    color = "tan"
    shape = "natural"
    imported = False
    seasons = ['Spring', 'Summer']


class Watermelon(SuperMelon):
    name =  "Watermelon"
    color = "Green"
    shape = "natural"
    imported = False
    seasons = ['Fall', 'Summer']

    def get_price(self, qty):
        if qty >= 3:
            return 0.75 *(qty * self.get_base_price())
        else:
            return qty * self.get_base_price()

class Casaba(SuperMelon):
    name =  "Casaba"
    color = "green"
    shape = "natural"
    imported = True
    seasons = ['Spring', 'Summer', 'Fall', 'Winter']

    def get_price(self, qty):
        return 1.5 * (qty*(self.get_base_price() + 1))


class Sharlyn(SuperMelon):
    name =  "Sharlyn"
    color = "tan"
    shape = "natural"
    imported = True
    seasons = ['Summer']

    def get_price(self, qty):
        return 1.5 * (qty * self.get_base_price())

class SantaClaus(SuperMelon):
    name =  'Santa Claus'
    color = 'green'
    shape = 'natural'
    imported = True
    seasons = ['Winter', 'Spring']
    def get_price(self, qty):
        return 1.5 * (qty * self.get_base_price())

class Christmas(SuperMelon):
    name =  'Christmas'
    color = 'green'
    shape = 'natural'
    imported = False
    seasons = ['Winter']
    def get_price(self, qty):
        return (qty * self.get_base_price())

class HornedMelon(SuperMelon):
    name =  'Horned Melon'
    color = 'yellow'
    shape = 'natural'
    imported = True
    seasons = ['Summer']

    def get_price(self, qty):
        return 1.5(qty * self.get_base_price())

class Xigua(SuperMelon):
    name =  'Xigua'
    color = 'black'
    shape = 'square'
    imported = True
    seasons = ['Summer']

    def get_price(self, qty):
        return 2(qty * self.get_base_price())

class Ogen(SuperMelon):
    name =  'Ogen'
    color = 'tan'
    shape = 'natural'
    imported = False
    seasons = ['Spring', 'Summer']

    def get_price(self, qty):
        return 1.5(qty * (self.get_base_price() + 1))

