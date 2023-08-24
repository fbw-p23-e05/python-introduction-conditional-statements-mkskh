scale = input("Input the scale shortcut you'd like to convert (F - Fahrenheit, C - Celsius) : ")
temp = int(input("Input the value of temperature you'd like to convert  : "))

if scale == 'F':
    convert = (5 / 9) * (temp - 32)
    print('The temperature in Celsius is', round(convert, 1), 'degrees.')
elif scale == 'C':
    convert = ((9 / 5) * temp) + 32
    print('The temperature in Fahrenheit is', int(convert), 'degrees.')
else:
    None