#counts all numbers that are multiples of 3 or 5, below 1000
count = 0
count1 = 0
for x in range(3, 1000):
    if int(x/3) == float(x/3.0) or int(x/5) == float(x/5.0):
        count += x

print count

for x in range(3, 1000):
    if x%3 == 0 or x%5 == 0:
        count1 += x

print count1
#Test case to assist with logic
# if float(num) == int(num):
#     print "true"
