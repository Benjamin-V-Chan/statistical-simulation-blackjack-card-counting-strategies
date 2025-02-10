class CardCountingStrategy:
    def __init__(self):
        self.running_count = 0
        self.decks_remaining = 6  # Starts with 6 decks

    def hi_lo_count(self, card):
        if card in range(2, 7):
            self.running_count += 1
        elif card in [10, 11, 12, 13, 1]:
            self.running_count -= 1

    def true_count(self):
        return self.running_count / max(1, self.decks_remaining)