with open(r"D:\Python\Shradha Khapra Python Series\Lecture 7\Project\count_even_no\file.txt","r") as f:
    data = f.read()
    no = data.split(',')
    count = 1
    for num in no:
        num = int(num)
        if 0 == num % 2:
            count += 1
    print(count)

        