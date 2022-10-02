# Sorting List of numbers (Array)
nums = [1, 3, 4, 4, 2, 5, 8, 9, 4, 1]
print(sorted(nums))
#[1, 1, 2, 3, 4, 4, 4, 5, 8, 9]

# Sorting List of strings (capital letters go first!)
names = ['Mario', 'Luigi', 'marco', 'Yoshi', 'bowser', 'Ann', 'tom']
print(sorted(names))
#['Ann', 'Luigi', 'Mario', 'Yoshi', 'bowser', 'marco', 'tom']

# Set is like sorting, but takes all duplicates out
print(set(nums))
#{1, 2, 3, 4, 5, 8, 9}

# Set is like sorting, but takes all duplicates out
# it messing up with the string order!!!
print(set(names))
#{'Mario', 'Yoshi', 'marco', 'Ann', 'bowser', 'Luigi', 'tom'}

# Set with Dictionaries (Objects) to remove duplicated values
ninjas = {'Mario': 'black', 'Luigi': 'green',
          'Yoshi': 'black', 'Bowser': 'white'}
print(ninjas.values())
#dict_values(['black', 'green', 'black', 'white'])

print(set(ninjas.values()))
#{'green', 'black', 'white'}


# Function example of Set (removing duplicates)
# when looping through Dictionary (Objects)
def belt_count(dictionary):
    belts = list(dictionary.values())
    for belt in set(belts):
        num = belts.count(belt)
        print(f'There are {num} {belt} belts')


belt_count(ninjas)
# There are 2 black belts
# There are 1 white belts
# There are 1 green belts
