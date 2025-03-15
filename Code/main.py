from compute_dispersion import DispersionCalculator

filename = "prices.txt"
calculator = DispersionCalculator(filename)

range_value, mean_value, variance_value, std_dev_value, iqr_value = calculator.compute_dispersion()

print(f"Range: {range_value}")
print(f"Mean: {mean_value:.2f}")
print(f"Variance: {variance_value:.2f}")
print(f"Standard Deviation: {std_dev_value:.2f}")
print(f"Interquartile Range (IQR): {iqr_value}")

calculator.visualize_data()
