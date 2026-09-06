n = int(input("Enter a no.: "))

org = n
sum = 0

while n > 0:
    digit = n % 10
    sum = sum + digit ** 3
    n = n // 10

if org == sum:
    print("Armstrong no.")
else:
    print("Not Armstrong no.")