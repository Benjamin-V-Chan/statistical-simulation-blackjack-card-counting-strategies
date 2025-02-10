import csv
import random

class BlackjackGame:
    def __init__(self):
        self.deck = [value for value in range(1, 14)] * 4 * 6  # 6 decks
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

class CardCountingStrategy:
    def __init__(self):
        self.running_count = 0
        self.decks_remaining = 6

    def hi_lo_count(self, card):
        if card in range(2, 7):
            self.running_count += 1
        elif card in [10, 11, 12, 13, 1]:
            self.running_count -= 1

    def true_count(self):
        return self.running_count / max(1, self.decks_remaining)

class BlackjackSimulation:
    def __init__(self, rounds=10000):
        self.rounds = rounds
        self.results = []

    def run_simulation(self):
        game = BlackjackGame()
        strategy = CardCountingStrategy()
        bankroll = 1000

        for _ in range(self.rounds):
            game_result = game.play_round()
            for card in game_result["player_hand"] + game_result["dealer_hand"]:
                strategy.hi_lo_count(card)

            if game_result["result"] == "win":
                bankroll += 10
            else:
                bankroll -= 10

            self.results.append((strategy.true_count(), bankroll))

        self.save_results()

    def save_results(self):
        with open("outputs/results.csv", "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["True Count", "Bankroll"])
            writer.writerows(self.results)

if __name__ == "__main__":
    sim = BlackjackSimulation(10000)
    sim.run_simulation()