
def set_stuff(s1,s2):
	return (tuple(s1.union(s2)), s1.issubset(s2), s1.issuperset(s2))