# Dispersion Calculator Documentation

## Overview
This project defines a class `DispersionCalculator` that reads toothpaste price data from an external text file and computes statistical measures of dispersion, including:
- Range
- Mean
- Variance
- Standard Deviation
- Interquartile Range (IQR)
Additionally, it visualizes the data using a Box and Whisker plot.

## File Structure
The implementation consists of two files:
1. `compute_dispersion.py` – Defines the `DispersionCalculator` class.
2. `main.py` – Imports and uses the class for computation and visualization.

## File Format
The script expects a file (`prices.txt`) containing price values, each on a new line, for example:
```
10
11
12
13
11
12
10
13
10
10
8
8
9
8
9
```

## Class Structure
### 1. `__init__(self, filename)`
   - Reads the prices from the given file and stores them as an attribute.

### 2. `read_prices(self, filename)`
   - Opens and reads `prices.txt`, converting the contents into a list of integers.

### 3. `compute_dispersion(self)`
   - Computes:
     - **Range**: Maximum price minus minimum price.
     - **Mean**: The average of the prices.
     - **Variance**: The average squared deviation from the mean.
     - **Standard Deviation**: The square root of the variance.
     - **Interquartile Range (IQR)**: The difference between the 75th percentile (Q3) and the 25th percentile (Q1).

### 4. `visualize_data(self)`
   - Generates a Box and Whisker plot using Matplotlib.

## Running the Script
Ensure Python is installed along with the required libraries:
```sh
pip install numpy matplotlib
```

### Running the Script
Create `main.py` and use the following code:
```python
from compute_dispersion import DispersionCalculator

filename = "prices.txt"  # The file containing prices
calculator = DispersionCalculator(filename)  # Create an instance of the class

# Compute measures of dispersion
range_value, mean_value, variance_value, std_dev_value, iqr_value = calculator.compute_dispersion()

# Print the results
print(f"Range: {range_value}")
print(f"Mean: {mean_value:.2f}")
print(f"Variance: {variance_value:.2f}")
print(f"Standard Deviation: {std_dev_value:.2f}")
print(f"Interquartile Range (IQR): {iqr_value}")

# Visualize the data
calculator.visualize_data()
```

### Running `main.py`
```sh
python main.py
```
The output will display statistical calculations and a plot representing data distribution.

## Conclusion
This approach makes the script easier to maintain and reuse for different datasets.
