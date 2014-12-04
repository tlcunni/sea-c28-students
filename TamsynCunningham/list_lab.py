#!/usr/bin/env python
#from__future__import print__function

FRUIT = [u'Apples', u'Pears',u'Oranges',u'Peaches']
#create base fruit list

for _ in FRUIT:
	print _

FRUIT.append((raw_input(u'Please add your favorite fruit-> ')))
#add additional user defined fruit

for _ in FRUIT:
	print _

user_input = input(u'Please select number from 1 to 5 ->  ')
#display user seleted fruit and user's selection

print user_input 
print FRUIT[(user_input-1)]

print ""
print ""

NEW_FRUIT = [u"Mango"]

FRUIT = NEW_FRUIT + FRUIT
#add additional fruit to list

for _ in FRUIT:
	print _

print ""
print ''


FRUIT.insert(0,u"Bananna")
#add more fruit

for _ in FRUIT:
	print _

print ""
print ""

for i in FRUIT:
	if 'P' == i[0]:
		print i
	if 'p' == i[0]:
		print i
#display just the fruits that start with p

print ''
print ''

for _ in FRUIT:
	print _

print ""
print ""

FRUIT.pop(-1)

for _ in FRUIT:
	print _

USERCUT = raw_input("Please select a fruit to remove ->  ")

if USERCUT not in FRUIT:
	USERCUT = raw_input("Please select fruit from list to remove  ")

if USERCUT in FRUIT:
	FRUIT.remove(USERCUT)

#FRUIT.remove(raw_input("Please select a fruit to remove ->  "))
#remove fruit based on user input, will break if they do it wrong, can fix later

for _ in FRUIT:
	print _

print ''
print ''

for i in FRUIT[:]:
	question = "Do you like %s   " %i
	answer = raw_input(question) 
	while answer != "yes" and answer != "no":
		print "Please answer yes or no"
		answer = raw_input(question)
	if answer == "yes":
		pass
	if answer == "no":
		FRUIT.remove(i)
		continue
	else:
		answer = raw_input("Please answer yes or no  ")
		continue

for _ in FRUIT:
	print _


