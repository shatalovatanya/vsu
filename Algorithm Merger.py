def merge_sort(list):
    print("Splitting ", list)
    if len(list)>1:
        mid = len(list) // 2
        leftHalf = list[:mid]
        rightHalf = list[mid:]

        merge_sort(leftHalf)
        merge_sort(rightHalf)

        i=0
        j=0
        k=0
        while i<len(leftHalf) and j<len(rightHalf):
            if leftHalf[i]<rightHalf[j]:
                list[k]=leftHalf[i]
                i=i+1
            else:
                list[k]=rightHalf[j]
                j=j+1
            k=k+1

        while i<len(leftHalf):
            list[k]=leftHalf[i]
            i=i+1
            k=k+1

        while j<len(rightHalf):
            list[k]=rightHalf[j]
            j=j+1
            k=k+1
    print("Merging ", list)

list = [8, 1, 2, 6, 0, 9, 23, 56, 100, 93, 82, 8, 42]
merge_sort(list)
print(list)