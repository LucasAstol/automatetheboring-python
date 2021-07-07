import time, random

questions= {}

for i in range(10):
    tries = 1
    num1 = random.randint(0,9)
    num2 = random.randint(0,9)

    while tries < 4:
        try:
            response = int(input('question %s: %s * %s' % (i+1, num1, num2) ))
            if response == num1*num2:
                print('Correct!')
                time.sleep(1)
                questions.setdefault('q'+str(i+1), 'OK')
            else:
                tries += 1
                if tries == 4:
                    questions.setdefault('q'+str(i+1), 'NOK')
                continue
            break
        except Exception:
            tries += 1
            if tries == 4:
                    questions.setdefault('q'+str(i+1), 'NOK')

for key in questions.keys():
    print(key + ': ' + questions.get(key))
    


