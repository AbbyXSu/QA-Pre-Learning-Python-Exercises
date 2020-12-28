
def vowel_swapper(string):
    # ==============
    # a becomes 4
    # e becomes 3
    # i becomes !
    # o becomes ooo
    # u becomes |_|
    # Your code here
    vowel_map = {
        'a': "4",
        "A": "4",
        "e": "3",
        "E": "3",
        "i": "!",
        "I": "!",
        "o": "ooo",
        "O": "OOO",
        "u": "|_|",
        "U": "|_|"
    }
    counter = {}
    output = []
    for x in string:
        if x not in vowel_map.keys():
            output.append(x)
        elif x.lower() not in counter:
            counter[x.lower()] = 1
            output.append(x)
        else:
            counter[x.lower()] += 1
            if counter[x.lower()] == 2:
                output.append(vowel_map[x])
            else:
                output.append(x)
    return "".join(output)

print(vowel_swapper("aAa eEe iIi oOo uUu"))  # Should print "a4a e3e i!i o000o u|_|u" to the console
print(vowel_swapper("Hello World"))  # Should print "Hello Wooorld" to the console
print(vowel_swapper("Everything's Available"))  # Should print "Ev3rything's Av4!lable" to the console


