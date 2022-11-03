num1 = 3.1425467389
num2 = 10.2903948

#PREVIOUS
print('num 1 is', num1, 'and num2 is', num2)

#FORMAT METHOD
print('num 1 is {0} ad num 2 is {1}'.format(num1, num2))#prints all numbers in the value
print('num 1 is {0:.3} ad num 2 is {1:.3}'.format(num1, num2)) #prints 3 numbers in total for each value

#USING F STRINGS
print('num 1 is {0:.3f} ad num 2 is {1:.3f}'.format(num1, num2)) # prints 3 numbers after the decimal for each value
print(f'num 1 is {num1} and num2 is {num2}')
