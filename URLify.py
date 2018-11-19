def URLify(input_string):
    output_string = ''
    for char in input_string:
        if char == ' ':
            output_string += '%20'
        else:
            output_string += char

    return output_string