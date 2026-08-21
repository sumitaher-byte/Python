n = int(input("Entre your No.:-"))

def fact(a):
    ans = 1
    for el in range(1, a+1):
        ans *= el
    return(ans)

print(fact(n))