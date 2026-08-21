list = (1,4,9,16,25,36,49,64,81,100)

x = int(input("Enter No. Want To Serch:-"))

for el in list:
    if el == x:
        print("No. Found At Idx", list.index(el) )
        break

