list1 = []
n1 = int(input("Enter the number of elements for the numeric list (list1): "))
for i in range(n1):
    element = int(input(f"Enter numeric element {i+1}: "))
    list1.append(element)

list2 = []
n2 = int(input("Enter the number of elements for the string list (list2): "))
for i in range(n2):
    element = input(f"Enter string element {i+1}: ")
    list2.append(element)

final_list = list1 + list2

print("\nThe concatenated list is:")
print(final_list)
