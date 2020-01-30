
def sum_to_k(lst,k):
	ptd = []
	for num in lst:
		n = k - num
		if n in lst and n not in ptd and num not in ptd:
			ptd.append(n)
			ptd.append(num)
			print(num, n)