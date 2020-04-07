import codecademylib
import pandas as pd

ad_clicks = pd.read_csv('ad_clicks.csv')
print(ad_clicks.head(5))

utm_count = ad_clicks.groupby('utm_source').user_id.count().reset_index()
print(utm_count)

ad_clicks['is_click'] = ~ad_clicks.ad_click_timestamp.isnull()
print(ad_clicks.head(5))

clicks_by_source = ad_clicks.groupby(['utm_source', 'is_click']).user_id.count().reset_index()
print(clicks_by_source)


clicks_pivot = clicks_by_source.pivot(columns='is_click', index='utm_source', values='user_id').reset_index()
print(clicks_pivot)

clicks_pivot['percent_clicked'] = (clicks_pivot[True] / (clicks_pivot[True] + clicks_pivot[False])) * 100
print(clicks_pivot)

samples = ad_clicks.groupby('experimental_group').user_id.count().reset_index()
print(samples)

control_or_experimental = ad_clicks.groupby(['experimental_group', 'is_click']).user_id.count().reset_index()
print(control_or_experimental)

c_or_e_pivot = control_or_experimental.pivot(columns='is_click', index='experimental_group', values='user_id').reset_index()
print(c_or_e_pivot)

a_clicks = ad_clicks[ad_clicks.experimental_group == 'A']
b_clicks = ad_clicks[ad_clicks.experimental_group == 'B']

a_clicks_day = a_clicks.groupby(['is_click', 'day']).user_id.count().reset_index()
b_clicks_day = b_clicks.groupby(['is_click', 'day']).user_id.count().reset_index()
a_clicks_pivot = a_clicks_day.pivot(columns='is_click', index='day', values='user_id')
b_clicks_pivot = b_clicks_day.pivot(columns='is_click', index='day', values='user_id')
a_clicks_pivot['percent_A'] = (a_clicks_pivot[True] / (a_clicks_pivot[True] + a_clicks_pivot[False])) * 100
b_clicks_pivot['percent_B'] = (b_clicks_pivot[True] / (b_clicks_pivot[True] + b_clicks_pivot[False])) * 100
print(a_clicks_pivot, b_clicks_pivot)
a_clicks_pivot['percent_B'] = (b_clicks_pivot['percent_B'])
print(a_clicks_pivot)

#Based on the findings, Group A received the most clicks overall. On Tuesdays, however, Group B received slightly more clicks. Group A is recommended for the advertisement moving forward.