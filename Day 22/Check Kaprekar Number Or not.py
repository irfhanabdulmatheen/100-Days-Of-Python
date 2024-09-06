num = int(input("Enter a number: "))

sq = num * num

sq_str = str(sq)

length = len(sq_str)

left_str = sq_str[:length // 2]  
right_str = sq_str[length // 2:]

if left_str == '':
    left = 0
else:
    left = int(left_str)  

right = int(right_str)

if left + right == num:
    print(f"{num} is a Kaprekar number.")
else:
    print(f"{num} is not a Kaprekar number.")
