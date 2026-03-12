birth_year = int(input("Enter your birth year: "))
current_year = 2026

age = current_year - birth_year
print("Your age is:", age)


#another code for age calculater
import datetime

current_year = datetime.datetime.now().year
birth_year = int(input("Enter your birth year: "))

age = current_year - birth_year

print("Your age is:", age)
