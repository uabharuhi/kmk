cnt = 0
def g1(i):
	global cnt
	print(i)
	for j in range(i,i+10):
		yield g2(10*i+j)
		cnt = cnt+1

	if cnt <30:
		yield g1(i+1)

def g2(j):
	return j

for i in g1(4):
	print(i)