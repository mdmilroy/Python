import noshmishmosh
import numpy as np

all_visitors = noshmishmosh.customer_visits
total_visitor_count = len(all_visitors)
paying_visitors = noshmishmosh.purchasing_customers
paying_visitor_count = len(paying_visitors)
print paying_visitor_count

baseline_percent = paying_visitor_count / float(total_visitor_count) * 100
print baseline_percent

payment_history = noshmishmosh.money_spent
average_payment = np.mean(payment_history)
print average_payment
new_customers_needed = np.ceil(1240 / average_payment)
print new_customers_needed

percentage_point_increase = (new_customers_needed * 100) / total_visitor_count

minimum_detectable_effect = 100 * percentage_point_increase / baseline_percent
print minimum_detectable_effect

ab_sample_size = 300