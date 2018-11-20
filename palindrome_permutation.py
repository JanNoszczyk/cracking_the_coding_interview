def palindrome_permutation(input_string):

    no_spaces = 0
    for i in input_string:
        if i == ' ':
            no_spaces += 1

    number_repetitions =