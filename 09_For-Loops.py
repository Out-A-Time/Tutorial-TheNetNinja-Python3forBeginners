#FOR LOOP
ninjas = ["Ryu", "Yoshi", "Mario", "Bowser"]
#for loop - generic
for ninja in ninjas:
    print(ninja)

# Ryu
# Yoshi
# Mario
# Bowser

#for loop with slice
for ninja in ninjas[1:3]:
    print(ninja)

# Yoshi
# Mario

#for loop with if statement
for ninja in ninjas:
    if ninja == "Mario":
        print(f'{ninja} - black belt')
    else:
        print(ninja)

# Ryu
# Yoshi
# Mario - black belt
# Bowser

#for loop with if statement and break
for ninja in ninjas:
    if ninja == "Mario":
        print(f'{ninja} - black belt')
        break
    else:
        print(ninja)

# Ryu
# Yoshi
# Mario - black belt