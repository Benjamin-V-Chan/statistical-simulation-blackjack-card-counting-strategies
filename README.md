# statistical-simulation-blackjack-card-counting-strategies

## Project Overview

This project is a statistical simulation analyzing the effectiveness of the **Hi-Lo Card Counting Strategy** in Blackjack. The simulation uses **Monte Carlo methods** to estimate the long-term effects of card counting on bankroll growth and win rates.

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
- NumPy
- Pandas
- Matplotlib