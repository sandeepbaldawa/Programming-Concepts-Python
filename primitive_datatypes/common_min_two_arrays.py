def getCommonMin(arr1, arr2):
    """
    Common minimum between arr1 and arr2
    """
    dict = {}
    # Hash all values from fist array
    for i,each in enumerate(arr1):
        dict[i] = each
    print dict
    curr_min = float('INF')
    print arr1, arr2

    # Check if values from arr1 are present in arr2
    for v in arr2:
        if v in dict.values():
            if v < curr_min:
                curr_min = v
    return curr_min

arr1 = [1,2,3,4,5]
arr2 = [5,6,7,8,9]
print getCommonMin(arr1, arr2)
