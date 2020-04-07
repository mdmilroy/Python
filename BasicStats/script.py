import codecademylib3_seaborn
import pandas as pd
import numpy as np
from weather_data import london_data

# Viewing random data points further into the dataset
print(london_data.iloc[950:975])
print(len(london_data))

# Average Temperature for 2015
temperature_c = london_data['TemperatureC']
avg_temp_c = np.mean(temperature_c)
# print(avg_temp_c)

# Variance in Temperature for 2015
temp_c_var = np.var(temperature_c)
temp_c_std = np.std(temperature_c)
# print(temp_c_std)

# June Temperature information
june = london_data.loc[london_data['month'] == 6]['TemperatureC']
june_avg = np.mean(june)
# print('June Average Temp: ', str(round(june_avg, 2)))
june_std = np.std(june)
# print('June Std Dev: ', str(round(june_std, 2)))

# July Temperature information
july = london_data.loc[london_data['month'] == 7]['TemperatureC']
july_avg = np.mean(july)
# print('July Average Temp: ', str(round(july_avg, 2)))
july_std = np.std(july)
# print('July Std Dev: ', str(round(july_std, 2)))

# Let's see the average and std of every month in 2015
for i in range(1, 13):
  month = london_data.loc[london_data['month'] == i]['TemperatureC']
  print('The average temperature for the month of ' + str(i) + ' is ' + str(round(np.mean(month), 2)))
  print('The standard deviation for the month of ' + str(i) + ' is ' + str(round(np.std(month), 2)) + '\n')

# What about rain measurements?
for i in range(1, 13):
  rain = london_data.loc[london_data['dailyrainMM'] == i]['month']
  print('The average rainfall for the month of ' + str(i) + ' is ' + str(round(np.mean(rain), 2)))
  print('The standard deviation for rain in the month of ' + str(i) + ' is ' + str(round(np.std(rain), 2)) + '\n')

# Hottest and Coldest Days
warmest = london_data.loc[london_data['TemperatureC'].idxmax()]
print('The warmest temp of ' + str(warmest['TemperatureC']) + ' was measured on ' + str(warmest['Time']))

coldest = london_data.loc[london_data['TemperatureC'].idxmin()]
print('The coldest temp of ' + str(coldest['TemperatureC']) + ' was measured on ' + str(coldest['Time']))