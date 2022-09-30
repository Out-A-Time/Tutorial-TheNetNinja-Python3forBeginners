#WHILE LOOP

age = 25
num = 0
# while loop generic
# prints all number from 0 to 24
while num < age:
    print(num)
    num = num + 1

# 0
# 1
# 2
# ...
# 23
# 24

#while loop with if statement
#(prints only even numbers)
while num < age:
    if num % 2 == 0:
        print(num)
    num = num + 1

# 0
# 2
# 4
#...
# 22
# 24

#while loop with if statement
#prints only even number not larger than 10
while num < age:
    if num % 2 == 0:
        print(num)
    if num > 10:
        break
    num = num + 1

# 0
# 2
# 4
# 6
# 8
# 10

#while loop with if statements, continue and break
while num < age:
    if num == 0:
        num = num + 1
        continue
    if num % 2 == 0:
        print(num)
    if num > 10:
        break
    num = num + 1

# 2
# 4
# 6
# 8
# 10