
#Takes user input and splits it into three parts seperated by a comma and puts them into a list
info = input('Enter these three things seperated by commas. What was your first pets name? what street did you grow up on? An ajective').split(',')

#prints out the list with those three parts in specified order
print('Hello, the ' + info[2] + ' ' + info[0] + ' ' + info[1])