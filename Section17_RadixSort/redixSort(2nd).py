# def radixSort(arr):
#     maxDigitCount = mostDigits(arr)
#     temp = arr.copy()
#     for k in range(maxDigitCount):
#         digitBuckets = [[],[],[],[],[],[],[],[],[],[]]
#         for i in range(len(arr)):
#             digit = getDigit(temp[i], k)
#             digitBuckets[digit].append(temp[i])
#         temp = []
#         for k in digitBuckets:
#             temp.extend(k)
#     return temp
            
def radixSort(arr): #in placeでarrを書き直す方法。上の方法は入力したのとは別のarrを作っている
    maxDigitCount = mostDigits(arr)
    for k in range(maxDigitCount):
        # digitBuckets = [[],[],[],[],[],[],[],[],[],[]]
        digitBuckets = [[] for _ in range(10)] #内包表記で作成
        for i in range(len(arr)):
            digit = getDigit(arr[i], k)
            digitBuckets[digit].append(arr[i])
        arr = []
        for k in digitBuckets:
            arr.extend(k) #extendはin placeでリストをmodifyすることに注意
    return arr

def getDigit(num, place):
    strNum = str(num)
    digits = len(strNum)
    if place >= digits:
        return 0
    return int(strNum[- (place + 1)])

def getDigit2(num, place):
    return num // (10 ** place) % 10

def digitCount(num):
    count = 0
    temp = num
    while True:
        count += 1
        temp = temp // 10
        if temp < 1:
            return count
        
def mostDigits(arr):
    return digitCount(max(arr))

print(radixSort([23, 567,89,12234324, 90, 1, 983]))

# print(getDigit2(38291, 0))
# print(getDigit2(38291, 1))
# print(getDigit2(38291, 2))
# print(getDigit2(38291, 3))
# print(getDigit2(38291, 4))
# print(getDigit2(38291, 5))