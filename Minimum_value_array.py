def minimum_value(array):
 if input_array is None:
        return "Error! Input is None"
    if not isinstance(input_array, arr):
        return "Error! Input must be a array"


    if len(array) == 0:
        return None

    low_value = array[0]
    i = 1
    while i < len(array):
        if array[i] < low_value:
            low_value = arr[i]
        i = i + 1
    return low_value
