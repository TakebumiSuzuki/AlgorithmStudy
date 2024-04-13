
#この方法だと、Time Complexityはbestで(中央値をとり続けた場合O(nlogn))、worstでO(n^2)
#Space Complexityも同様で、bestで(中央値をとり続けた場合O(nlogn))、worstでO(n^2)
#Udemy内での講義のようにin placeでswapさせていく方法だとSpace Complexityがbestで(中央値をとり続けた場合O(logn))、worstでO(n)になる
def quickSort(arr):
    if len(arr) <= 1:
        return arr;
    
    leftArr = [];
    rightArr = [];
    pivot = arr[0];
    for i in range(1, len(arr)):
        if arr[i] <= pivot:
            leftArr.append(arr[i]);
        else:
            rightArr.append(arr[i]);
    return quickSort(leftArr) + [pivot] + quickSort(rightArr);


print(quickSort([5,7,1,8,-4,-1,-7,12,4,10,-100, 100]))
    