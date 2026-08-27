class Circle:


    def area(self, r):
        self.radius = r
        self.area = (22/7)*self.radius*self.radius
        return self.area


r = float(input("Entre Radius of Circle:-"))
c1 = (2)
Circle.area(r)