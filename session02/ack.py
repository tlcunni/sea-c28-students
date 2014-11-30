#ack

def a(m,n):
	"""Return a value calculated with Ackerman's Function"""
	if m == 0:
		return n + 1
	if n == 0:
		return a(m-1, 1)
	return a(m-1, a(m, n-1))

print a(3,4)
