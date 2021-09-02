#! python3
# prettifiedStopwatch.py - stopwatch with justified otuput in console and copies the final output to the clipboard.

#still not ready... download pyperclip module and import it

import time


print('Welcome to prettified Stopwatch.\nTo start the stopwatch and mark laps press Enter / Return key. To terminate the stopwatch press Ctrl + c .' + 
'\nWhen terminated all the info displayed will be copied to the clipboard and ready for you to paste it')
input()
startTime = time.time()
laps = 0
lastLap = startTime
finalInfo = ''
while True:    
    try:
        input()
        
        laps += 1
        lapStopTime = time.time()
        totalTime = str(round(lapStopTime - startTime, 2))
        lapTime = str(round(lapStopTime - lastLap, 2))

        lapInfo = 'Lap # ' + str(laps) + ': ' + totalTime.rjust(8) + '('.rjust(3) + lapTime.rjust(8) + ')'
        finalInfo += lapInfo + '\n'

        print(lapInfo, end='')
        
        lastLap = lapStopTime  
    except KeyboardInterrupt:
        print('\n\n\n The final Info \n')
        print(finalInfo)
        exit()