import random


test1 = random.randint(0, 10000)

test1 = test1 %2


if test1 == 1:
    print('play gow')
else:
    print('play er')