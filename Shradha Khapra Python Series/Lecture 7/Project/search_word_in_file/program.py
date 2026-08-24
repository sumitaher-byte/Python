with open(r"D:\Python\Shradha Khapra Python Series\Lecture 7\Project\search_word_in_file\file.txt","r") as f:
    data = f.read()

word = str(input("Word want to Find:-"))
t = data.count(word)
if t == 0:
    print("No word found")
else:
    print("Word found", t,"times.")