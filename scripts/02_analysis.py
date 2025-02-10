import pandas as pd
import matplotlib.pyplot as plt

class BlackjackAnalysis:
    def __init__(self, file_path="outputs/results.csv"):
        self.data = pd.read_csv(file_path)

    def plot_bankroll(self):
        plt.figure(figsize=(10, 5))
        plt.plot(self.data["Bankroll"], label="Bankroll over time")
        plt.xlabel("Simulation Round")
        plt.ylabel("Bankroll")
        plt.title("Effect of Card Counting on Bankroll")
        plt.legend()
        plt.show()

    def plot_true_count_histogram(self):
        plt.figure(figsize=(8, 4))
        plt.hist(self.data["True Count"], bins=20, alpha=0.7)
        plt.xlabel("True Count")
        plt.ylabel("Frequency")
        plt.title("Distribution of True Count")
        plt.show()

if __name__ == "__main__":
    analysis = BlackjackAnalysis()
    analysis.plot_bankroll()
    analysis.plot_true_count_histogram()