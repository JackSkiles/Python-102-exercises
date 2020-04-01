#Asks the user to input a number based on day of the week
day = input('Day (0-6)? ')

#Changes the string entered to an integer
day = int(day)

#reads user input of 'day' and decides what to print based on the number
if day >= 0 and day < 5:
    print('Its a work day, better get up')
elif day == 5:
    print('Its Friday, your almost there!')
elif day == 6:
    print('Its Saturday!! Celebrate by catching some zzzzs')
else:
    print('Thats not a day of the week. Dont go crazy on me.')