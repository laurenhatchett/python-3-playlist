# OPERATORS
# <,>,==,!=, =>,=<

age = int(input('enter your age:'))

if age < 10: 
  print('you are young, strange one')
elif age < 40:
  print('the fire in you is strong, strange one')
else: 
  print('you are wise beyond doubt')

meaty = input('do you eat meat? yes or no')
if meaty == 'yes':
  print('here is the meaty menu')
else: 
  print('here is the veggie menu')