
def radix_sort(lst,times):
   # for each power of two (starting at lowest) sort based on that power
   for p in range(times):  # Assume 6 bits
      # Split list in two
      lo = [x for x in lst if x & (1 << p) == 0] # lo where the bit is zero
      hi = [x for x in lst if x & (1 << p) != 0] # hi where the bit is one
      lst = lo + hi # combine the two into one list.
   return lst