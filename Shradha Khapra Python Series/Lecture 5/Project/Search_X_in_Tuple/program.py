tuple = (1,4,9,16,25,36,49,64,81,100)
idx = 0

no = int(input("Enter No. You Want To Search :-"))

while idx < (len(tuple)):
    if tuple[idx] == no:
        print("your np.", no, "is on index", idx)
    idx += 1



