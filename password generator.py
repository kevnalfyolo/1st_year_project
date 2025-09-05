import random

print("Welcome to Password Generator🤗")
digit = int(input("How long password that you need?(In digits): "))
(print("Here you go!, your password is: "))
char = "abcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*"

password = ''
for x in range(digit):
  password += random.choice(char)
print(password)
repetition = ''
while True:
  repetition = input("Try again? (yes/no): ")
  if repetition == "no":
      print("Thank you for using our program!🙌")
      break
  elif repetition == "yes":
      password = ''
      for x in range(digit):
          password += random.choice(char)
      print(password)
  else:
      print("Error!")
