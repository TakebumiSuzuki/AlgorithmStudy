def merge(arr1, arr2):
    i = 0
    j = 0
    result = []
    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            result.append(arr1[i])
            i += 1
        elif arr1[i] > arr2[j]:
            result.append(arr2[j])
            j += 1
    if i >= len(arr1):
        result += arr2[j:]
    if j >= len(arr2):
        result += arr1[i:]
    return result

print(merge([106],[2,14,99,100]))