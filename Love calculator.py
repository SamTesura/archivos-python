while 1:
	# 🚨 Don't change the code below 👇
	print("Welcome to the Love Calculator! \n")
	name1 = input("What is your name? \n")
	# name2 = " "
	name2 = input("What is their name? \n")
	# 🚨 Don't change the code above 👆

	#Write your code below this line 👇

	name_lower = name1.lower() + name2.lower()

	lista1 = []
	lista2 = []

	for x in "true":
		lista = name_lower.count(x)
		lista1.append(lista)
	sum_true = sum(lista1)
	# print(sum_true)

	for x in "love":
		lista = name_lower.count(x)
		lista2.append(lista)
	sum_love = sum(lista2)
	# print(sum_love)

	true_love_str = str(sum_true) + str(sum_love)
	true_love_int = int(true_love_str)

	if true_love_int < 10 or true_love_int > 90 and true_love_int < 99:
		print(f"\n***************************\nYour score is {true_love_int}%, you go together like coke and mentos.\n***************************\n")
	elif true_love_int >=40 and true_love_int <= 50:
		print(f"\n***************************\nYour score is {true_love_int}%, you are alright together.\n***************************\n")
	elif true_love_int >= 100:
		print("\n***************************\nYour score is 100%, you rock together!\n***************************\n")
	else:
		print(f"\n***************************\nYour score is {true_love_int}%.\n***************************\n")



	'''
	t = name_lower.count("t")
	r = name_lower.count("r")
	u = name_lower.count("u")
	e = name_lower.count("e")

	l = name_lower.count("l")
	o = name_lower.count("o")
	v = name_lower.count("v")
	e = name_lower.count("e")

	true = t+r+u+e
	love = l+o+v+e

	true_love_str = str(true) + str(love)
	true_love_int = int(true_love_str)

	if true_love_int < 10 or true_love_int > 90 and true_love_int < 99:
		print(f"Your score is {true_love_int}%, you go together like coke and mentos.\n")
	elif true_love_int >=40 and true_love_int <= 50:
		print(f"Your score is {true_love_int}%, you are alright together.\n")
	elif true_love_int >= 100:
		print("Your score is 100%, you rock together!\n")
	else:
		print(f"Your score is {true_love_int}%.\n")
		'''