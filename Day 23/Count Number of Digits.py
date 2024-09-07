num = int(input("Enter a number: "))

count = 0

num = abs(num)

while num > 0:
    num //= 10  
    count += 1
    
if count == 0:
    count = 1

print("Number of digits:", count)
