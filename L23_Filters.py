grades = ['A', 'B', 'C', 'F', 'F', 'A']


def remove_fails(grade):
    return grade != 'F'


# FOR LOOP
filtered_grades = []
for grade in grades:
    if grade != 'F':
        filtered_grades.append(grade)
print(filtered_grades)
#['A', 'B', 'C', 'A']

# COMPREHENSION METHOD
filtered_grades = [grade for grade in grades if grade != 'F']
print(filtered_grades)
#['A', 'B', 'C', 'A']

# FILTER
filtered_grades = list(filter(remove_fails, grades))
print(filtered_grades)
#['A', 'B', 'C', 'A']
