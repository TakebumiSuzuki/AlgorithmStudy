def findLongestSubstring(str):
    dic = {}
    maxLength = 0
    i = 0
    j = 0
    while j < len(str):
        char = str[j]
        if char in dic and dic[char] == 1:
            tempLength = j - i
            maxLength = max(maxLength, tempLength)
            while str[i] != char:
                dic[str[i]] = 0
                i += 1
            i += 1
        else:
            dic[char] = 1
        j += 1
        
    #jが最後まで行き着いた後の時点でのカウントがされていないのでした２行を加えて完成した。
    tempLength = j - i 
    maxLength = max(maxLength, tempLength)
        
    return maxLength



#以下はAIによる回答
# def findLongestSubstring(str):
#     dic = {}
#     maxLength = 0
#     i = 0
#     j = 0
#     while j < len(str):
#         char = str[j]
#         if char in dic:
#             i = max(dic[char], i)
#         maxLength = max(maxLength, j - i + 1)
#         dic[char] = j + 1
#         j += 1
#     return maxLength

print(findLongestSubstring('')) # 0
print(findLongestSubstring('rithmschool')) # 7
print(findLongestSubstring('thisisawesome')) # 6
print(findLongestSubstring('thecatinthehat')) # 7
print(findLongestSubstring('bbbbbb')) # 1
print(findLongestSubstring('longestsubstring')) # 8
print(findLongestSubstring('thisishowwedoit')) # 6

