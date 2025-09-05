import random

print("Your password is: ")
char = "abcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*"

password = ''
for x in range(16):
  password += random.choice(char)
print(password)
repetition = ''
while True:
  repetition = input("Try again? (yes/no): ")
  if repetition == "no":
    print("Thank you for using our program!")
    break
  elif repetition == "yes":
    password = ''
    for x in range(16):
      password += random.choice(char)
    print(password)
  else:
    print("Error!")