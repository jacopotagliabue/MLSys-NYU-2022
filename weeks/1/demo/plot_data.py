import json 

import matplotlib.pyplot as plt 
import numpy as np

# Read in the data from disk.
print("Reading in data.json")
with open("data.json", "r") as f:
    data = json.load(f)

# Create x and y arrays from the data.
x = []
y = []
for point in data:
    x.append(point["x"])
    y.append(point["y"])

x = np.array(x)
y = np.array(y)

# Display a scatter plot of the data.
print("Plotting...")
plt.scatter(x, y)
plt.show()

print("All done!")
