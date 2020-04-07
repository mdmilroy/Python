import codecademylib
import numpy as np
from matplotlib import pyplot as plt

survey_responses = ['Ceballos', 'Kerrigan', 'Ceballos', 'Ceballos', 'Ceballos','Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Ceballos', 
'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Ceballos', 'Ceballos', 'Ceballos', 'Ceballos',
'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Ceballos',
'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Ceballos']
print len(survey_responses)
total_ceballos = sum([1 for n in survey_responses if n=='Ceballos'])
print total_ceballos
survey_length = float(len(survey_responses))
percentage_ceballos = (total_ceballos / survey_length) * 100
print percentage_ceballos

possible_surveys = np.random.binomial(survey_length, .54, size=10000) / survey_length

plt.hist(possible_surveys, range=(0,1), bins=20)
plt.show()
possible_surveys_length = float(len(possible_surveys))
incorrect_surveys = len(possible_surveys[possible_surveys < .5])
ceballos_loss_surveys = incorrect_surveys / possible_surveys_length
print ceballos_loss_surveys

new_survey = float(7000)
large_survey = np.random.binomial(new_survey, .54, size=10000) / new_survey
plt.hist(large_survey, bins=20, range=(0,1))
plt.show()

incorrect_large_survey = len(large_survey[large_survey < .5])
ceballos_survey_new = incorrect_large_survey / new_survey
print ceballos_survey_new