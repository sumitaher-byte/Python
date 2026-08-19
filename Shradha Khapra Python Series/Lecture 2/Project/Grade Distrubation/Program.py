marks = float(input("Enter Your Marks:-"))

if 100 > marks >= 90:
    print("Grade-A")

elif 90 > marks >= 80:
    print("Grade-B")

elif 80 > marks >= 70:
    print("Grade-C")

elif 70 > marks >= 0:
    print("Grade-D")

else:
    print("Enter Valid Marks")