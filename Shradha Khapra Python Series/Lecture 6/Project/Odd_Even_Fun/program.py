no = int(input("Entre No.:-"))

def odd_even_finder(no):
    if 0 == no % 2:
        ans = "EVEN"
    elif 1 == no %  2:
        ans = "ODD"
    else:
        ans = "Something Went Wrong!"
    return(ans)

print(odd_even_finder(no))
    