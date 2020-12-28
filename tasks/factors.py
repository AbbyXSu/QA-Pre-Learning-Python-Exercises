def factors(number):
    # ==============
    # Your code here
    output = []
    for i in range(2, number):
        if number % i == 0:
            output.append(i)

    if len(output) == 0:
        return f'{number} is a prime number'
    return output
    # ==============


print(factors(15))  # Should print [3, 5] to the console
print(factors(12))  # Should print [2, 3, 4, 6] to the console
print(factors(13))  # Should print “[]” (an empty list) to the console
