a, b = int(raw_input()), raw_input()
if a>3:
	c = '-'.join([b[i-1:i+1] for i in range(1,a,2)])
	if (a%2): c += b[a-1]	
	print c
else: 
	print b 
