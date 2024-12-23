def find_key(data):
    if not data: 
        return None
    return max(data, key=data.get)
def get_user_input():
    n = int(input("Enter the number of entries in the dictionary: "))
    data = {}
    for _ in range(n):
        key = input("Enter the key: ")
        value = int(input("Enter the value: "))
        data[key] = value
    return data
example_dict = get_user_input()
max_key = find_key(example_dict)

if max_key:
    print(f"The key with the maximum value is '{max_key}' with a value of {example_dict[max_key]}.")
else:
    print("The dictionary is empty.")
