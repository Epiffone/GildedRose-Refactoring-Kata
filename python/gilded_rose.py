# -*- coding: utf-8 -*-


class GildedRose(object):

    def __init__(self, items):
        self.items = items

    # def update_quality(self):
    #     for item in self.items:
    #         if item.name != "Aged Brie" and item.name != "Backstage passes to a TAFKAL80ETC concert":
    #             if item.quality > 0:
    #                 if item.name != "Sulfuras, Hand of Ragnaros":
    #                     item.quality = item.quality - 1
    #         else:
    #             if item.quality < 50:
    #                 item.quality = item.quality + 1
    #                 if item.name == "Backstage passes to a TAFKAL80ETC concert":
    #                     if item.sell_in < 11:
    #                         if item.quality < 50:
    #                             item.quality = item.quality + 1
    #                     if item.sell_in < 6:
    #                         if item.quality < 50:
    #                             item.quality = item.quality + 1
    #         if item.name != "Sulfuras, Hand of Ragnaros":
    #             item.sell_in = item.sell_in - 1
    #         if item.sell_in < 0:
    #             if item.name != "Aged Brie":
    #                 if item.name != "Backstage passes to a TAFKAL80ETC concert":
    #                     if item.quality > 0:
    #                         if item.name != "Sulfuras, Hand of Ragnaros":
    #                             item.quality = item.quality - 1
    #                 else:
    #                     item.quality = item.quality - item.quality
    #             else:
    #                 if item.quality < 50:
    #                     item.quality = item.quality + 1

    def update_quality(self):
        for item in self.items:
            if item.name.lower() not in [
                "aged brie",
                "backstage passes to a tafkal80etc concert",
                "sulfuras, hand of ragnaros",
            ]:
                self._normal_update(item)
                continue

            elif item.name.lower() == "sulfuras, hand of ragnaros":
                continue

            elif item.name.lower() == "aged brie":
                item.quality = item.quality + 1 if item.quality < 50 else item.quality
                item.sell_in = item.sell_in - 1
                if item.sell_in < 0:
                    if item.quality < 50:
                        item.quality = item.quality + 1

            elif item.name.lower() == "backstage passes to a tafkal80etc concert":
                item.quality = item.quality + 1 if item.quality < 50 else item.quality
                if item.sell_in < 11:
                    if item.quality < 50:
                        item.quality = item.quality + 1
                if item.sell_in < 6:
                    if item.quality < 50:
                        item.quality = item.quality + 1
                item.sell_in = item.sell_in - 1
                if item.sell_in < 0:
                    item.quality = item.quality - item.quality

    def _normal_update(self, item):
        if item.quality > 0:
            item.quality = item.quality - 1
            item.sell_in = item.sell_in - 1
            if item.sell_in < 0:
                if item.quality > 0:
                    item.quality = item.quality - 1


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
