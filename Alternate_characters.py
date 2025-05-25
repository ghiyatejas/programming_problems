def get_alternate_characters(input_string):
    result = ""
    for i in range(0, len(input_string)):
        if i % 2 == 0:
            result += input_string[i]
    return result
