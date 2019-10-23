import json
import matplotlib.pyplot as plt
import pandas

# Load Json Data
players = pandas.read_json ('../eCrawler/players.json')

# Fix ages
players['age'] = [(age.split()[0]) for age in players['age']]

# Generate frequencies
ages = players['age'].value_counts(sort=False).sort_index()
countries = players['country'].value_counts(sort=False).sort_index()

# Checking for duplicates
nicks = players['nick'].value_counts()
names = players['name'].value_counts()
print(nicks)
print(names)


# Init plot
plt.close('all')
plt.figure()

# Plot ages
plt.subplot(2, 1, 1)
ages.plot(kind='bar')

# Plot countries
plt.subplot(2, 1, 2)
countries.plot(kind='bar')

# Show plot
plt.show()
