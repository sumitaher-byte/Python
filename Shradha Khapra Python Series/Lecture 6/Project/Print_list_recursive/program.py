def lis(list, idx=0):
    if idx == len(list):
        return
    print(list[idx])
    return lis(list, idx+1)

list = ["sumit","triveni",'rutuja','urvi','daksh']
lis(list)