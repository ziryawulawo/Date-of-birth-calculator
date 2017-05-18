#Calculate the day someone was born
import datetime
import calendar
Age = int(input("Enter your age:")) #This inputs my current age
MOB = int(input("Enter your month of birth:"))#This inputs the month of birth
DOB = int(input("Enter your date of birth:")) #This inputs the date of birth
DateNow = datetime.datetime.now()
DaysPerYear = 365
DaysLived = Age*DaysPerYear  
RDOBTD = datetime.timedelta(days = DaysLived)#calcualtes the date of birth
#This inputs the real date of birth
RDOB = DateNow-RDOBTD
#YOB means year of birth
YOB = int(RDOB.strftime("%Y"))
#prints the Actual Date Of Birth
ADOB = datetime.date(YOB,MOB,DOB)
print (ADOB.strftime('You were born on %A %dth %Y'))


input("Guess it was an easy calculator, was it?")
