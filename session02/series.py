#def fibonacci(n):
#	ranger = range(n)
#	for number in ranger:
#		print number + number-1

def fibonacci(n):
	a , b = 0,1
	while a<n:
		print a,
		a, b = b, a+b

fibonacci(101)

def lucas(n=2,m=1):
	range(n)