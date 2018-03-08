##############
# Question 7 #
##############

# Which one will print the right grocery purchase?








## A ##
prices = {'apple': 0.40, 'banana': 0.50,'kiwi': 2.0}

my_purchase = {
    'apple': 1,
    'banana': 6
}

grocery_bill = 0
for fruit in my_purchase:
  grocery_bill += (prices[fruit] * my_purchase[fruit])

print ('I owe the grocer', grocery_bill)








## B ##
prices = {'apple': 0.40, 'banana': 0.50}

my_purchase = {
    'apple': 1,
    'banana': 6
}

grocery_bill = 0
for fruit in prices:
  grocery_bill += (my_purchase[fruit] * prices[fruit])

print ('I owe the grocer', grocery_bill)