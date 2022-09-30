#FOR LOOP with Range
#prints number from range 0 to 5 (5 not included!)
for n in range(5):
    print(n)

# 0
# 1
# 2
# 3
# 4

#prints numbers from range 2 to 5 (5 not included!)
for n in range(2,5):
    print(n)

# 2
# 3
# 4

#prints numbers from range 1 to 20 (20 not included) with step 4
for n in range(1, 20, 4):
    print(n)

# 1
# 5
# 9
# 13
# 17

#print list of burgers at the specific position in the list
burgers = ['beef', 'chicken', 'veg', 'supreme', 'double']
for n in range(len(burgers)):
    print(n, burgers[n])

# 0 beef
# 1 chicken
# 2 veg
# 3 supreme
# 4 double

#print list of burgers in reverse order
#could be used also: for n in range(- 1, -1, -1):
for n in range(len(burgers) - 1, -1, -1):
    print(n, burgers[n])

# 4 double
# 3 supreme
# 2 veg
# 1 chicken
# 0 beef