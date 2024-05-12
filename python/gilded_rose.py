# -*- coding: utf-8 -*-


class GildedRose(object):
    """
    Class to manage the inventory of items in the Gilded Rose store.

    Attributes:
        items (list of Item): The list of items in the store's inventory.
    """

    def __init__(self, items):
        """
        Initializes the Gilded Rose store with a list of items.

        Args:
            items (list of Item): The list of items to be managed.
        """
        self.items = items

    def update_quality(self) -> None:
        """
        Updates the quality of all items in the inventory each day except for 'Sulfuras, Hand of Ragnaros',
        which does not decrease in quality or need to be sold. The quality update rules vary by item type:
        - 'Aged Brie' increases in quality over time.
        - 'Backstage passes to a TAFKAL80ETC concert' have special quality increase rules as the concert date approaches.
        - 'Conjured' items degrade in quality twice as fast as normal items.
        - Other items degrade in quality normally.
        """
        for item in self.items:
            if item.name.lower() == "sulfuras, hand of ragnaros":
                continue
            elif item.name.lower() == "aged brie":
                self.update(item, False, 50, 1)
            elif item.name.lower() == "backstage passes to a tafkal80etc concert":
                self.update(item, False, 50, 1, True)
            elif item.name.lower() == "conjured mana cake":
                self.update(item, True, 1, 2)
            else:
                self.update(item, True, 0, 1)

    def update(
        self, item, does_quality_degrade, qual_min_max, qual_mod, special_increase=False
    ) -> None:
        """
        Modifies the quality and sell-in values for a given item according to predefined rules.

        Args:
            item (Item): The item whose quality and sell-in values are to be updated.
            does_quality_degrade (bool): Indicates if the item's quality degrades over time.
            qual_min_max (int): The minimum or maximum quality threshold, depending on whether the quality degrades.
            qual_mod (int): The amount by which the quality should be modified.
            special_increase (bool): Flag to apply special rules for increasing quality based on sell-in thresholds.
        """
        if does_quality_degrade:
            if item.quality > qual_min_max:
                item.quality -= qual_mod
        else:
            if item.quality < qual_min_max:
                item.quality += qual_mod

        if special_increase:
            if item.sell_in < 11 and item.quality < 50:
                item.quality += qual_mod
                if item.sell_in < 6:
                    item.quality += qual_mod
            if item.sell_in - 1 < 0:
                item.quality = -1

        item.sell_in -= 1
        if does_quality_degrade:
            if item.sell_in < 0 and item.quality > qual_min_max:
                item.quality -= qual_mod
        else:
            if item.sell_in < 0 and item.quality < qual_min_max:
                item.quality += qual_mod


class Item:
    """
    Represents an item in the inventory of the Gilded Rose store.

    Attributes:
        name (str): The name of the item.
        sell_in (int): The number of days to sell the item.
        quality (int): The quality of the item.
    """

    def __init__(self, name, sell_in, quality):
        """
        Initializes an item with a name, sell-in period, and quality.

        Args:
            name (str): The name of the item.
            sell_in (int): The number of days to sell the item.
            quality (int): The quality of the item.
        """
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
