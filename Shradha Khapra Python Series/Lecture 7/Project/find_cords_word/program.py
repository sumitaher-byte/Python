def cord_finder():
    with open(r"D:\Python\Shradha Khapra Python Series\Lecture 7\Project\find_cords_word\file.txt","r") as f:
        data = f.read()
        position = data.find("learning")
        print(position)

cord_finder()