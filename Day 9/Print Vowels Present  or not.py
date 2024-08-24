input_string = input("Enter a string: ")

vowels = {'a', 'e', 'i', 'o', 'u'}

input_set = set(input_string.lower())

vowels_present = bool(vowels & input_set)

if vowels_present:
    print("Vowels are present in the string.")
else:
    print("Vowels are not present in the string.")
