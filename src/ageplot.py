import json
import matplotlib.pyplot as plt
import pandas as pd

with open('../eCrawler/players.json') as json_file:
	players = json.load(json_file)
	ages = [int(player['age'].split()[0]) for player in players]
	plt.hist(ages, bins=range(min(ages) - 1,max(ages) + 2))
	plt.title("Histogram with 'auto' bins")
	plt.show()