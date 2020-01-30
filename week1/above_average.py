
def calc_average(lst):
	sm = sum(lst) / len(lst)
	return sm

def above_average(lst):
	av = calc_average(lst)
	abv = []
	for num in lst:
		if num > av:
			abv.append(num)
	print(abv)