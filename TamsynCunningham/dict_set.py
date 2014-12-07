tester = {'name': 'Chris' , 'city': 'Seattle' , 'cake': 'Chocolate'}

print tester

tester.pop('cake')

print tester

tester.setdefault('fruit','Mango')

key_view = tester.viewkeys()
value_view = tester.viewvalues()

print key_view
print value_view
print tester

cake_test ='cake' in tester
print cake_test

Mango_test = "Mango" in tester.itervalues()
print Mango_test
