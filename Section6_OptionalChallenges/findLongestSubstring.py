def findLongestSubstring(str):
    charBag = {}
    maxSize = 0;
    startIndex = 0;
    endIndex = 0;
    
    while endIndex < len(str):
        ##endIndexの文字がcharBag内にない、または0の場合
        if str[endIndex] not in charBag or charBag[str[endIndex]] == 0:
            charBag[str[endIndex]] = 1;
            maxSize = max(maxSize, endIndex - startIndex + 1);
            endIndex += 1;
        else:##endIndexの文字がcharBag内に、値1としてある場合
            charBag[str[startIndex]] = 0
            startIndex += 1;
    return maxSize


print(findLongestSubstring('')) # 0
print(findLongestSubstring('rithmschool')) # 7
print(findLongestSubstring('thisisawesome')) # 6
print(findLongestSubstring('thecatinthehat')) # 7
print(findLongestSubstring('bbbbbb')) # 1
print(findLongestSubstring('longestsubstring')) # 8
print(findLongestSubstring('thisishowwedoit')) # 6