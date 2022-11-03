#FOR LOOPS
# foods = ['pizza', 'salad', 'spaghetti', 'hamburger']


# for food in foods:
#   print(food)

# for food in foods[1:3]:
#   print(food)

# for food in foods:
#   if food == 'salad':
#     print(f'{food} - is tasty')
#     break
#   else:
#     print(food)

#WHILE LOOPS

age = 27
num = 0

#while the condition is true, the codeblock will run
while num < age:
  if num == 0:
    num += 1
    continue
  if num % 2 == 0:
    print(num)
  if num > 10:
    break
  num += 1