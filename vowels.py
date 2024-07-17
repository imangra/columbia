 #%%
for number in range(1, 11):
    print(number)

names = ["Ian", "Hadeel", "Narendra"]

for name in names:
    print(f"Hello, {name}")

numbers = [1, 2, 3, 4, 5]

total = 0
for num in numbers:
    total += num

print(f"Sum: {total}")

original_str = "basketball"

reversed_str = ""
for char in original_str:
    reversed_str = char + reversed_str

print(reversed_str)

input_str = "soccer"

frequency = {}
for char in input_str:
    if char in frequency:
        frequency[char] += 1
    else:
        frequency[char] = 1

for char, count in frequency.items():
    print(f"{char}: {count}")

students = {
    "Ian": 99,
    "Jalen": 55,
    "Tanner": 59,
    "Alew": 70
}

passing_grade = 60

for student, grade in students.items():
    if grade >= passing_grade:
        print(f"{student}: {grade}")

n = 5

for i in range(1, 11):
    print(f"{n} x {i} = {n * i}")

# %%
num = 1
while num <= 10:
    print(num)
    num += 1

while True:
    name = input("Enter a name (enter 'quit' to exit): ")
    if name.lower() == 'quit':
        break
    print(f"Hello, {name}")
        

# %%
num = int(input("Enter a number: "))

if num % 2 == 0:
    print(f"{num} is even.")
else:
    print(f"{num} is odd.")

import random

numbers = [random.randint(1, 100) for _ in range(10)]

smallest = numbers[0]
largest = numbers[0]

for num in numbers:
    if num < smallest:
        smallest = num
    elif num > largest:
        largest = num

print("List of numbers:", numbers)
print("Smallest number:", smallest)
print("Largest number:", largest)

fruit_store = {
    "apple": 2,
    "grape": 1,
    "clementine": 3,
    "orange": 2,
    "strawberry": 4}

fruit_name = input("Enter a fruit name: ")

if fruit_name in fruit_store:
    print(f"The price of {fruit_name} is ${fruit_store[fruit_name]:.2f}")
else:
    print("Sorry, we don't have that fruit.")
# %%
