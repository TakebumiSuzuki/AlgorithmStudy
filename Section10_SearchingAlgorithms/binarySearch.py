
def binarySearch(arr, num):
    i = 0;
    j = len(arr) - 1;
    while i <= j:
        halfIndex = (i + j) // 2;
        halfNum = arr[halfIndex];
        if halfNum == num:
            return halfIndex;
        elif halfNum < num:
            i = halfIndex + 1;
        else:
            j = halfIndex - 1;
       
    return -1;
 
print(binarySearch([
  5, 6, 10, 13, 14, 18, 30, 34, 35, 37, 
  40, 44, 64, 79, 84, 86, 95, 96, 98, 99
], 100))