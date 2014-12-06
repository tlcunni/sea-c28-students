import string

rot13 = string.maketrans("ABCDEFGHIJKLMabcdefghijklmNOPQRSTUVWXYZnopqrstuvwxyz","NOPQRSTUVWXYZnopqrstuvwxyzABCDEFGHIJKLMabcdefghijklm")

def rottrans(x):
	code = raw_input("What would you like to translate?  ")
	print string.translate(code,rot13)

rottrans(1)