
def get_odd_list():
	import sys
	odd = []
	for num in sys.stdin:
		num = int(num.strip())
		if num == -1:
			return odd
		elif num % 2 != 0:
			odd.append(num)
