number = int(input("Enter a number: "))
for i in range(1, number):
    sum=0
    temp=i
    for j in range(1,number):
        if temp % j == 0:
            sum += j
            if(temp == sum):
                print(f"{sum}")
      
