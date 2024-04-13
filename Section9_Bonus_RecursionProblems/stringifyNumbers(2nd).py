def stringifyNumbers(dic):
    newDic = {}
    for key, value in dic.items():
        if type(value) == dict:
            newDic[key] = stringifyNumbers(value)
        elif type(value) == int or type(value) == float:
            newDic[key] = str(value)
        else:
            newDic[key] = value
            
    return newDic
    
obj = {
    "num": 1,
    "test": [],
    "data": {
        "val": 4,
        "info": {
            "isRight": True,
            "random": 66
        }
    }
}
        

print(stringifyNumbers(obj))
    