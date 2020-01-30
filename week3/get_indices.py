
def get_indices(lst):
	a = [0 for i in range(9)]
	for word in lst:
		l = len(word)
		a[l] += 1
	return a
