numUser = int(input('Enter a number '))

def collatz(number):
    if number % 2 == 0:
        print(str(number // 2))
        return number // 2
    else:
        print(str(3 * number + 1))
        return 3 * number + 1

while numUser != 1:
    numUser = collatz(numUser)


