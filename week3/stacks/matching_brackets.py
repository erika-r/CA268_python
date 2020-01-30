
from Stack import Stack

def match(s):
	stack = Stack()
	for letter in s:
		if letter == ")" and stack.is_empty():
			return False
		elif letter == "(":
			stack.push("(")
		elif letter == ")" and not stack.is_empty():
			stack.pop()
	return stack.is_empty()
	
	