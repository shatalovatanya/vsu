list = [7, 1, 2, 6, 0, 9, 23, 55, 106, 97, 86, 10, 31]
def past_sort(arrayToSort):
    a = arrayToSort
    for i in range(len(a)):
        num = a[i]
        indexNum = i
        while (a[indexNum - 1] > num) and (indexNum > 0):
            a[indexNum] = a[indexNum - 1]
            indexNum = indexNum - 1
        a[indexNum] = num
        print (a)
    return a
print (past_sort(list))