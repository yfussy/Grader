class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return "("+str(self.x)+","+str(self.y)+")" 
    
class Rect:
    def __init__(self, p1, p2):
        self.lowerleft = p1
        self.upperright = p2
        self.xrange = range(p1.x, p2.x+1)
        self.yrange = range(p1.y, p2.y+1)

    def area(self):
        l = self.upperright.x - self.lowerleft.x
        h = self.upperright.y - self.lowerleft.y
        return l*h
    
    def contains(self, p):
        if p.x in self.xrange and p.y in self.yrange:
            return True
        return False
    
x1,y1,x2,y2 = [int(e) for e in input().split()]
lowerleft = Point(x1,y1)
upperright = Point(x2,y2)
rect = Rect(lowerleft, upperright)
print(rect.area())
m = int(input())
for i in range(m):
    x,y = [int(e) for e in input().split()]
    p = Point(x,y)
    print(rect.contains(p)) 