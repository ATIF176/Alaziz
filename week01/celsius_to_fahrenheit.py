def celsius_to_fahrenheit():
    cels_temp = float(input("Enter celsius temprature: "))
    fahren_temp = (cels_temp * (9/5)) + 32
    print("Given temprature in fahrenheit is: " + str(fahren_temp) + "F")

celsius_to_fahrenheit()