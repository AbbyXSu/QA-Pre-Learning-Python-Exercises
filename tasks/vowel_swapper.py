def vowel_swapper(string):
    # ==============
    #a becomes 4
    #e becomes 3
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
    return "".join([x if x.lower() not in vowel_map.keys() else vowel_map[x] for x in string])

    # ==============

print(vowel_swapper("aA eE iI oO uU")) # Should print "44 33 !! ooo000 |_||_|" to the console
print(vowel_swapper("Hello World")) # Should print "H3llooo Wooorld" to the console 
print(vowel_swapper("Everything's Available")) # Should print "3v3ryth!ng's 4v4!l4bl3" to the console


def vowel_swapper_extension(string):
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
        elif x not in counter:
            counter[x] = 1
            output.append(x)
        else:
            counter[x] += 1
            if counter[x] == 2:
                output.append(vowel_map[x])
    return "".join(output)


print(vowel_swapper_extension("aAa eEe iIi oOo uUu")) # Should print "a4a e3e i!i o000o u|_|u" to the console
print(vowel_swapper_extension("Hello World")) # Should print "Hello Wooorld" to the console
print(vowel_swapper_extension("Everything's Available")) # Should print "Ev3rything's Av4!lable" to the console