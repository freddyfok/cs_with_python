from dataclasses import dataclass
from typing import List, Optional


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)


@dataclass
class Increments:
    quality: Optional[int]
    sellin: int


class LegendaryItem(Exception):
    pass


def legendary_item():
    raise LegendaryItem()


def _cal_pass_value(num_of_days):
    if num_of_days > 10:
        return Increments(1, -1)
    elif num_of_days > 5:
        return Increments(2, -1)
    elif num_of_days > 0:
        return Increments(3, -1)
    else:
        return Increments(None, -1)


SPECIAL_ITEMS = {
    "Aged Brie": lambda n: Increments(1, -1)
    , "Sulfuras, Hand of Ragnaros": lambda n: legendary_item()
    , "Backstage passes to a TAFKAL80ETC concert": lambda n: _cal_pass_value(n)
    , "Conjured Mana Cake": lambda n: Increments(-2, -1)
}


class GildedRose:
    def __init__(self, items: List[Item]):
        self.items = items

    def update_quality(self):
        for item in self.items:
            try:
                increment = SPECIAL_ITEMS.get(item.name, lambda n: Increments(-1, -1))(item.sell_in)
            except LegendaryItem:
                continue
            item.sell_in += increment.sellin
            if increment.quality is None:
                item.quality = 0
            elif item.sell_in < 0:
                item.quality += 2 * increment.quality
            else:
                item.quality += increment.quality
            if item.quality > 50:
                item.quality = 50
            if item.quality < 0:
                item.quality = 0
