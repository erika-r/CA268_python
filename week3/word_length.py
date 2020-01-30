
def get_counts_dict(lst):
	dct = {}
	for word in lst:
		if word in dct:
			dct[word] += 1
		elif word not in dct:
			dct[word] = 1
	return dct
