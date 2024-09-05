def print_binary(n):
    binary = ""
    num_bits = n.bit_length()
    for i in range(num_bits, 0, -1):
        binary += str((n >> (i - 1)) & 1)
    print(binary)
num = int(input("Enter a number: "))
print_binary(num)
