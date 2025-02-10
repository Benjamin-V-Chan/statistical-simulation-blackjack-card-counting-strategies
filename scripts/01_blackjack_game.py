import random

class BlackjackGame:
    def __init__(self):
        self.deck = self.create_deck()
        self.shuffle_deck()

    def create_deck(self):
        return [value for value in range(1, 14)] * 4 * 6  # 6 decks of cards

    def shuffle_deck(self):
        random.shuffle(self.deck)

    def draw_card(self):
        return self.deck.pop() if self.deck else None

    def hand_value(self, hand):
        total = sum(min(10, card) for card in hand)
        aces = hand.count(1)
        while aces > 0 and total + 10 <= 21:
            total += 10
            aces -= 1
        return total

    def play_round(self):
        player_hand = [self.draw_card(), self.draw_card()]
        dealer_hand = [self.draw_card(), self.draw_card()]

        while self.hand_value(player_hand) < 17:
            player_hand.append(self.draw_card())

        while self.hand_value(dealer_hand) < 17:
            dealer_hand.append(self.draw_card())

        player_value = self.hand_value(player_hand)
        dealer_value = self.hand_value(dealer_hand)

        return {
            "player_hand": player_hand,
            "dealer_hand": dealer_hand,
            "player_value": player_value,
            "dealer_value": dealer_value,
            "result": "win" if player_value <= 21 and (dealer_value > 21 or player_value > dealer_value) else "lose"
        }