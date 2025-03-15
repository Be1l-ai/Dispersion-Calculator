# Dispersion Calculator

This project calculates statistical measures of dispersion (range, variance, standard deviation, and interquartile range) from a dataset of toothpaste prices stored in a file. It also visualizes the data using a Box and Whisker plot.

## Features
- Reads price data from an external text file (`prices.txt`)
- Computes:
  - Range
  - Mean
  - Variance
  - Standard Deviation
  - Interquartile Range (IQR)
- Generates a Box and Whisker plot to visualize price distribution
- Implements a class-based structure for clean and reusable code

## Installation & Setup
1. Clone this repository:
   ```sh
   git clone https://github.com/Be1l-ai/Dispersion-Calculator.git
   ```
2. Navigate to the project folder:
   ```sh
   cd dispersion-calculator
   ```
3. Install dependencies:
   ```sh
   pip install numpy matplotlib
   ```

## Usage
1. Ensure `prices.txt` contains the dataset (one price per line).
2. Run the script:
   ```sh
   python main.py
   ```
3. The output will display the computed dispersion measures and generate a Box and Whisker plot.

For detailed explanations of how the script works, refer to [Documentation.md](Documentation.md).
