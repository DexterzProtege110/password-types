import random
import string

print("Enter the length of password do you want")
l = int(input())

password = []

if(l >= 8):
	for i in range(l):
		lett = random.choice(string.ascii_letters)
		password.append(lett)
	print(''.join(map(str, password)))
else:
	print("Password length cannot be less than 8.")

