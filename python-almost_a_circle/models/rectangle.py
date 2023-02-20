#!/usr/bin/python3
""" This module defines the Rectangle class """

from models.base import Base


class Rectangle(Base):
    """
    Rectangle class

    Private Instance Attributes:
        width (int):
            width of the rectangle instance
        heigth (int):
            height of the rectangle instance
        x (int):
            x position of the rectangle instance
        y (int):
            y position of the rectangle instance
        id (int):
            unique identifier for the rectangle instance

    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ Constructor method """

        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ Getter method for width property """

        return self.__width

    @width.setter
    def width(self, value):
        """ Setter method for width property """

        self.validate_attribute("width", value)
        self.__width = value

    @property
    def height(self):
        """ Getter method for height property """

        return self.__height

    @height.setter
    def height(self, value):
        """ Setter method for height property """

        self.validate_attribute("height", value)
        self.__height = value

    @property
    def x(self):
        """ Getter method for x property """

        return self.__x

    @x.setter
    def x(self, value):
        """ Setter method for x property """

        self.validate_attribute("x", value)
        self.__x = value

    @property
    def y(self):
        """ Getter method for y property """

        return self.__y

    @y.setter
    def y(self, value):
        """ Setter method for y property """

        self.validate_attribute("y", value)
        self.__y = value

    def area(self):
        """ Computes the are of the rectangle instance """

        return (self.width * self.height)

    def display(self):
        """ Prints to stdout the Rectangle instance """
        for i in range(self.y):
            print("")

        for i in range(self.height):
            print((" " * self.x) + ("#" * self.width))

    def update(self, *args, **kwargs):
        """ Assigns an argument to each attribute """

        attrs = ("id", "width", "height", "x", "y")
        if args:
            for kw, value in zip(attrs, args):
                setattr(self, kw, value)
        elif kwargs:
            for kw, value in kwargs.items():
                setattr(self, kw, value)

    def to_dictionary(self):
        """ Returns the dictionary representation of a Rectangle """

        square_attibutes = ["id", "width", "height", "x", "y"]
        return {attr: getattr(self, attr) for attr in square_attibutes}

    def __str__(self):
        """
        Defines the string representation of the rectangle object

        Returns:
            A string representation of the rectangle with "#"

        """
        rectangle_str = f"[Rectangle] ({self.id}) {self.x}/{self.y} \
- {self.width}/{self.height}"

        return (rectangle_str)

    @staticmethod
    def validate_attribute(attribute_name, value):
        """
        Validates a given attribute of a rectangle instance

        Parameters:
            attribute_name (str):
                the name of the attribute
            value (any):
                the value to be validated

        Raises:
            TypeError:
                if value is not an integer

            ValueError:
                if value is less or equal to zero for the widht or heigh
                if value is less than zero for x and y

        """

        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(attribute_name))

        if attribute_name in ("width", "height"):
            if value <= 0:
                raise ValueError("{:s} must be > 0".format(attribute_name))
        elif attribute_name in ("x", "y"):
            if value < 0:
                raise ValueError("{:s} must be >= 0".format(attribute_name))
