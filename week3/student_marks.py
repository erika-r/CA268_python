
def make_map():
	dct = {}
	n = input().strip().split()
	while n:
		dct[n[0]] = n[1]
		n = input().strip().split()
	return dct

