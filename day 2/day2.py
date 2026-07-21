print("Sum of 2 Numbers")
a = int(input("Enter the 1st Number :" ))
b = int(input("Enter the 2nd Number : "))

print("Sum =", a + b)


print("Check whether the number is odd or even")
num = int(input("Enter a number to check Even or Odd : "))

if num % 2 == 0:
    print("Even")
else:
    print("Odd")

print("Mulitples of the nnumber")
num = int(input("Enter the number for muliplication tables : "))

for i in range(1, 11):
    print(num, "x", i, "=", num * i)
