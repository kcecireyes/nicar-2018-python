##############
# Question 6 #
##############

# Which script will print "puebla" only once?








## A ##
for x in xrange(1,8):
  if x % 2 == 0:
    if x % 3 == 0:
      print ('chicago')
    print ('puebla')
  print ('karachi')








## B ##
for x in xrange(1,8):
  if (x % 2 == 0) and (x % 3 == 0):
    print ('chicago')
  if x % 2 == 0:
    if x % 3 == 0:
      print ('puebla')
  print ('karachi')