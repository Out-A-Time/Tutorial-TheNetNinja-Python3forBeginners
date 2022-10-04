class Planet:
    # Class Attributes
    shape = 'round'

    # Instance Attributes
    def __init__(self, name, radius, gravity, system):
        self.name = name
        self.radius = radius
        self.gravity = gravity
        self.system = system

    # Method (has access to instance level attributes)
    def orbit(self):
        return f'{self.name} is orbiting in the {self.system}'

    # Class Method (has access to class level attributes)
    @classmethod
    def commons(cls):
        return f'All planets are {cls.shape} because of gravity'

    @staticmethod  # with default value speed
    def spin(speed='2000 miles per hour'):
        return f'The planet spins and spins at {speed}'


# Print Instance attributes
naboo = Planet('Naboo', 300000, 8, 'Naboo System')
print(f'Name: {naboo.name}')
print(f'Radius: {naboo.radius}')
print(f'Gravity: {naboo.gravity}')
print(naboo.orbit())
# Print Class attributes
print(Planet.shape)
print(naboo.shape)
print(Planet.commons())
print(naboo.commons())
#Print @staticmethod
print(Planet.spin())
print(naboo.spin('a very high speed'))

# Name: Naboo
# Radius: 300000
# Gravity: 8
# Naboo is orbiting in the Naboo System
# round
# round
# All planets are round because of gravity
# All planets are round because of gravity
# The planet spins and spins at 2000 miles per hour
# The planet spins and spins at a very high speed
