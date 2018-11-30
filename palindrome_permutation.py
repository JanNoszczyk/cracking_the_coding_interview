# Given a string, write a function to check if it is a permutation of a palindrome.
# A palindrome is a word or phrase that is the same forwards and backwards.
# A permutation is a rearrangement of letters.
# The palindrome does not need to be limited to just dictionary words.
# EXAMPLE
# Input: Tact Coa
# Output: True (permutations: "taco cat", "atco eta", etc.)

def palindrome_permutation(input_string):
    input_string = input_string.lower()
    repetition_dict = {}
    for char in input_string:
        if char in repetition_dict:
            repetition_dict[char] += 1
        else:
            repetition_dict[char] = 1

    number_of_pairs = 0
    number_of_singles = 0
    for k, v in repetition_dict.items():
        if v % 2 == 0:
            # Even case
            number_of_pairs += v/2
        else:
            number_of_singles += 1
            if v > 1:
                number_of_pairs += (v-1)/2

    # A palindrome will have only character pairs for even
    # length strings and pairs + 1 single for odd strings
    string_length = len(input_string)
    if number_of_singles > 1 or string_length < 2:
        return False
    else:
        if string_length % 2 == 0 and number_of_singles == 0:
            return True
        elif string_length % 2 != 0 and number_of_singles == 1:
            return True
        else:
            return False
