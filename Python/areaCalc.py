""" A calculator to calculate the area of a circle or triangle"""

from math import pi
from time import sleep
from datetime import datetime

now = datetime.now()
print "Calculator Engine Starting!"
print "%s/%s/%s %2d:%d" % ( now.day, now.month, now.year, now.hour, now.minute)


sleep(1)

hint = "Don't forget to inclue the correct units! \nExiting..."
option = raw_input("Enter C for Circle or T for Triangle: ")
option = option.upper()

if option == "C":
  radius = float(raw_input("Enter the radius of your Circle: "))
  area = pi*radius**2
  print "The pie is baking..."
  sleep(1)
  print "%02d\n%s" % (area, hint)
