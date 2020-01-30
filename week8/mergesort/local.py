
from queue import *
from student import *

q = Queue()
for num in [10,9,8,7]:
	q.enqueue(num)

q1,q2 = split(q)
print(q1,q2)