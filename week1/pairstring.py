
import sys
s = sys.argv[1]

for i in range(len(s)):
	try:
		print(s[i] + s[i+1])
	except:
		continue