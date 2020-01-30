
def maximum(l):
    if len(l) == 1:
        return l[0]		#BASECASE
    elif l[len(l) - 1] >= l[len(l) - 2]:
    	del l[len(l) - 2]
    elif l[len(l) - 1] <= l[len(l) - 2]:
    	del l[len(l) - 1]
    return maximum(l)