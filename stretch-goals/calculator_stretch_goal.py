def calculator(a, b, operator):
    # ==============
    # Your code here
    add = lambda i, k: i + k
    minus = lambda i, k: i - k
    multiple = lambda i, k: i * k
    divide = lambda i, k: i / k

    options = {
        '+': add,
        "-": minus,
        "*": multiple,
        "/": divide
    }
    return bin(int(options[operator](a, b)))[2:]
    # ==============


print(calculator(2, 4, "+"))  # Should print 110 to the console
print(calculator(10, 3, "-"))  # Should print 111 to the console
print(calculator(4, 7, "*"))  # Should output 11100 to the console
print(calculator(100, 2, "/"))  # Should print 110010 to the console
