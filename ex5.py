from datetime import datetime

year_of = input("Enter year of birth :  ")
month_of = input("Enter month of birth : ")
day_of = input("Day of birth : ")

delta = datetime.now() - datetime(int(year_of), int(month_of), int(day_of))
delta_sec = delta.total_seconds()

print ("Happy " + str(delta_sec) + " seconds anniversary !")

