# General variables
subtotal = "Subtotal: \n$";
discounts = "Discounts: \n$";
tax = "Tax: \n$";
total = "---------- \n Customer Total: \n$";

# Products with descriptions and prices
lovely_loveseat_description = "Lovely Loveseat. Tufted polyester blend on wood. 32 inches high x 40 inches wide x 30 inches deep. Red or white.\n\n";

lovely_loveseat_price = 254.00;

stylish_settee_description = 'Stylish Settee. Faux leather on birch. 29.50 inches high x 54.75 inches wide x 28 inches deep. Black.\n\n';

stylish_settee_price = 180.50;

luxurious_lamp_description = 'Luxurious Lamp. Glass and iron. 36 inches tall. Brown with cream shade.\n\n';

luxurious_lamp_price = 52.15;

# Customer 1 tracking
customer_one_total = 0;
customer_one_itemization = "";

# Sales Info
sales_tax = .088;
military_and_veteran_discount = .20;

customer_one_total += lovely_loveseat_price;
customer_one_itemization += lovely_loveseat_description;

customer_one_total += luxurious_lamp_price;
customer_one_itemization += luxurious_lamp_description;

customer_one_discount = customer_one_total * military_and_veteran_discount;
customer_one_total_with_discount = customer_one_total - customer_one_discount;

customer_one_tax = customer_one_total_with_discount * sales_tax;

customer_one_total_with_discount += customer_one_tax;

# Receipt
print("Customer One Items:\n" + customer_one_itemization);
print(subtotal, round(customer_one_total, 2));
print(discounts, round(customer_one_discount, 2));
print(tax, round(customer_one_tax, 2));
print(total, round(customer_one_total_with_discount, 2));