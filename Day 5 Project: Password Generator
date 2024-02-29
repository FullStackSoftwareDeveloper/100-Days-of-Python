import random

list_num = [1,2,3,4,5,6,7,8,9,0]
list_letter = ["q","w","e","r","t","y","!","?","_"]

password = ""
counter1 = 0
counter2 = 0

user_num = int(input("How many numbers ? "))
user_letter = int(input("How many letters ? "))

while counter1 < user_num:
  num = random.randint(0,len(list_num)-1)
  password = password + str(list_num[num])
  counter1 += 1
while counter2 < user_letter:
  letter = random.randint(0,len(list_letter)-1)
  password = password + str(list_letter[letter])
  counter2 += 1

print(password)
