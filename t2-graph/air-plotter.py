'''
You have been provided with ‘leeds-central-air-quality.csv’ which is a file containing air quality data for Leeds from the last few years. There are 4 values – particulate matter (25), particulate matter (10), Ozone and Nitrous Oxide which are all different measures of air quality – which are recorded against the date.
Load this file into a suitable data structure.

From this data, create a line plot of the average of the 4 data points against the date.

For example, for the row:
07/09/2024,68,20,25,5

You would plot a point at (68+20+25+5)/4 = 29.5

The X-axis should be the date, the Y-axis should be the average pollution.
'''

import matplotlib.pyplot as plt
import pandas as pd



x = []
y = []

data = pd.read_csv("leeds-centre-air-quality.csv", header=None, skiprows=1)
for i, row in data.iterrows():
    if row.isnull().all():
        break
    x.append(row[0])
    y.append((int(row[1]) + int(row[2]) + int(row[3]) + int(row[4]))/4)

plt.plot(x, y)

plt.title("Student Name: Hashim Ali")
plt.xlabel("date")
plt.ylabel("average pollution")
plt.savefig("PLOT.png")


