def binary_search(arr, num):
    if arr is None:
        return "Error! Input is None"
    if not isinstance(arr, list):
        return "Error! Input must be a list"
   
    low = 0
    high = len(arr) - 1
   
    while low <= high:
        mid = (low + high) // 2
       
        if arr[mid] == num:
            return True
        elif num < arr[mid]:
            high = mid - 1
        else:
            low = mid + 1
