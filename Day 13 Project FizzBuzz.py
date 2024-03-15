#FizzBuzz if number divisible by 3 and 5
#Fizz if number divisible by 3
#Buzz if number divisible by 5
#Show the number if none are aplicable

user = int(input("Pick a range: "))
numbers=[]

for i in range(1,user+1):
  numbers.append(i)

for i in range(len(numbers)):
  if numbers[i]%3 == 0 and not numbers[i]%5 == 0:
    print("Fizz")
  elif numbers[i]%5 == 0 and not numbers[i]%3 == 0:
    print("Buzz")
  elif numbers[i]%3 == 0 and numbers[i]%5 == 0:
    print("FizzBuzz")
  else:
    print(numbers[i])
