number = int(input("Enter a number: "))

# Check Even or Odd
if number % 2 == 0:
    print("The number is Even")
else:
    print("The number is Odd")


# Check Prime or Not Prime
if number <= 1:
    print("The number is Not Prime")
else:
    is_prime = True

    for i in range(2, number):
        if number % i == 0:
            is_prime = False
            break

    if is_prime:
        print("The number is Prime")
    else:
        print("The number is Not Prime")
