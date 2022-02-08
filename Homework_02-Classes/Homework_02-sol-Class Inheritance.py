#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 24 15:13:43 2021

@author: alivaliyev
"""
from abc import ABC, abstractmethod
import math

class Point(ABC):
    
    def __init__(self, x, y):
        self.X = x
        self.Y = y

    def stri(self):
        
        return (self.X, self.Y) 
    
class Shape(Point):
    
    def __init__(self, leftTop):
        
        self.leftTop = leftTop
        
    @abstractmethod
    def calculatePoints(self):
        """Points:"""
        pass
    @abstractmethod
    def calculateArea(self):
        """Area:"""
        pass
        
    @abstractmethod
    def calculatePerimeter(self):
        """Perimeter:"""
        pass
    
    
class Rectangle(Shape):

    def __init__(self, leftTop, height, width):
        
        super().__init__(leftTop)
        self.height = height
        self.width = width
    
    def calculatePoints(self):
        
        Points=[]
        Points.append(self.leftTop)
        a=self.leftTop
        a=list(a)
        a[0]=a[0]+self.width
        a=tuple(a)
        b=self.leftTop
        c=self.leftTop
        b=list(b)
        c=list(c)
        b[0]=b[0]+self.width
        b[1]=b[1]+self.height
        c[1]=c[1]+self.height
        b=tuple(b)
        c=tuple(c)
        Points.append(a)
        Points.append(b)
        Points.append(c)
        Points= str(Points).replace('[','').replace(']','')
        return Points
    
    def calculateArea(self):
        return self.width * self.height

    def calculatePerimeter(self):
        return 2 * (self.width + self.height)
    
    def get_height(self):
        return self.height
    
    def get_width(self):
        return self.width

    def get_lefttop(self):
        return self.leftTop
        
class Circle(Shape):
    
    def __init__(self, leftTop, radius):
        super().__init__(leftTop)
        self.radius = radius
        
    def calculatePoints(self):
        Points=[]
        Points.append(self.leftTop)
        d=self.leftTop
        d=list(d)
        d[0] =d[0] + 2*self.radius
        d[1] =d[1] + 2*self.radius
        d=tuple(d)
        Points.append(d)
        Points= str(Points).replace('[','').replace(']','')
        return Points
    
    def calculateArea(self):
        return math.pi * self.radius ** 2

    def calculatePerimeter(self):
        return 2 * math.pi * self.radius
    
    def get_radius(self):
        return self.radius
    
    def get_lefttop(self):
        return self.leftTop
    
#def main():
 #   "main kod buraya yazılacak"

#if __name__ == "__main__":
 #   main()
 
#main part of code
while(True):
    var = input("Type of Shape (q for exit):  ")
    if var=="r":
        x1, y1, height, width = input("Coordinate(leftTop), height and width:  ").split()
        
        lefttop1 =  Point(int(x1),int(y1))
        lefttop2 = lefttop1.stri()
        rectangle1=Rectangle(lefttop2,int(height),int(width))
        print("--Rectangle --")
        print("Height:", rectangle1.get_height())
        print("Width:", rectangle1.get_width())
        print("Left Top Point:", rectangle1.get_lefttop())
        print("Area:","{:.2f}".format(rectangle1.calculateArea()))
        print("Perimeter:","{:.2f}".format(rectangle1.calculatePerimeter()))
        print("Points:", rectangle1.calculatePoints())
        
        x2, y2 =input("Move object to the new coordinate(leftTop):  ").split()
        lefttop3=Point(int(x2),int(y2))
        lefttop4=lefttop3.stri()
        rectangle2=Rectangle(lefttop4,int(height),int(width))
        
        print("--Rectangle --")
        print("Height:", rectangle2.get_height())
        print("Width:", rectangle2.get_width())
        print("Left Top Point:", rectangle2.get_lefttop())
        print("Area:","{:.2f}".format(rectangle2.calculateArea()))
        print("Perimeter:", "{:.2f}".format(rectangle2.calculatePerimeter()))
        print("Points:", rectangle2.calculatePoints())
    if var=="c":
        x3,y3, radius1 =input("Coordinates(leftTop) and radius:"  ).split()
        lefttop5=Point(int(x3),int(y3))
        lefttop6=lefttop5.stri()
        circle1 = Circle(lefttop6, int(radius1))
    
        print("--Circle --")
        print("Radius:", circle1.get_radius())
        print("Left Top Point:", circle1.get_lefttop())
        print("Area:","{:.2f}".format(circle1.calculateArea()))
        print("Perimeter:", "{:.2f}".format(circle1.calculatePerimeter()))
        print("Points:", circle1.calculatePoints())
    
        x4,y4 = input("Move object to the new coordinate(leftTop): ").split()
        lefttop7=Point(int(x4),int(y4))
        lefttop8=lefttop7.stri()
        circle2 = Circle(lefttop8, int(radius1))
    
        print("--Circle --")
        print("Radius:", circle2.get_radius())
        print("Left Top Point:", circle2.get_lefttop())
        print("Area:","{:.2f}".format(circle2.calculateArea()))
        print("Perimeter:", "{:.2f}".format(circle2.calculatePerimeter()))
        print("Points:", circle2.calculatePoints())
    if var=="q":
        break