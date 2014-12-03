#(!/usr/bin/env python)
#from__future__import print__function

FRUIT = [u'Apples', u'Pears',u'Oranges',u'Peaches']


for _ in FRUIT:
	print _

FRUIT.append((raw_input(u'Please add your favorite fruit-> ')))

for _ in FRUIT:
	print _

user_input = input(u'Please select number from 1 to 5 ->  ')

print user_input 
print FRUIT[(user_input-1)]

print ""
print ""

NEW_FRUIT = [u"Mango"]

FRUIT = NEW_FRUIT + FRUIT

for _ in FRUIT:
	print _

print ""
print ''



FRUIT.insert(0,u"Bananna")
	
for _ in FRUIT:
	print _
