class Point:
    def set(self, x, y):
        self.x = x
        self.y = y

    def disp(self):
        print(self.x, self.y)

pt = Point()
pt.set(3, 5)
pt.disp()
        
