
def sum2k0n(lst,k):
	printed = []
	for num in lst:
		o = k - num
		if o in lst and o not in printed and num not in printed:
			printed.append(o)
			printed.append(num)
			print(num,o)
