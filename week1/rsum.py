
def sumto(a,b):
	if a == b:
		return 0
	else:
		a = a + sumto((a+1),b)
		return a
		print(a)