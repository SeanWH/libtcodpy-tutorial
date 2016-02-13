import math


class Rect(object):
    """
    A rectangle on the map. used to characterize a room.
    """
    def __init__(self, x, y, w, h):
        self.x1 = x
        self.y1 = y
        self.x2 = x + max(0, w)
        self.y2 = y + max(0, h)

    def center(self):
        center_x = (self.x1 + self.x2) / 2
        center_y = (self.y1 + self.y2) / 2
        return (center_x, center_y)

    def intersect(self, other):
        """
        Returns true if two rectangles intersect.
        """
        return (self.x1 <= other.x2 and self.x2 >= other.x1 and
                self.y1 <= other.y2 and self.y2 >= other.y1)


class Location(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return (isinstance(other, self.__class__) and
                self.x == other.x and self.y == other.y)

    def __ne__(self, other):
        return not self.__eq__(other)

    def __add__(self, other):
        return Location(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Location(self.x - other.x, self.y - other.y)

    def bound(self, rect):
        if (self.x > rect.x2):
            self.x = rect.x2
        if (self.y > rect.y2):
            self.y = self.y2
        if (self.x < rect.x1):
            self.x = rect.x1
        if (self.y < rect.y1):
            self.y = rect.y1


class Direction(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return (isinstance(other, self.__class__) and
                self.x == other.x and self.y == other.y)

    def __ne__(self, other):
        return not self.__eq__(other)

    def normalize(self):
        """
        Normalize to length 1 (preserving direction), then round and
        convert to integer so the movement is restricted to the map grid.
        """
        distance = math.sqrt(self.x ** 2 + self.y ** 2)
        self.x = int(round(self.x / distance))
        self.y = int(round(self.y / distance))


north = Direction(0, -1)
south = Direction(0, 1)
west = Direction(-1, 0)
east = Direction(1, 0)
northwest = Direction(-1, -1)
northeast = Direction(1, -1)
southwest = Direction(-1, 1)
southeast = Direction(1, 1)
