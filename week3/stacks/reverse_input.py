
from Stack import Stack

def reverse_input(stack):
	n = input()
	while n:
		stack.push(n)
		try:
			n = input()
		except:
			break
	while not stack.is_empty():
		print(stack.pop())