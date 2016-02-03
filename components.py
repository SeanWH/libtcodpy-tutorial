import math

 
class Object:
    """
    This is a generic object: the player, a monster, an item, the stairs...
    It's always represented by a character on screen.
    """
    def __init__(self, x, y, char, name, color, blocks=False, always_visible=False, fighter=None, ai=None, item=None, equipment=None):
        self.x = x
        self.y = y
        self.char = char
        self.name = name
        self.color = color
        self.blocks = blocks
        self.always_visible = always_visible
        self.fighter = fighter
        self._ensure_ownership(fighter)
 
        self.ai = ai
        self._ensure_ownership(ai)
 
        self.item = item
        self._ensure_ownership(item)
 
        self.equipment = equipment
        self._ensure_ownership(equipment)
 
    def _ensure_ownership(self, component):
        if (component):
            component.set_owner(self)
 
    def distance_to(self, other):
        #return the distance to another object
        dx = other.x - self.x
        dy = other.y - self.y
        return math.sqrt(dx ** 2 + dy ** 2)
 
    def distance(self, x, y):
        #return the distance to some coordinates
        return math.sqrt((x - self.x) ** 2 + (y - self.y) ** 2)