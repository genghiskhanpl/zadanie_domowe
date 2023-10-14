unit = input('is this temperature in celsius of fahrenheit (C/F): ')
temp = float(input('enter temp: '))

if unit == "C":
    temp = round((9 * temp) / 5 + 32, 1)
    print(f"The temperature in Fahrenheit is: {temp} F")
elif unit == "F":
    temp = round((temp - 32) * 5 / 9, 1)
    print(f"The temperature in Celsious is: {temp} C")
else:
    print(f"{unit} is invalid of measurement")
