import codecademylib
import numpy as np

calorie_stats = np.genfromtxt('cereal.csv', delimiter=',')

average_calories = np.mean(calorie_stats)
print 'Competitor Average Calories:', average_calories

calorie_stats_sorted = np.sort(calorie_stats)
print calorie_stats_sorted

median_calories = np.median(calorie_stats)
print 'Median Competitor Calories:', median_calories

nth_percentile = np.percentile(calorie_stats, 4)
more_calories = np.mean(calorie_stats > 60)
percent_more_calories = more_calories * 100
print 'Percent with More Calories:', percent_more_calories

calorie_std = np.std(calorie_stats)
print 'Average Spread in Data:', calorie_std

"""
CrunchieMunchies is well below the average calorie count of its competitors. 
The data shows over 96 percent of competitor products have more calories than 
Yummy Corp's CrunchieMunchies. Not only this, but the product calories are 
typically 20 calories apart. With CrunchieMunchies being less than 96 percent
of calorie counts for cereals, other products are well above the average of 
106 calories; this shows the significance of this product's market standing.
""" 
