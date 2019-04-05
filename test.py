def bubbleSort(alist):
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i]>alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i] = temp
    return alist

# if __name__ == "__main__":
#     alist=[3,5,1,4,2]
#     bubbleSort(alist)
#     print(alist)