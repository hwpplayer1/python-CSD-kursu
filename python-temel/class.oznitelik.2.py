class Point:
    def set(self, x, y):
        self.x = x
        self.y = y

    def disp(self):
        print(self.x, self.y)

pt1 = Point()
pt2 = Point()

pt1.set(10, 20)
pt2.set(30, 40)

pt1.disp()
pt2.disp()
