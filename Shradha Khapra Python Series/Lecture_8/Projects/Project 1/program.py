class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def sum(self):
        s = 0
        for m in self.marks:
            s += m
        print("Your avg marks are:", s/3)

        

s1 = Student("Sumit",[98,56,76])
s1.sum()