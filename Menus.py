# Creating the Menu
class Menu:
  def __init__(self,name,items,start_time,end_time):
    self.name = name
    self.items = items
    self.start_time = start_time
    self.end_time = end_time

  def __repr__(self):
    return "{m} is available from {s} until {e}".format(m=self.name, s=self.start_time, e=self.end_time)

  def calculate_bill(self,purchased_items):
    total = 0
    for item in purchased_items:
      total += self.items[item]
    return total 

brunch = Menu("Brunch", {"Pancakes":7.50, "Waffles":9.00, "Burger":11.00,"Home Fries":4.50,"Coffee":1.50,"Tea":1.00,"Mimosa":10.50,"Orange Juice":3.50}, 1100, 1600)

early_bird = Menu("Early Bird",{'Salumeria Plate': 8.00, 'Salad and Breadsticks (Serves 2, No Refills)': 14.00, 'Pizza with Quattro Formaggi': 9.00, 'Duck Ragu': 17.50, 'Mushroom Ravioli (Vegan)': 13.50, 'Coffee': 1.50, 'Espresso': 3.00,}, 1500, 1800)

dinner = Menu("Dinner",{'Crostini with Eggplant Caponata': 13.00, 'Caesar Salad': 16.00, 'Pizza with Quattro Formaggi': 11.00, 'Duck Ragu': 19.50, 'Mushroom Ravioli (Vegan)': 13.50, 'Coffee': 2.00, 'Espresso': 3.00,}, 1700, 2300)

kids = Menu("Kids",{'Chicken Nuggets': 6.50, 'Fusilli with Wild Mushrooms': 12.00, 'Apple Juice': 3.00}, 1100, 2100)

print(brunch)
print("\n")

breakfast_order = ["Pancakes", "Home Fries", "Coffee"]
print(brunch.calculate_bill(breakfast_order))

early_bird_order = ["Salumeria Plate", "Mushroom Ravioli (Vegan)"]
print(early_bird.calculate_bill(early_bird_order))

# Creating the Franchises
class Franchise:
  def __init__(self, address, menus):
    self.address = address
    self.menus = menus

  def __repr__(self):
    return self.address

  def available_menus(self, time):
    menus = []
    for menu in self.menus:
      if time >= menu.start_time and time <= menu.end_time:
        menus.append(menu)
    return menus

menus = [brunch, early_bird, dinner, kids]

flagship_store = Franchise("1232 West End Road",menus)

new_installment = Franchise("12 East Mulberry Street",menus)

print(flagship_store.available_menus(1700))

franchises = [flagship_store, new_installment]

#Creating Businesses
class Business:
  def __init__(self, name, franchises):
    self.name = name
    self.franchises = franchises

basta_fazoolin = Business("Basta Fazoolin' with my Heart", franchises)

arepas_menu = Menu("Take a' Arepa", {'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50}, 1000, 2000)

arepas_place = Franchise("189 Fitzgerald Avenue", arepas_menu)

arepas_business = Business("Take a' Arepa", [arepas_place])

print(arepas_place)
