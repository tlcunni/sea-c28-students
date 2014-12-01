def fibonacci(n):
	"""Return "nth" value in the Fibonacci series"""
	a , b = 0,1
	for i in range(n):
		a, b = b, a+b
	print a

#fibonacci(9)

def lucas(n):
	"""Return "nth" value in the Lucas string"""
	a , b = 2, 1
	for i in range(n):
		a, b = b, a+b
	print a

#lucas(101)

def sum_series(n,a=0,b=1):
	for i in range(n):
		a, b = b, a+b
	print a

sum_series(9)
