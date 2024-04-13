def collectStrings(dic):
    arr = []
    for value in dic.values():
        if type(value) is dict:
            arr.extend(collectStrings(value))
        if type(value) is str:
            arr.append(value)
    return arr

obj = {
    "stuff": "foo",
    "data": {
        "val": {
            "thing": {
                "info": "bar",
                "moreInfo": {
                    "evenMoreInfo": {
                        "weMadeIt": "baz"
                    }
                }
            }
        }
    }
}

print(collectStrings(obj))
