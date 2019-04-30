# Learn how to convert minutes to hours using Python Programming.
# Source code used in this video: https://www.youtube.com/watch?v=4SRiRpZZ5Qc
# Python code used to convert minutes into hours. 

# ~~~~~~~~~~~~~~~~ #
#  BASIC VERSION   #
# ~~~~~~~~~~~~~~~~ #

def timeConv (num):
  minutes = num % 60
  print ("Minutes: ", minutes)
  hours = (num - minutes)/60
  print ("Hours: ", hours)
  result = str(hours) + " hours " + ": " + str(minutes) + " min. "
  return result

print (timeConv(566))

# ~~~~~~~~~~~~~~~~~~~ #
#  IMPROVED VERSION   #
# ~~~~~~~~~~~~~~~~~~~ #

def timeConv (num):
  print ("You have entered the following number of minutes: ", num)
  minutes = num % 60
  print ("Minutes: ", minutes)
  hours = (num - minutes)/60
  print ("Hours: ", hours)
  result = "{} is equivalent to : ".format(num) + str(hours) + " hours " + ": " + str(minutes) + " min. "
  return result

print (timeConv(566))

# ~~~~~~~~~~~~~~~~~~~~ #
#  GETTING USER INPUT  #
# ~~~~~~~~~~~~~~~~~~~~ #

num = int(input("Please, enter a number: "))
print ("You have entered the following number of minutes: ", num)
minutes = num % 60
print ("Minutes: ", minutes)
hours = (num - minutes)/60
print ("Hours: ", hours)
result = "{} is equivalent to : ".format(num) + str(hours) + " hours " + ": " + str(minutes) + " min. "

print (result)
