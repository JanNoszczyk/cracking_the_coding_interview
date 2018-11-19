def URLify(string, true_length):
    space_count = 0
    for j in string:
        if j == ' ':
            space_count += 1

    index = true_length + 2*space_count
    print(index)
    string_list = list(string)
    for i in reversed(range(true_length)):
        print(i)
        if string[i] == ' ':
            string_list[index - 1] = '0'
            string_list[index - 2] = '2'
            string_list[index - 3] = '%'
            index -= 3
        else:
            string_list[index - 1] = string[i]
            index -= 1

    return string_list