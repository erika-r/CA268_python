
def print_queue(q,front,back):
	lst = []
	while front != back:
		lst.append(q[front])
		front = (front + 1) % len(q)	#used to reset index to 0
	return lst

