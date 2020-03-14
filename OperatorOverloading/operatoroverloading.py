class Point:

    def __init__(self,x,y):
        self.__x = x
        self.__y = y

    def __str__(self):
        return "(" + str(self.__x) + "," + str(self.__y) + ")"

    def __add__(self,point_object):
        return Point(self.__x + point_object.__x,self.__y + point_object.__y)

P1 = Point(1,2)
P2 = Point(3,4)
P3 = P1 + P2
print(P3)
