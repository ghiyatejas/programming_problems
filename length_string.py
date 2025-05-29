def length_string(input_string):
    if input_string is None:
        return "Error! Input is none"
    if not isinstance(input_string, str):
        return "Error! Input must be a string"

    length = 0
    for _ in input_string:
        length += 1
    return length  
