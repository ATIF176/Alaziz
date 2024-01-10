def earning_calculater():
    working_hours = float(input("Enter your working hours: "))
    rate_per_hour = float(input("Enter rate per hour: "))
    earning = working_hours * rate_per_hour
    print("Your weekly earning is: " + str(earning))

earning_calculater()