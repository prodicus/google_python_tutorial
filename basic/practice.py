a = [(2, 1), (3, 4, 2), (1, 0), (3, 4, -1)]
print sorted(a)

def Last() : 
	for i, c in enumerate(a):
		print c[-1]

print sorted(a, key = Last())