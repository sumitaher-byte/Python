with open(r"D:\Python\Shradha Khapra Python Series\Lecture 7\Project\create_file_add_data\New_File.txt","r+") as f:
    data = f.read()

    new_data = data.replace("Java","Python")

    f.seek(0)
    f.write(new_data)
    f.truncate()

print(new_data)

