
def rpal(s):
	if len(s) == 1:
		return True
	elif s[0] == s[-1]:
		s = s[1:-1]
		return rpal(s)
	elif s[0] != s[-1]:
		return False