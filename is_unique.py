# Implement an algorithm to determine if a string has all unique characters.
# What if you cannot use additional data structures?

def is_unique(input_string):
    unique_flag = True
    encountered_characters = []

    for char in input_string:
        if char in encountered_characters:
            unique_flag = False
        else:
            encountered_characters.append(char)

    return unique_flag
