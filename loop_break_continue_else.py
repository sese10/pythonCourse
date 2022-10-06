print("Loop break continue else\n")
# use for loop to iterate from 0 to 10
# for each iteration print out "Number ", i
# if the i value is equal to 2 add the continue
# if the i value is equal to 8 add the break statement

number = 11
for i in range(number):
    print("for: Number:", i)
else:
    print("for: end of loop")

for i in range(number):
    if i == 2:
        continue
    print("for: Number:", i)

for i in range(number):
    if i == 8:
        break
    print("for: Number:", i)












"""
print("Break\n")

number = 5
for i in range(number):
    if i == 3:
        break
    print("for: Number:", i)

while number > 0:
    if number == 3:
        break
    print("while: Number:", number)
    number -= 1

print("\ncontinue\n")

number = 5
for i in range(number):
    if i == 3:
        continue
    print("for: Number:", i)

while number > 0:
    if number == 3:
        number -= 1
        continue
    print("while: Number:", number)
    number -= 1

print ("\nelse\n")

number = 5
for i in range(number):
    print("for: Number:", i)
else:
    print("for: end of loop")

while number > 0:
    print("while: Number:", number)
    number -= 1
else:
    print("while: end of loop")

print("\nelse, continue and break\n")

number = 5
for i in range(number):
    if i == 3:
        continue
    print("for: Number:", i)
else:
    print("for: end of loop")

while number > 0:
    if number == 3:
        number -= 1
        continue
    print("while: Number:", number)
    number -= 1
else:
    print("for: end of loop") """