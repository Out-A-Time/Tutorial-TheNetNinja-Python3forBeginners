#SCOPING
my_name = 'Yoshi'

def print_name():
    global my_name
    my_name = 'Mario'
    print('Name inside the function:', my_name)

print('Name outside the function:', my_name)

print_name()  

print('Name outside the function after print():', my_name)

# Name outside the function: Yoshi
# Name inside the function: Mario
# Name outside the function after print(): Mario