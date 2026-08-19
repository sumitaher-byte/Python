list = []

list.append(str(input("Enter:-")))
list.append(str(input("Enter:-")))
list.append(str(input("Enter:-")))
list.append(str(input("Enter:-")))
list.append(str(input("Enter:-")))


list_copy = list.copy()
list_copy.reverse()

if list == list_copy:
    print("List is Pelindrom")

else:
    print("List is not Pelindrom")
