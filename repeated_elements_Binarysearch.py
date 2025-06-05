def find_duplicate_binary_search(arr):
    if arr is None:
        return "Error! Input is None"
    if not isinstance(arr, list):
        return "Error! Input must be a list"

    low = 1
    high = len(arr) - 1  

    while low <= high:
        mid = (low + high) // 2


        count = 0
        for i in range(len(arr)):
            if arr[i] <= mid:
                count += 1

        if count > mid:
            duplicate = mid
            high = mid - 1
        else:
             low = mid + 1

    return duplicate


print(find_duplicate_binary_search([1, 2, 3, 4, 4, 5]))  
print(find_duplicate_binary_search([1, 3, 4, 2, 2]))
