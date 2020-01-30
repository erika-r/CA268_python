#
#   qsort code and a partition function.
#
#   Modify the qsort function so that it returns the maximum depth of recursion.
#
height = 0

def partition(lst, lo, hi): #height == 15
    global height 
    height += 1
    part = lo
    while lo < hi:
        while lst[lo] <= lst[part] and lo < hi:
            lo += 1
        while lst[hi] > lst[part]: # Don't have to check for hi >= 0 cos part is there as a sentinel.
            hi -= 1

        if lo < hi:
            # Swap the two entries
            lst[hi], lst[lo] = lst[lo], lst[hi]

    # Swap part into position
    if lst[part] > lst[hi]: # (this may happen of the array is small (size 2))
        lst[part], lst[hi] = lst[hi], lst[part]
        
    return hi

def rec_qsort(lst, lo, hi, rec=1): #height = 31
    global rec_lst
    if lo < hi:
        pivot = partition(lst, lo, hi)
        rec_qsort(lst, lo, pivot - 1,rec + 1)
        rec_qsort(lst, pivot + 1, hi,rec + 1)
        rec_lst.append(rec)

def qsort(lst): #always height = 1
    global rec_lst
    rec_lst =[]
    rec_qsort(lst, 0, len(lst) - 1)
    return max(rec_lst)
