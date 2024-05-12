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
                Updater(item, False, 50, 1).update()
            elif item.name.lower() == "backstage passes to a tafkal80etc concert":
                Updater(item, False, 50, 1, True).update()
            elif item.name.lower() == "conjured mana cake":
                Updater(item, True, 1, 2).update()
            else:
                Updater(item, True, 0, 1).update()


class Updater:
    """
    Class to manage the updating of an item's quality and sell-in values.

    Attributes:
        item (Item): The item to be updated.
        does_quality_degrade (bool): Flag to indicate if the item's quality degrades over time.
        qual_min_max (int): The minimum or maximum quality limit depending on degradation.
        qual_mod (int): The amount by which the quality changes.
        special_increase (bool): Flag to indicate if the item has special rules for quality increase.
    """

    def __init__(
        self,
        item: GildedRose,
        does_quality_degrade: bool,
        qual_min_max: int,
        qual_mod: int,
        special_increase: bool = False,
    ) -> None:
        """
        Initializes the Updater with the item and its update rules.

        Args:
            item (Item): The item to be updated.
            does_quality_degrade (bool): If the item's quality degrades over time.
            qual_min_max (int): The minimum or maximum quality limit.
            qual_mod (int): The modification value for the item's quality.
            special_increase (bool): If the item has special rules for quality increase.
        """
        self.item = item
        self.does_quality_degrade = does_quality_degrade
        self.qual_min_max = qual_min_max
        self.qual_mod = qual_mod
        self.special_increase = special_increase

    def update(self) -> None:
        """
        Updates the quality and sell-in values for the item based on its rules.
        """
        if self.does_quality_degrade:
            if self.item.quality > self.qual_min_max:
                self.item.quality -= self.qual_mod
        else:
            if self.item.quality < self.qual_min_max:
                self.item.quality += self.qual_mod

        if self.special_increase:
            if self.item.sell_in < 11 and self.item.quality < 50:
                self.item.quality += self.qual_mod
                if self.item.sell_in < 6:
                    self.item.quality += self.qual_mod
            if self.item.sell_in - 1 < 0:
                self.item.quality = -1

        self.item.sell_in -= 1
        if self.does_quality_degrade:
            if self.item.sell_in < 0 and self.item.quality > self.qual_min_max:
                self.item.quality -= self.qual_mod
        else:
            if self.item.sell_in < 0 and self.item.quality < self.qual_min_max:
                self.item.quality += self.qual_mod


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
