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
        Updates the quality of all items in the inventory each day.
        Sulfuras does not have to be sold, nor decreases in quality.
        """
        for item in self.items:
            if item.name.lower() == "sulfuras, hand of ragnaros":
                continue
            elif item.name.lower() == "aged brie":
                self._aged_brie_update(item)
                continue
            elif item.name.lower() == "backstage passes to a tafkal80etc concert":
                self._backstage_passes_update(item)
                continue
            elif item.name.lower() == "conjured party hat":
                self._conjured_party_hat_update(item)
                continue
            else:
                self._normal_update(item)
                continue

    def _normal_update(self, item: "Item") -> None:
        """
        Updates the quality and sell-in values for a normal item.
        A normal item reduces in quality and sell-in each day.
        After sell_in drops to 0, quality reduces twice as fast.

        Args:
            item (Item): The item to update.
        """
        if item.quality > 0:
            item.quality -= 1
        item.sell_in -= 1
        if item.sell_in < 0 and item.quality > 0:
            item.quality -= 1

    def _backstage_passes_update(self, item: "Item") -> None:
        """
        Updates the quality and sell-in values for a 'Backstage Passes' item.
        'Backstage Passes' increase in quality as sell_in increases, but drops to 0 after the concert.

        Args:
            item (Item): The item to update.
        """
        if item.quality < 50:
            item.quality += 1
        if item.sell_in < 11 and item.quality < 50:
            item.quality += 1
            if item.sell_in < 6:
                item.quality += 1
            item.sell_in -= 1
            if item.sell_in < 0:
                item.quality = 0

    def _aged_brie_update(self, item: "Item") -> None:
        """
        Updates the quality and sell-in values for an 'Aged Brie' item.
        'Aged Brie' increases in quality the older it gets.

        Args:
            item (Item): The item to update.
        """
        if item.quality < 50:
            item.quality += 1
        item.sell_in -= 1
        if item.sell_in < 0 and item.quality < 50:
            item.quality += 1

    def _conjured_party_hat_update(self, item):
        """
        Updates the quality and sell-in values for a "Conjured Party Hat" item.
        'Conjured Party Hat' degrades in quality twice as fast as normal items.

        Args:
            item (Item): The item to update.
        """
        if item.quality > 1:
            item.quality -= 2
        item.sell_in -= 1
        if item.sell_in < 0 and item.quality > 1:
            item.quality -= 2


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
