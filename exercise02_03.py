#This code is a temperature converter which asks the user for the temperature in Farenhiet and converts the temperature to Celsius and Kelvin, printing these out.
in_temp = input('Enter temperature in Farenhiet:')
ftemp = float(in_temp)
ctemp = (ftemp - 32.0) * 0.5556
ktemp = ctemp + 273.0
print(ctemp, 'Celsius')
print(ktemp, 'Kelvin')