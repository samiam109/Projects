import random

nums = str(1234567)
fortune = str(random.choice(nums))
#fortune = str(random.randint(1,7))

q = open('quotes.txt', 'r')

for line in q:
    if line[0] == fortune:
        with open('fortune.txt', 'w') as f:
            f.write(line)

q.close()
