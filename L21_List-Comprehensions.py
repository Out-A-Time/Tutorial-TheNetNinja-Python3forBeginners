# Double prize money weekend bonanza
prizes = [5, 10, 50, 100, 1000]

double_prizes = []
# FOR LOOP
for prize in prizes:
    double_prizes.append(prize*2)
print(double_prizes)
#[10, 20, 100, 200, 2000]

# COMPREHENSION METHOD
double_prizes = [prize*2 for prize in prizes]
print(double_prizes)
#[10, 20, 100, 200, 2000]

# Squaring numbers
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

squared_even_nums = []
for num in nums:
    if num % 2 == 0:
        squared_even_nums.append(num ** 2)
print(squared_even_nums)
#[4, 16, 36, 64, 100]

# COMPREHENSION METHOD
squared_even_nums = [num ** 2 for num in nums if (num ** 2) % 2 == 0]
print(squared_even_nums)
#[4, 16, 36, 64, 100]
