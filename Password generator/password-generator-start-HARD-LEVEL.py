#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

#Letters
i = 0
y = []
while i < nr_letters:
	a = random.randint(0, len(letters)-1)
	x = letters[a]
	i += 1
	y.append(x)

#Numbers
i = 0
w = []
for x in numbers:
    a = random.randint(0, len(numbers)-1)
    x = numbers[a]
    i += 1
    w.append(x)

#Symbols
i = 0
z = []
for x in symbols:
    a = random.randint(0, len(symbols)-1)
    x = symbols[a]
    i += 1
    z.append(x)

password = []
password.extend(y)
password.extend(w)
password.extend(z)
password = set(password)
password = "".join(password)
print("Here is your password: " + password)