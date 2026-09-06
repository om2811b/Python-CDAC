n = int(input("Enter a no.: "))

rev = 0

while n>0:
    digit = n % 10
    rev = rev * 10 + digit
    n = n // 10

print("Reverse no.:", rev)