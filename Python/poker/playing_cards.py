#!/usr/bin/env python

import random

# 花色


class CardColour:
    diamond = 1
    clubs = 2
    heart = 3
    spade = 4
    joker = 5


# 卡牌
class PlayingCards:
    def __init__(self, count=1):
        self._new(count)

    # 牌数
    @property
    def num(self):
        return len(self.cards)

    # 洗牌
    def shuffle(self):
        random.shuffle(self.cards)

    # 理牌
    def sort(self):
        self.cards.sort()

    # 复原
    def recovery(self):
        self._new(self.count)

    # 去除
    def filter(self, num=None, color=None):
        num_list = list()
        color_list = list()
        if num:
            if isinstance(num, list):
                num_list.extend(num)
            else:
                num_list.append(num)
        if color:
            if isinstance(color, list):
                color_list.extend(color)
            else:
                color_list.append(color)
        self.cards = [x for x in self.cards if x[0]
                      not in color_list and x[1] not in num_list]

    # 创建牌
    def _new(self, count):
        self.count = count
        self.cards = list()
        for _ in range(count):
            for c in range(1, 5):
                for n in range(1, 14):
                    self.cards.append((c, n))
            self.cards.append((CardColour.joker, 98))
            self.cards.append((CardColour.joker, 99))


if "__main__" == __name__:
    p = PlayingCards()
    p.filter(color=CardColour.joker)
    p.shuffle()
    print(p.cards)
    p.recovery()
    print(p.cards)
