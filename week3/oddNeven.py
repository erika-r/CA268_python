
def get_both_lsts():
	import sys
	odd = ""
	even = ""
	for num in sys.stdin:
		num = int(num.strip())
		if num == -1:
			return "({}),({})".format(odd[:-1],even[:-1])
		elif num % 2 != 0:
			odd += str(num) + ","
		else:
			even += str(num) + ","
