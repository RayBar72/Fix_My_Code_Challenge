#!/usr/bin/python3
"""Module square."""


class Square():
    """Square Class."""

    def __init__(self, *args, **kwargs):
        """Init fuction."""
        my_dic = kwargs
        if 'width' not in my_dic or getattr(my_dic['width']) < 0:
            my_dic['width'] = 0
        if 'height' not in my_dic or getattr(my_dic['height']) < 0:
            my_dic['height'] = 0
        for key, value in my_dic.items():
            setattr(self, key, value)

    def area_of_my_square(self):
        """Area of the square."""
        return self.width * self.height

    def PermiterOfMySquare(self):
        """Perimeter function."""
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """New string function."""
        return "{}/{}".format(self.width, self.height)


if __name__ == "__main__":
    s = Square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.PermiterOfMySquare())
