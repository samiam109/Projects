import random

num = random.randint(1,8)

EIGHTBALL={
    1: "Yes, everything is OK",
    2: "No, everything is not OK",
    3: "Ask again in 10 minutes",
    4: "You'll have your hearts desires",
    5: "You'll have a house ",
    6: "You're going to need a loan",
    7: "Just lay down",
    8: "Life's short. Enjoy yourself",
}

print(EIGHTBALL[num])
