# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):

    def test_normal_item_updates_quality_and_sell_in(self):
        items = [Item("foo", 1, 1)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].sell_in, 0)
        self.assertEqual(items[0].quality, 0)

    def test_sell_by_date_passes_item_degrades_twice_as_fast(self):
        items = [Item("foo", 0, 2)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].sell_in, -1)
        self.assertEqual(items[0].quality, 0)

    def test_item_quality_never_becomes_negative(self):
        items = [Item("foo", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 0)

    def test_aged_brie_increases_in_quality(self):
        items = [Item("Aged Brie", 1, 49)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 50)

    def test_aged_brie_double_increases_in_quality_after_sell_by(self):
        items = [Item("Aged Brie", 0, 48)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 50)

    def test_item_quality_never_exceeds_50(self):
        items = [
            Item("Aged Brie", 1, 50),
            Item("Backstage passes to a TAFKAL80ETC concert", 1, 50),
        ]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 50)
        self.assertEqual(items[1].quality, 50)

    def test_sulfuras_item_attributes_never_decrease(self):
        items = [Item("Sulfuras, Hand of Ragnaros", 1, 80)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].sell_in, 1)
        self.assertEqual(items[0].quality, 80)

    def test_backstage_passes__quality_changes_as_it_approaches_sell_in(self):
        items = [
            Item("Backstage passes to a TAFKAL80ETC concert", 10, 0),
            Item("Backstage passes to a TAFKAL80ETC concert", 5, 0),
            Item("Backstage passes to a TAFKAL80ETC concert", 0, 1),
        ]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 2)
        self.assertEqual(items[1].quality, 3)
        self.assertEqual(items[2].quality, 0)

    def test_conjured_party_hat_degrades_twice_as_fast_as_normal(self):
        items = [Item("Conjured Mana Cake", 2, 2), Item("Conjured Mana Cake", 0, 4)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].sell_in, 1)
        self.assertEqual(items[0].quality, 0)
        self.assertEqual(items[1].sell_in, -1)
        self.assertEqual(items[1].quality, 0)


if __name__ == "__main__":
    unittest.main()
