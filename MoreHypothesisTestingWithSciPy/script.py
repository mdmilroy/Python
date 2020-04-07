import numpy as np
import fetchmaker

rottweiler_tl = fetchmaker.get_tail_length('rottweiler')
print(np.mean(rottweiler_tl), np.std(rottweiler_tl))

whippet_rescue = fetchmaker.get_is_rescue('whippet')
num_whippet_rescue = np.count_nonzero(whippet_rescue)
print(num_whippet_rescue)
num_whippets = np.size(whippet_rescue)
print(num_whippets)


from scipy.stats import binom_test

whippet_binom_test = binom_test(num_whippet_rescue, num_whippets, 0.08)
if whippet_binom_test < 0.05:
  print('Significant Difference!')
else:
  print('No Difference.')
  

from scipy.stats import f_oneway

whippet_avg_weight = fetchmaker.get_weight('whippet')
terrier_avg_weight = fetchmaker.get_weight('terrier')
pitbull_avg_weight = fetchmaker.get_weight('pitbull')
weight_t, weight_pval = f_oneway(whippet_avg_weight, terrier_avg_weight, pitbull_avg_weight)

if weight_pval < 0.05:
  print('There is a difference between these breeds!')
else:
  print('There is no difference between these breeds.')
  

from statsmodels.stats.multicomp import pairwise_tukeyhsd

weight_pw = np.concatenate([whippet_avg_weight, terrier_avg_weight, pitbull_avg_weight])
weight_labels = ['whippet'] * len(whippet_avg_weight) + ['terrier'] * len(terrier_avg_weight) + ['pitbull'] * len(pitbull_avg_weight)

tukey_results = pairwise_tukeyhsd(weight_pw, weight_labels, 0.05)
print(tukey_results)


poodle_colors = fetchmaker.get_color('poodle')
shihtzu_colors = fetchmaker.get_color('shihtzu')
color_table = [
  [np.count_nonzero(poodle_colors == 'black'), np.count_nonzero(shihtzu_colors == 'black')], [np.count_nonzero(poodle_colors == 'brown'), np.count_nonzero(shihtzu_colors == 'brown')],
[np.count_nonzero(poodle_colors == 'gold'), np.count_nonzero(shihtzu_colors == 'gold')],
[np.count_nonzero(poodle_colors == 'grey'), np.count_nonzero(shihtzu_colors == 'grey')],
[np.count_nonzero(poodle_colors == 'white'), np.count_nonzero(shihtzu_colors == 'white')]]
print(color_table)

from scipy.stats import chi2_contingency

t, pval, df, n = chi2_contingency(color_table)
print(pval)

