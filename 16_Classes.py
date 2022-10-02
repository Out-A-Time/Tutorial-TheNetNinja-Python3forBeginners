name = 'Yoshi'
print(type(name))
age = 20
print(type(age))
nums = [1, 2, 3]
print(type(nums))

# <class 'str'>
# <class 'int'>
# <class 'list'>


class Planet:
    # Attributes
    def __init__(self):
        self.name = 'Hoth'
        self.radius = 200000
        self.gravity = 5.5
        self.system = 'Hoth System'

    # Method
    def orbit(self):
        return f'{self.name} is orbiting in the {self.system}'


hoth = Planet()
print(f'Name is: {hoth.name}')
print(f'Radius is: {hoth.radius}')
print(f'The gravity is: {hoth.gravity}')

print(hoth.orbit())

# Name is: Hoth
# Radius is: 200000
# The gravity is: 5.5
# Hoth is orbiting in the Hoth System
