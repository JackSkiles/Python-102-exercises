#Asks the user to input a number based on day of the week
day = input('Day (0-6)? ')

#Changes the string entered to an integer
day = int(day)

#reads user input of 'day' and decides what to print based on the number
if day == 0:
    print('That day is Sunday')
elif day == 1:
    print('That day is Monday')
elif day == 2:
    print('That day is Tuesday')
elif day == 3:
    print('That day is Wednesday')
elif day == 4:
    print('That day is Thursday')
elif day == 5:
    print('That day is Friday')
elif day == 6:
    print('That day is Saturday. I will drink to that!')
else:
    print('That is not a day of the week')