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

brunch = Menu("Brunch", {"Pancakes":7.50, "Waffles":9.00, "Burger":11.00,"Home Fries":4.50,"Coffee":1.50,"Tea":1.00,"Mimosa":10.50,"Orange Juice":3.50}, "11:00 AM", "4:00 PM")

early_bird = Menu("Early Bird",{'Salumeria Plate': 8.00, 'Salad and Breadsticks (Serves 2, No Refills)': 14.00, 'Pizza with Quattro Formaggi': 9.00, 'Duck Ragu': 17.50, 'Mushroom Ravioli (Vegan)': 13.50, 'Coffee': 1.50, 'Espresso': 3.00,}, "3:00 PM", "6:00 PM")

dinner = Menu("Dinner",{'Crostini with Eggplant Caponata': 13.00, 'Caesar Salad': 16.00, 'Pizza with Quattro Formaggi': 11.00, 'Duck Ragu': 19.50, 'Mushroom Ravioli (Vegan)': 13.50, 'Coffee': 2.00, 'Espresso': 3.00,}, "5:00 PM", "11:00 PM")

kids = Menu("Kids",{'Chicken Nuggets': 6.50, 'Fusilli with Wild Mushrooms': 12.00, 'Apple Juice': 3.00}, "11:00 AM", "9:00 PM")

print(brunch)
print("\n")

breakfast_order = ["Pancakes", "Home Fries", "Coffee"]
print(brunch.calculate_bill(breakfast_order))

early_bird_order = ["Salumeria Plate", "Mushroom Ravioli (Vegan)"]
print(early_bird.calculate_bill(early_bird_order))


