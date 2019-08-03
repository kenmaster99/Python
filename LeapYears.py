import calendar
yyyy = int(input('Enter the Years : '))
print(calendar.calendar(yyyy, 2, 2, 6, 3))

def leap(years):
    if (years % 4) == 0:
        if (years % 100) == 0:
            if (years % 400) == 0:
                return "Leap Years"
            else:
                return "Not Leap Years"
        else:
            return "Leap Years"
    else:
        return "Not Leap Years"
    


leap(yyyy)