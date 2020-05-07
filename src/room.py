#!/bin/env python3
# Implement a class to hold room information. This should have name and
# description attributes.

# * Add the ability to add items to rooms.
#   * The `Room` class should be extended with a `list` that holds the `Item`s
#     that are currently in that room.
#   * Add functionality to the main loop that prints out all the items that are
#     visible to the player when they are in that room.
# * Add capability to add `Item`s to the player's inventory. The inventory can
#   also be a `list` of items "in" the player, similar to how `Item`s can be in a
#   `Room`.
from item import get_lit


class Room:
    """
    < Room > is traveled by < Player >
    """
    name = None  # name of Item
    description = None  # description of Item
    items = None  # items in this room
    is_light = None  # true if the room is naturally illuminated

    def __init__(self, name, description, items=[], is_light=True):
        self.name = name
        self.description = description
        self.items = items or []
        self.is_light = is_light

    def __str__(self):
        return f'<Room: {self.name}>'

    def available(self, itemName):
        """
        available < Item >(s) named [itemName]
        """
        return len(list(filter(lambda x: x.name.lower() == itemName.lower(), self.items)))

    def takeItem(self, name):
        """
        take < Item > from room by [name]
        """
        if not self.is_light:
            print(f"good luck finding {name} in the dark.")
            return
        # filter by name
        i = list(filter(lambda x: x.name == name, self.items))
        if not len(i) > 0:
            # if no matches,
            return False
        # if we have a match, find the index number
        idx = self.items.index(i[0])
        # remove it from available items
        removed = self.items.pop(idx)
        if get_lit(removed):
            self.is_light = False
        return removed

    def dropItem(self, item):
        """
        drop < Item > into this room
        """
        self.items.append(item)
        if get_lit(item):
            self.is_light = True
        return f"dropped {item.name}"

    def view(self, *args, **kwargs):
        """
        the room from <Player>'s POV
        """
        return self.description if self.is_light else "It's pitch black!"


if __name__ == "__main__":
    from item import LightSource
    print('creating new Room')
    lambdaSchool = Room("LambdaSchool", "a place for learning how to learn")
    basement = Room(
        "basement", "the basement contains many cardboard boxes", is_light=False)
    lantern = LightSource(
        "a lantern", "a lantern's light burns brightly and illuminates the surrounding area.")
    print(f"{lambdaSchool.name}: {lambdaSchool.view()}")
    print(f"{basement.name}: {basement.view()}")
