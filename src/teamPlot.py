import json
import matplotlib.pyplot as plt
import pandas

# Load Json Data
matches = pandas.read_json ('../eCrawler/matches.json')
# Generate frequencies
matchCount1 = matches['team1'].value_counts(sort=False)
matchCount2 = matches['team2'].value_counts(sort=False)
matchCount = (matchCount1 + matchCount2).sort_index()
print(matchCount)

dayMatches = matches['date'].value_counts(sort=True).sort_index()

# Init plot
plt.close('all')
plt.figure()

# Plot teans
plt.subplot(2, 1, 1)
matchCount.head(20).sort_index().plot(kind='bar')
plt.subplot(2, 1, 2)
dayMatches.head(20).sort_index().plot(kind='bar')

# Show plot
plt.show()
