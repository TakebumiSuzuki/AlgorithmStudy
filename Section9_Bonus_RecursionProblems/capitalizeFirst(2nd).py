def capitalizeFirst(arr):
    if len(arr) == 0: return []
    #if arr is None: return []　と書くと、arrの参照先そのものがNoneであるという意味になるのでダメ
    
    lastWord = arr.pop()
    capitalized = ''
    
    for i in range(len(lastWord)):
        if i == 0:
            capitalized += lastWord[i].upper()
        else:
            capitalized += lastWord[i]
    
    result = capitalizeFirst(arr)
    result.append(capitalized)
    return result
    #上の３行で、return capitalizeFirst(arr).append(capitalized)と書くと、appendはin placeで操作を行い、戻り値がNoneなので、
    #エラーが出る。必ず変数の中に格納した上でreturnしないといけないのでこうなる。
    

print(capitalizeFirst(['car','taco','banana','mango','orange']))
    
    