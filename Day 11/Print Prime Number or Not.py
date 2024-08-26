number = int(input("Enter a number: "))
is_prime = 1
if number <= 1:
    is_prime = 0 
else:
    for i in range(2, number):
        if number % i == 0:
            is_prime = 0  
            break
if is_prime == 1:
    print("Prime")
else:
    print("Not Prime")
