'''
You have been provided with ‘leeds-central-air-quality.csv’ which is a file containing air quality data for Leeds from the last few years. There are 4 values – particulate matter (25), particulate matter (10), Ozone and Nitrous Oxide which are all different measures of air quality – which are recorded against the date.
Load this file into a suitable data structure.

From this data, create a line plot of the average of the 4 data points against the date.

For example, for the row:
07/09/2024,68,20,25,5

You would plot a point at (68+20+25+5)/4 = 29.5

The X-axis should be the date, the Y-axis should be the average pollution.
'''
'''Student Name: Hashim Ali
Student ID: 201967833'''

import matplotlib.pyplot as plt
import pandas as pd

x = []
y = []

# Read CSV file
data = pd.read_csv("leeds-centre-air-quality.csv", header=None, skiprows=1)
# Iterate through each row in CSV file
for i, row in data.iterrows():
    if row.isnull().all():
        break
    x.append(row[0])
    # Calculate average of 4 values
    y.append((int(row[1]) + int(row[2]) + int(row[3]) + int(row[4]))/4)

# Plot the graph
plt.plot(x, y)

plt.title("Student Name: Hashim Ali | rdks0284 | 201967833")
plt.xlabel("date")
plt.ylabel("average pollution")
plt.savefig("PLOT.png")


