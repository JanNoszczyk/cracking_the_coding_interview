# Given two strings,write a method to decide if one is a permutation of the
# other.

def check_permutation(string1, string2):
    if len(string1) != len(string2):
        return False
    else:
        if sorted(string1) == sorted(string2):
            return True
        else:
            return False