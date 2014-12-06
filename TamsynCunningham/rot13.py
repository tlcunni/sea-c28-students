import string

rot13 = string.maketrans("ABCDEFGHIJKLMabcdefghijklmNOPQRSTUVWXYZnopqrstuvwxyz","NOPQRSTUVWXYZnopqrstuvwxyzABCDEFGHIJKLMabcdefghijklm")

def rottrans(code):
	code = raw_input("What would you like to translate?  ")
	print string.translate(raw_input(code,rot13)

print rottrans(bob)