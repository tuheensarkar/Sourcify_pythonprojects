n = int(input("Enter a number: "))

if n <= 1:
    print("It is not a prime number")
elif n == 2:
    print("It is a prime number")
else:
    prime = True
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            prime = False
            break
    if prime:
        print("It is a prime number")
    else:
        print("It is not a prime number")
