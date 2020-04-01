
#Prompts user to input a number that is a degree in celcius
celcius = input('please input a number in celcius ')

#converts celcius input to integer
celcius = int(celcius)

#creates fahrenheit variable and assigns it the vaule of the conversion formula
#using the user input of celcius
fahrenheit = (celcius * 9/5) + 32

#prints out the information that was calculated
print(f'It is {fahrenheit} degrees in Fahrenheit')