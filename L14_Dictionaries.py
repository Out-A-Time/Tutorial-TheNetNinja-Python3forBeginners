#Dictionaries are like Objects in JS
ninja_belts = {"Mario": "red", "Luigi": "black"}

print(ninja_belts["Mario"])
print(ninja_belts["Luigi"])

#red
#black

#Displays as boolean if key exists inside key-value pairs collection
print("Yoshi" in ninja_belts)
print("Mario" in ninja_belts)
#False
#True

#Displays all existing keys (from key-value pairs)
print(ninja_belts.keys())
#dict_keys(['Mario', 'Luigi'])

#Keys displayed as Lists (Arrays)
print(list(ninja_belts.keys()))
#['Mario', 'Luigi']

#Displays all values from key-value pairs collection
print(ninja_belts.values())
#dict_values(['red', 'black'])

#Display all values, stored as variable
vals = list(ninja_belts.values())
print(vals)
#['red', 'black']

#Display how many instances of specific value exists
print(vals.count('black'))
print(vals.count('red'))
print(vals.count('blue'))
#1
#1
#0

#Adding new key-value pair
ninja_belts['Yoshi'] = 'red'
print(ninja_belts)
#{'Mario': 'red', 'Luigi': 'black', 'Yoshi': 'red'}

#Creating dictinary (Object) and assigning to variable
person = dict(name= 'shaun', age= 27, height= "6ft")
print(person)

#{'name': 'shaun', 'age': 27, 'height': '6ft'}

#Function with adding key-value pairs
def ninja_intro(dictionary):
    for key, val in dictionary.items():
        print(f'I am {key} and I am a {val} belt')

ninja_belts = {}

while True:
    ninja_name = input('Enter a ninja name: ')
    ninja_belt = input('Enter a belt colour: ')
    ninja_belts[ninja_name] = ninja_belt

    add_another = input('Add another ninja? (y/n)')
    if add_another == 'y':
        continue
    else:
        break

ninja_intro(ninja_belts)

#I am Max and I am a black belt