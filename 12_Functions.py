#Function - generic construction
def greet1():
    print('hello world')

greet1()
#hello world

#Function with default parameters
def greet2(name='Stranger', time='evening'):
    print(f'Good {time} {name}, hope you are well')

greet2('Max', 'morning')
#Good morning Max, hope you are well
greet2()
#Good evening Stranger, hope you are well

#Function where function arguments are variables from inputs
def greet3(give_name, give_time):
    print(f'Good {give_time} {give_name} , hope you are well')

name = input('Enter your name:')
time = input('Enter the time of day:')

greet3(name, time)
#Good evening Yoshi, hope you are well



def circle_area1(radius):
    print(3.142 * radius * radius)

circle_area1(5)
#78.55


def circle_area2(radius):
    print(3.142 * radius * radius)

radius = int(input('Enter a radius: '))

circle_area2(radius)
#78.55

#HIGHER ORDER FUNCTION:
def circle_area3(radius):
    return 3.142 * radius * radius

def volume(area, length):
    print(area * length)


radius = int(input('Enter a cilinder radius: '))
length = int(input('Enter a cilinder length: '))

area_calc = circle_area3(radius)

volume(area_calc, length)