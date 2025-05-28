def remove_duplicates(input_string):
    if input_string is None:
        return "Error! Input is None"
    if not isinstance(input_string, str):
        return "Error! Input must be a string"

    check = {}
    result = ""

    for char in input_string:
        if char not in check:
            check[char] = 1
            result = result + char

    return result
