from queue import Queue

def split(q):
	q1 = Queue()
	q2 = Queue()
	ln = (len(q) // 2)
	#print(ln)
	i = 0
	while i < ln:
		q1.enqueue(q.dequeue())
		i += 1
	while not q.isempty():
		q2.enqueue(q.dequeue())
	return (q1,q2)


def merge(q1,q2,q):
	while not q1.isempty() and not q2.isempty():
			if q1.first() < q2.first():
				q.enqueue(q1.dequeue)
			else:
				q.enqueue(q2.dequeue())

	while not q2.isempty():
		q.enqueue(q2.dequeue())

	while not q1.isempty():
		q.enqueue(q1.dequeue())

	return q