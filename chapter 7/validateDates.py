import re

def isDateValid(day, month, year):
    monthsWith30 = [4,6,9,11]
    validDate = False
    dayInt = int(day)
    monthInt=int(month)
    yearInt=int(year)
    if(monthInt in monthsWith30):
        if (dayInt > 0 and dayInt < 31):
            validDate = True 
    elif(monthInt == 2):
        if((yearInt % 4 == 0 and yearInt % 100 != 0) or (yearInt %4 == 0 and yearInt % 100 == 0 and yearInt % 400 == 0)):
            if dayInt > 0 and dayInt < 30:
                validDate = True
        else:
            if dayInt > 0 and dayInt < 29:
                validDate = True
    elif(dayInt > 0 and dayInt < 32):
        validDate = True
    return validDate

def validateTheDates(theDate):
    dateRegex = re.compile(r'([0-3][1-9])/([0-1][1-9])/(\d{1,4})')
    validOnes = []
    for group in dateRegex.findall(theDate):
        day = group[0]
        month = group[1]
        year = group[2]
        if(isDateValid(day,month,year)):
            validOnes.append(day + '/' + month + '/'+ year)
    
    if(validOnes.__sizeof__() > 0):
        return 'Valid dates are: \n' + '\n'.join(validOnes)
    else:
        return "There aren't any valid dates"    


print(validateTheDates('28/02/2020 02/03/4567 65/89/25415  251/01/2020   31/12/2021  29/02/2021 14/u/098'))