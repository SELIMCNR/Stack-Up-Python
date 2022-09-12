letters = ["a", "b", "c", "d", "e"]

for letter in letters:
    print(letter)

numbers = [0, 1, 2, 3, 4]

for number in numbers:
    print(number)

numbers = range(10)
for number in numbers:
    print(number)

for number in range(9):
    print("Hello")

numbers = range(9)  # [0,.....,8]
for number in numbers:
    if number == 5:
        # continue breake pass
        print("The above let code pass")
    else:
        print(number)

# while True :
# code will continuously run

test = 0

while test < 9:
    print("Hello")
    test += 1  # adds 1 to test
