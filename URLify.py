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