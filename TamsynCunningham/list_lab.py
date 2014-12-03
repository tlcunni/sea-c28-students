#(!/usr/bin/env python)
#from__future__import print__function

FRUIT = [u'Apples', u'Pears',u'Oranges',u'Peaches']

print FRUIT

FRUIT.append((raw_input(u'Please add your favorite fruit-> ')))

print FRUIT

user_input = input(u'Please select number from 1 to 5 ->  ')

print user_input 
print FRUIT[(user_input-1)]

NEW_FRUIT = [u"Mango"]

FRUIT = NEW_FRUIT + FRUIT

print FRUIT

FRUIT.insert(0,u"Bananna")

print FRUIT
