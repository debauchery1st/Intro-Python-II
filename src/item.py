# * Create a file called `item.py` and add an `Item` class in there.
#   * The item should have `name` and `description` attributes.
#      * Hint: the name should be one word for ease in parsing later.
#   * This will be the _base class_ for specialized item types to be declared
#     later.


class Item:
    """
    Contained in some < Room >'s,
    the player may interact with an < Item >
    to unlock mysteries throughout the adventure.

    __base class__ for specialized item types
    """
    name = None
    description = None

    def __init__(self, name="generic item", description="give me a description"):
        self.name = name
        self.description = description

    def __str__(self):
        return f'< Item: {self.name} >'

    def on_take(self, *args, **kwargs):
        try:
            other = args[0]
            other.items.append(self)
        except Exception as e:
            raise e
        print(f"You have picked up {self.name}")

    def on_drop(self, *args, **kwargs):
        print(f"You dropped {self.name}")


class LightSource(Item):
    """
    <Item> illuminates environment
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __str__(self):
        return f"<LightSource: {self.name}"

    def on_drop(self):
        super().on_drop(self)
        print(f"*It's not wise to drop your source of light!")


def get_lit(kls):
    # ? class method
    return isinstance(kls, LightSource)


if __name__ == "__main__":
    print('creating new item')
    laptop = Item(
        "laptop",
        "it's a thankpad C29, equipped with the latest 𝝺eFTL processor.")
    print(laptop)
    print(laptop.description)
    lantern = LightSource(
        "a lantern",
        "a lantern's light burns brightly and illuminates the surrounding area.")
    print(lantern)
    print(lantern.description)
    lantern.on_drop()
    laptop.on_drop()
    get_lit(laptop)
