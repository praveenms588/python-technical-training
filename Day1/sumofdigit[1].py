#
number = int(input("Enter a no: "))
sum=int(0)

""" for digit in str(number):
    sum+=int(digit)
print("Sum of digit of no is ",sum) """

while number>0:
    sum+=int(number%10)
    number/=10
print("Sum of digit of no is ",sum)