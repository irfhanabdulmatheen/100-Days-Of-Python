n = int(input("Enter a number: "))

square = n * n

square2 = str(square)

left_part = square2[:len(square2) // 2]
right_part = square2[len(square2) // 2:]

if left_part == '':
    left_part = 0
else:
    left_part = int(left_part)

right_part = int(right_part)

if (left_part + right_part) == n:
    print(f"{n} is a Kaprekar number.")
else:
    print(f"{n} is not a Kaprekar number.")
