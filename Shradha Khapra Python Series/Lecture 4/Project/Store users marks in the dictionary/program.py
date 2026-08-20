#wap to enter marks of 3 sub from the user and store them in a dictionary. Start eith a empty dictionary add one by one.Use subject name as a key and marks as value.

dic = {}

dic.update({"math" : (input("Entre Your Math Marks:-"))})
dic.update({"physics" : (input("Entre your physics marks:-"))})
dic.update({"chemistry":(input("Entre your chemistry marks:-"))})

print(dic)