import codecademylib3_seaborn
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("country_data.csv")

print(data.head(5))
# This data shows Country name, Life Expectancy, and the Country's GDP

# Isolate just the life expectancy data
life_expectancy = data['Life Expectancy']

# Finding quartiles of the data
life_expectancy_quartiles = np.quantile(life_expectancy, [.25, .5, .75])
print(life_expectancy_quartiles)

# Turning to look at GDP
gdp = data['GDP']
median_gdp = np.quantile(gdp, .5)
print(median_gdp)

low_gdp = data[data['GDP'] <= median_gdp]
high_gdp = data[data['GDP'] > median_gdp]

# Comparing quartiles of low vs high GDPs
low_gdp_quartiles = np.quantile(low_gdp['Life Expectancy'], [.25, .5, .75])
print(low_gdp_quartiles)

high_gdp_quartiles = np.quantile(high_gdp['Life Expectancy'], [.25, .5, .75])
print(high_gdp_quartiles)

# Visualizing the data
plt.hist(low_gdp['Life Expectancy'], alpha = .5, label = 'Low GDP')
plt.hist(high_gdp['Life Expectancy'], alpha = .5, label = 'High GDP')
plt.legend()
plt.show()