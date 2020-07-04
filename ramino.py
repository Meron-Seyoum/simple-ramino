import random

NUM_OF_CARDS = 13


# Meron S.


def make_deck():
    cards_in_order = list(range(1, 14))

    card_types = ['Spades', 'Clubs', 'Diamonds', 'Hearts']

    complete_deck = []

    for card_type in card_types:
        for card in cards_in_order:
            if card == 11:
                card = "Jack" + " of " + card_type
            elif card == 12:
                card = "Queen" + " of " + card_type
            elif card == 1:
                card = "Ace" + " of " + card_type
            elif card == 13:
                card = "King" + " of " + card_type
            else:
                card = str(card) + " of " + card_type
            complete_deck.append(
                card)  # Create a-104 (basically, 2 full decks combined) deck so the drawing deck does not run out.
    complete_deck *= 2
    return complete_deck


def shuffle_deck(given_deck):
    random.shuffle(given_deck)  # randomly shuffle the cards in the deck


def give_out_cards(given_deck):  # simply hand out cards. 13 is for the opponent and 14 is for the distributor.
    # Then, the distributor gets rid of a card in his first turn without drawing a card.
    shuffle_deck(given_deck)

    givers_hand = []

    opponents_hand = []

    i = 0

    while (i < NUM_OF_CARDS):
        opponents_hand.append(given_deck.pop())
        givers_hand.append(given_deck.pop())
        i += 1
    givers_hand.append(given_deck.pop())

    return (givers_hand, opponents_hand)


def discard_card(given_deck, given_hand_of_cards):
    result = given_hand_of_cards.pop()

    print(len(given_deck))

    return result


def draw_card(given_deck, given_hand_of_cards):
    result = given_deck.pop()

    given_hand_of_cards.append(result)

    print(len(given_deck))

    return result


if __name__ == "__main__":
    deck = make_deck()
    print(deck);
    print("\n")
    shuffle_deck(deck)
    print(deck);
    print("\n")
    own_deck, opponents_deck = give_out_cards(deck)
    print(own_deck);
    print("\n");
    print(opponents_deck);
    print("\n");
    print(len(deck))
    print(discard_card(deck, own_deck))  # initially, the distributor has to discard a card.
    for i in range(15):
        print(discard_card(deck, own_deck))
        print(draw_card(deck, own_deck))

        print(draw_card(deck, opponents_deck))
        print(discard_card(deck, opponents_deck))

        print(len(own_deck))
        print(len(opponents_deck))
