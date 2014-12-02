def fibonacci(n):
	"""Return "nth" value in the Fibonacci series"""
	a , b = 0,1
	for i in range(n):
		a, b = b, a+b
	return a

#print fibonacci(9)

def lucas(n):
	"""Return "nth" value in the Lucas string"""
	a , b = 2, 1
	for i in range(n):
		a, b = b, a+b
	return a

#print lucas(9)

def sum_series(n,a=0,b=1):
	"""Return "nth" value using formula similar to Fibonacci series, beginning with value "a" and "b" """
	for i in range(n):
		a, b = b, a+b
	return a

#print sum_series(9)
#print sum_series(9,2,1)



if __name__ == '__main__':
    assert (fibonacci(9)) == 34
    assert lucas(9) == 76
    assert sum_series(9) == 34
    assert sum_series(9,2,1) == 76
    print "All Tests passed"