import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file
data = pd.read_csv('fitness-data.csv')

# Display the first few rows of the DataFrame
print(data.head())

# Extract data
x = data['x']
y = data['y']

# Create a plot
plt.plot(x, y, marker='o', linestyle='--', color='r')

# Add a title
plt.title('Line Plot from CSV Data')

# Add x and y labels
plt.xlabel('X Axis')
plt.ylabel('Y Axis')

# Show the plot
plt.grid(True)
plt.show()
