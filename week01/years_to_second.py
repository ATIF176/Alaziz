def years_sec():
    living_years = int(input("Enter your living years: "))
    living_seconds = living_years * 365 * 24 * 60 *60
    print("Your living seconds are: " + str(living_seconds))

years_sec()