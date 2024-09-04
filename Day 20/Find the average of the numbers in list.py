numbers = input("Enter a list of numbers")
numbers = [int(num) for num in numbers.split()]

sum = 0

for num in numbers:
    sum += num

average = sum / len(numbers)

print("The average of the list is:", average)
