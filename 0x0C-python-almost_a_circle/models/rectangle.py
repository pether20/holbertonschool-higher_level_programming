#!/usr/bin/python3
""" FUNCTION RECTANGLE """
from time import sleep
from unicodedata import name
from models.base import Base


class Rectangle(Base):
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
        return self.__y

    @width.setter
    def width(self, value):
        if not (isinstance(value, int)):
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')
        self.__width = value

    @height.setter
    def height(self, value):
        if not (isinstance(value, int)):
            raise TypeError('height must be an integer')
        if value <= 0:
            raise ValueError('height must be > 0')
        self.__height = value

    @x.setter
    def x(self, value):
        if not (isinstance(value, int)):
            raise TypeError('x must be an integer')
        if value < 0:
            raise ValueError('x must be >= 0')
        self.__x = value

    @y.setter
    def y(self, value):
        if not (isinstance(value, int)):
            raise TypeError('y must be an integer')
        if value < 0:
            raise ValueError('y must be >= 0')
        self.__y = value

    def area(self):
        """Methode return Area"""
        return self.__height * self.__width

    def display(self):
        """Methode print instance"""
        ex, ye = self.x, self.y
        an, al = self.width, self.height
        print("\n" * ye + "\n".join(" " * ex + "#" * an for i in range(al)))

    def __str__(self):
        """Print """
        nm = self.__class__.__name__
        ide, ex = self.id, self.__x
        ye, an, al = self.__y, self.__width, self.__height
        return f"[{nm}] ({ide}) {ex}/{ye} - {an}/{al}"

    def update(self, *args, **kwargs):
        """
        If args: set attributes in this order: id, width, height, x, y
        If no args given: set attributes according to kwargs
        """
        if args:
            for k, v in enumerate(args):
                if k == 0:
                    self.id = v
                elif k == 1:
                    self.width = v
                elif k == 2:
                    self.height = v
                elif k == 3:
                    self.x = v
                else:
                    self.y = v
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "width" in kwargs:
                self.width = kwargs["width"]
            if "height" in kwargs:
                self.height = kwargs["height"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]

    def to_dictionary(self):
        """Return dictionary representation"""
        d = {}
        d["id"] = self.id
        d["width"] = self.width
        d["height"] = self.height
        d["x"] = self.x
        d["y"] = self.y
        return d
        