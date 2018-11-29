# Write a method to replace all spaces in a string with '%20'.
# You may assume that the string has sufficient space at the end to hold the additional characters,
# and that you are given the "true" length of the string.
# (Note: If implementing in Java,please use a character array so that you can perform this operation in place.)
# EXAMPLE
# Input: "Mr John Smith ", 13
# Output: "Mr%20John%20Smith"

# Note this is a long implementation trying to mimic the behaviour of character arrays in Java
def URLify(string, true_length):
    string = list(string)
    space_count = 0
    for j in range(true_length):
        if string[j] == ' ':
            space_count += 1

    index = true_length + 2*space_count

    if true_length < len(string):
        string[true_length] = '\0'

    for i in reversed(range(true_length)):
        print(i)
        if string[i] == ' ':
            string[index - 1] = '0'
            string[index - 2] = '2'
            string[index - 3] = '%'
            index -= 3
        else:
            string[index - 1] = string[i]
            index -= 1

    return string