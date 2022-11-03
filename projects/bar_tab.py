class Tab:

  menu = {
    'wine': 5,
    'beer': 3,
    'soft-drink': 2,
    'chicken': 10,
    'beef': 15,
    'veggie': 12,
    'dessert': 6
  }

def __init__(self):
  self.total = 0
  self.items = []

def add(self, item):
  self.items.append(item)
  self.totatl += self.menu(item)

def print_bill(self, tax, service):
  tax = (tax/100) * self.total
  service = (service/100)*self.total
  total = self.total + tax + service

  for item in self.items:
    print(f'{item}${self.menu[item]}')

  print(f'{"Total"}${total:.2f}')
  print(f'{"Service charge":20} ${tax:2f}')
  print(f'{"Total":20} ${total:.2f}')