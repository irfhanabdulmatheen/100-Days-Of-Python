my_list = [1, 2, 3, 4, 5]

n = len(my_list)  
for i in range(n // 2):
    temp = my_list[i]
    my_list[i] = my_list[n - i - 1]
    my_list[n - i - 1] = temp

print("Reversed List:", my_list)
