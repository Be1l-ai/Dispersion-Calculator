import numpy as np
import matplotlib.pyplot as plt

class DispersionCalculator:
    def __init__(self, filename):
        self.prices = self.read_prices(filename)
    
    def read_prices(self, filename):
        """Reads the toothpaste prices from a file and returns a list of prices."""
        with open(filename, 'r') as file:
            prices = [int(line.strip()) for line in file]
        return prices
    
    def compute_dispersion(self):
        """Computes range, variance, standard deviation, and interquartile range."""
        range_value = max(self.prices) - min(self.prices)
        mean_value = np.mean(self.prices)
        variance_value = np.var(self.prices, ddof=1)
        std_dev_value = np.sqrt(variance_value)
        q1 = np.percentile(self.prices, 25)
        q3 = np.percentile(self.prices, 75)
        iqr_value = q3 - q1
        
        return range_value, mean_value, variance_value, std_dev_value, iqr_value
    
    def visualize_data(self):
        """Creates a Box and Whisker plot for the dataset."""
        plt.boxplot(self.prices, vert=False, patch_artist=True, boxprops=dict(facecolor="lightblue"))
        plt.title("Box and Whisker Plot of Toothpaste Prices")
        plt.xlabel("Price (PHP)")
        plt.show()
