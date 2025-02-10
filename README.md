# statistical-simulation-blackjack-card-counting-strategies

## Project Overview

This project is a statistical simulation analyzing the effectiveness of the **Hi-Lo Card Counting Strategy** in Blackjack. The simulation uses **Monte Carlo methods** to estimate the long-term effects of card counting on bankroll growth and win rates.

### Mathematical Analysis of Card Counting

The **Hi-Lo system** assigns values to cards:
- **High cards (10, J, Q, K, A)** → **-1**
- **Mid-value cards (7, 8, 9)** → **0**
- **Low cards (2, 3, 4, 5, 6)** → **+1**

#### Running Count ($RC$) and True Count ($TC$):
The running count updates dynamically as cards are drawn:
$$RC = \sum \text{Card Values Seen}$$

The **True Count** adjusts for the number of decks remaining:
$$TC = \frac{RC}{	ext{Decks Remaining}}$$

#### Statistical Expected Value Calculation:
For each round, the **expected value (EV)** of a bet is calculated:
$$EV = \sum_{i} P_i \cdot W_i$$
Where:
- $P_i$ is the probability of outcome $i$
- $W_i$ is the associated win/loss amount

When the **True Count is positive**, the expected value increases, indicating an advantage. The **Kelly Criterion** helps determine bet sizing:
$$f^* = \frac{p(b+1) - 1}{b}$$
Where:
- $p$ is the probability of winning
- $b$ is the net fractional odds of winning
- $f^*$ is the optimal fraction of bankroll to bet

### Monte Carlo Simulation
Monte Carlo methods simulate thousands of hands to statistically evaluate bankroll growth, variance, and the probability of long-term profitability.

## Folder Structure
```
project-root/
├── scripts/
│   ├── 01_simulation.py               # Runs Monte Carlo simulations
│   ├── 02_analysis.py                 # Analyzes results
├── outputs/                            # Stores simulation results
│   ├── results.csv
│   ├── analysis_plots/
├── requirements.txt                    # Dependencies
├── README.md                           # Project documentation
```

## Usage
### 1. Setup the Project:
Clone the repository.
Ensure you have Python installed.
Install required dependencies using the requirements.txt file:
```sh
pip install -r requirements.txt
```

### 2. Run the Blackjack Simulation
Execute the script to simulate multiple hands of Blackjack:
```sh
python scripts/01_simulation.py
```
This will generate a results CSV file in the `outputs/` folder.

### 3. Analyze the Results
To generate statistical analysis and visualizations:
```sh
python scripts/02_analysis.py
```
This will display graphs showing bankroll trends and card counting effectiveness.

## Requirements
- Python 3.8+
- Pandas
- Matplotlib