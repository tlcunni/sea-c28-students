import string

rot13 = string.maketrans("ABCDEFGHIJKLMabcdefghijklmNOPQRSTUVWXYZnopqrstuvwxyz","NOPQRSTUVWXYZnopqrstuvwxyzABCDEFGHIJKLMabcdefghijklm")

def rottrans(code=None):
	if code is None:
	    code = raw_input("What would you like to translate?  ")
	return string.translate(code,rot13)

print rottrans()

print rottrans("Carly's Birthday")

if __name__ == '__main__':
	assert rottrans('the') == 'gur'
	print "test passed"
