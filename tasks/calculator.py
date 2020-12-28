def calculator(a, b, operator):
    # ==============
    # Your code here
    add = lambda i, k: i+k
    minus = lambda i, k: i-k
    multiple = lambda i, k: i*k
    divide = lambda i, k: i/k

    options = {
        '+': add,
        "-": minus,
        "*": multiple,
        "/": divide
    }
    return int(options[operator](a, b))
    # ==============

print(calculator(2, 4, "+")) # Should print 6 to the console
print(calculator(10, 3, "-")) # Should print 7 to the console
print(calculator(4, 7, "*")) # Should print 28 to the console
print(calculator(100, 2, "/")) # Should print 50 to the console


def bin_calculator(a, b, operator):
    # ==============
    # Your code here
    return bin(calculator(a, b, operator))[2:]

print(bin_calculator(2, 4, "+"))# Should print 110 to the console
print(bin_calculator(10, 3, "-"))# Should print 111 to the console
print(bin_calculator(4, 7, "*")) # Should print 11100 to the console
print(bin_calculator(100, 2, "/"))# Should print 110010 to the console