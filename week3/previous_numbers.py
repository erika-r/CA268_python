
def prev_num():
	import sys
	prev = []
	prnt = []
	for num in sys.stdin:
		num = int(num.strip())
		if num == -1:
			return prnt
		elif num not in prev:
			prev.append(num)
		elif num in prev and num not in prnt:
			prnt.append(num)

