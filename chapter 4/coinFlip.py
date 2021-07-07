import random

numberOfStreaks = 0

for experimentNumber in range(10000):
    coinFlips = []
    for x in range (100):
        if random.randint(0, 1) == 0:
            coinFlips.append('H')
        else:
            coinFlips.append('T')

    #hStreak = 0
    #tStreak = 0

    streak = 1
    for i in range(1,100):
        if coinFlips[i] == coinFlips[i-1]:
            streak += 1
        else:
            streak = 1

        if streak == 6:
            numberOfStreaks += 1
            break

print('Chance of streak: %s%%' % (numberOfStreaks/100))