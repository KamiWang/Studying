
from poker.playing_cards import PlayingCards


def upstream_dealer(count=1):
    poker = PlayingCards(count)
    poker.shuffle()
    while poker.cards:
        yield poker.cards.pop()
