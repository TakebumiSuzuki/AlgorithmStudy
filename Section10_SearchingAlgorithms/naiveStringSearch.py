def naiveStringSearch(short, long):
    numOfMatch = 0
    for i in range(len(long)):
        matchingWords = 0
        for j in range(len(short)):
            if long[i + j] != short[j]:
                break
            matchingWords += 1
        if matchingWords == len(short):
            numOfMatch += 1
    
    return numOfMatch

print(naiveStringSearch("side", "off side and left side, water front in my side"))