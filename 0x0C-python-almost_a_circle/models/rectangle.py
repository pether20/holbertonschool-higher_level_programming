#!/usr/bin/python3
""" FUNCTION RECTANGLE """


class Rectangle(BASE):
    """ Class Rectangle inherits from Base """

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Set/Get the width of the Rectangle"""
        return self.__width

    @property
    def height(self):
        return self.__height

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self__y

    @width.setter
    def width(self, value):
        self.__width = value
    
    @height.setter
    def height(self, value):
        self.__height = value

    @x.setter
    def x(self, value):
        

        
