
print("Enter a name and number, or a name and ? to query (!! to exit)")

dct = {}

n = input()
while n != "!!":
	n = n.split()
	if n[1].isdigit():
		dct[n[0]] = n[1]
	elif n[1] == "?":
		if n[0] in dct:
			print("{} has number {}".format(n[0], dct[n[0]]))
		elif n[0] not in dct:
			print("Sorry, there is no {}".format(n[0]))
	n = input()

if n == "!!":
	print("Bye")