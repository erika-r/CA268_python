
import sys

file1 = sys.argv[1]
file2 = sys.argv[2]

with open(file1,'r') as f1:
	con1 = [name.strip() for name in f1.readlines()]


with open(file2,'r') as f2:
	con2 = [name.strip() for name in f2.readlines()]

same = [name for name in con2 if name in con1]

for i in range(1,len(same) + 1):
	print(str(i) + '. ' + same[i - 1])
