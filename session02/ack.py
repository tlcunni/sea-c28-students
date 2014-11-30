#ack

def a(m,n):
	"""Return a value calculated with Ackerman's Function, m,n are non-negative integers"""
	if m<0 or n<0:
		return "None"
	if m == 0:
		return n + 1
	if n == 0:
		return a(m-1, 1)
	return a(m-1, a(m, n-1))

#if __name__ == __main__:
#	assert a(0,0) == 1
#	print "All tests passed"
#assert a(1,0) == 2
#assert a(2,0) == 3
#assert a(3,0) == 5
#assert a(0,1) == 2
#assert a(0,2) == 3
#assert a(0,3) == 4
#assert a(0,4) == 5
#assert a(1,1) == 3
#assert a(2,1) == 5
#assert a(3,1) == 13
#assert a(1,2) == 4z
#assert a(1,3) == 5
#assert a(1,4) == 6
#assert a(2,2) == 7
#assert a(3,2) == 29
#assert a(2,3) == 9
#assert a(2,4) == 11
#assert a(3,3) == 61
#assert a(3,4) == 125


print a(1,1)
