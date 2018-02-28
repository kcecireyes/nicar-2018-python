# Game time!
# NICAR 2018, Nausheen H and Cecilia R

# Instructions:
# Each question will have two scripts,
# choose the one that will output the desired answer
# Beware of errors!

##############
# Question 1 #
##############

# Which one will result in "Sheridan"?

## A ##
streets = [Western, North, Sheridan, Michigan, Clark, Devon]
streets[2]

## B ##
streets = [Western, North, Sheridan, Michigan, Clark, Devon]
streets[3]


##############
# Question 2 #
##############

# Which one will result in the following: set(['a'])?

## A ##
foo = set('oaxaca')
bar = set('cox')
foo - bar

## B ##
foo = set('oaxaca')
bar = set('cox')
foo & bar

##############
# Question 3 #
##############

# Which script will print "I love burgers"?

## A ##
foods = ['pizza', 'burgers', 'hot dogs']
for food in foods:
  print 'I love', food

## B ##

foods = ['pizza', 'burgers', 'hot dogs']
for food in foods:
  if food == foods[1]:
    print 'I love', food

##############
# Question 4 #
##############

# Which script will print 'This is math.' ?

## A ##
x = 6 + 4
if x = 10:
  print 'This is math.'

## B ##
x = 6 + 4
if x == 10:
  print 'This is math.'

# Show how variables and if/elif/else work

##############
# Question 5 #
##############

# Which script will grant access to user `Cecilia`?

## A ##
user1 = "Nausheen"
user2 = "Cecilia"

if username == user1:
    print "Access granted"
else:
    print "Access denied"

## B ##
user1 = "Nausheen"
user2 = "Cecilia"

if username == user1:
    print "Access granted"
else:
    print "Access denied"
elif username == user1:
    print "Welcome to the system"


##############
# Question 6 #
##############

# Which script will print "puebla" only once?

## A ##
for x in xrange(1,8):
  if x % 2 == 0:
    if x % 3 == 0:
      print 'chicago'
    print 'puebla'
  print 'karachi'

## B ##
for x in xrange(1,8):
  if (x % 2 == 0) and (x % 3 == 0):
    print 'chicago'
  if x % 2 == 0:
    if x % 3 == 0:
      print 'puebla'
  print 'karachi'


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

print 'I owe the grocer', grocery_bill

## B ##
prices = {'apple': 0.40, 'banana': 0.50}

my_purchase = {
    'apple': 1,
    'banana': 6
}

grocery_bill = 0
for fruit in prices:
  grocery_bill += (my_purchase[fruit] * prices[fruit])

print 'I owe the grocer', grocery_bill
