def find_largest(numbers):
    negative_numbers = [num for num in numbers if num < 0]
    if not negative_numbers:
        return None
    return max(negative_numbers)
user_input = input("Enter numbers: ")
numbers = list(map(int, user_input.split()))
largest_negative = find_largest(numbers)
if largest_negative is not None:
    print(f"The largest negative number is: {largest_negative}")
else:
    print("No negative numbers in the list.")
