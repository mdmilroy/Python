import codecademylib
import pandas as pd

visits = pd.read_csv('visits.csv',
                     parse_dates=[1])
cart = pd.read_csv('cart.csv',
                   parse_dates=[1])
checkout = pd.read_csv('checkout.csv',
                       parse_dates=[1])
purchase = pd.read_csv('purchase.csv',
                       parse_dates=[1])
print(visits.head(5))
print(cart.head(5))
print(checkout.head(5))
print(purchase.head(5))

v_to_cart = pd.merge(visits, cart, how='left')
print(v_to_cart)
no_num = v_to_cart[v_to_cart.cart_time.isnull()]
no_num = float(len(no_num))
print(no_num)

percent_no_cart = (no_num / len(v_to_cart.cart_time)) * 100
print(percent_no_cart)

# Now on to cart --> checkout
c_to_c = pd.merge(cart, checkout, how='left')
print(c_to_c)
no_checkout = c_to_c[c_to_c.checkout_time.isnull()]
no_checkout = float(len(no_checkout))
print(no_checkout)
percent_no_checkout = (no_checkout / len(c_to_c.checkout_time)) * 100
print(percent_no_checkout)

all_data = pd.merge(visits, cart, how='left').merge(cart, how='left').merge(checkout, how='left').merge(purchase, how='left')
print(all_data.head(5))

all_no_cart = all_data[all_data.cart_time.isnull()]
all_no_cart = float(len(all_no_cart))
percent_all_no_cart = (all_no_cart / len(all_data.cart_time)) * 100
print '% no cart', percent_all_no_cart
all_no_checkout = all_data[all_data.checkout_time.isnull()]
all_no_checkout = float(len(all_no_checkout))
percent_all_no_checkout = (all_no_checkout / len(all_data.checkout_time)) * 100
print '% cart no checkout', percent_all_no_checkout
all_no_purchase = all_data[all_data.purchase_time.isnull()]
all_no_purchase = float(len(all_no_purchase))
percent_all_no_purchase = (all_no_purchase / len(all_data.purchase_time)) * 100
print '% checkout no purchase', percent_all_no_purchase

print 'Weakest link in flow: % checkout no purchase ', percent_all_no_purchase
# How to increase rate of finishing a purchase once in checkout?

all_data['time_to_purchase'] = all_data.purchase_time - all_data.visit_time
print all_data.time_to_purchase
print(all_data.time_to_purchase.mean())
# Average time from visit to purchase is about 45 minutes


