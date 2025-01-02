# classes are blueprint for creating an object
# object are actual instance of a class
# each object is a different instance of a point class
class Point:
    def move(self):
        print('move')

    def draw(self):
        print('draw')

point1 = Point()
point1.x = 10
point1.y = 20
print(point1.x