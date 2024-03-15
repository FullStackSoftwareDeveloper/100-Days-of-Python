def addition(first_number,second_number):
  result = first_number + second_number
  return result

def subtraction(first_number,second_number):
  result = first_number - second_number
  return result

def multiplication(first_number,second_number):
  result = first_number * second_number
  return result

def division(first_number,second_number):
  result = first_number / second_number
  return result

user_first_num = int(input("Write your first number: "))

while True:
  operation = input("Pick the operation [+ - * /]: ")
  user_second_num = int(input("Write another number: "))
  if operation == "+":
    answer = addition(user_first_num,user_second_num)
    print(answer)
    if input("calculate more? [Y/N]: ") == "Y":
      user_first_num = answer
    else:
      break
  elif operation == "-":
    answer = subtraction(user_first_num,user_second_num)
    print(answer)
    if input("calculate more? [Y/N]: ") == "Y":
      user_first_num = answer
    else:
      break
  elif operation == "*":
    answer = multiplication(user_first_num,user_second_num)
    print(answer)
    if input("calculate more? [Y/N]: ") == "Y":
      user_first_num = answer
    else:
      break
  else:
    answer = division(user_first_num,user_second_num)
    print(answer)
    if input("calculate more? [Y/N]: ") == "Y":
      user_first_num = answer
    else:
      break
