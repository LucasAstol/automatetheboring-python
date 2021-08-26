#! python3
# countdown.py - Will start a countdownfrom 60 and playa sound when itgets to 0.

import time, subprocess

timeLeft = 60
while timeLeft > 0:
    print(timeLeft)
    time.sleep(1)
    timeLeft = timeLeft - 1

subprocess.Popen(['start', 'C:\\Lucas\\Cicatriz\\01-Descansando.wav'], shell = True)

