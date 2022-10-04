class Tab:
    menu = {
        'wine': 5,
        'beer': 3,
        'soft_drink': 2,
        'chicken': 10,
        'beef': 15,
        'veggie': 12,
        'desert': 6
    }

# Initialization function


def __init__(self):
    self.total = 0
    self.items = []


def add(self, item):
    self.items.append(item)
    self.total = self.total + self.menu[item]


def print_bill(self, tax, service):
    tax = (tax/100) * self.total
    service = (service/100) * self.total
    total = self.total + tax + service

    for item in self.items:
        print(f'{item:20} £{self.menu[item]}')

    print(f'{"Total"} £{total:.2f}')


# Code doesn't work. Getting ERROR:
# AttributeError: 'Tab' object has no attribute 'add'
# Indentention issues??
table1 = Tab()
table1.add('soft_drink')

print(table1.print_bill(10, 10))
