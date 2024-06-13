from datetime import date, datetime

class Person():
    def __init__(self, name, country, date_of_birth):
        self.name = name
        self.country = country
        self.date_of_birth = datetime.strptime(date_of_birth, "%Y-%m-%d").date()
    
    def calc_age(self):
        today = date.today()
        if (today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day):
            age = today.year - self.date_of_birth.year - 1
        else:
            age = today.year - self.date_of_birth.year
        
        # Calculate remaining months and days
        if today.month < self.date_of_birth.month or (today.month == self.date_of_birth.month and today.day < self.date_of_birth.day):
            months = (12 - self.date_of_birth.month) + today.month
        else:
            months = today.month - self.date_of_birth.month
        
        # Calculate remaining days
        if today.day < self.date_of_birth.day:
            days = (date(today.year, today.month - 1, self.date_of_birth.day) - date(today.year, today.month - 1, today.day)).days
        else:
            days = today.day - self.date_of_birth.day

        return age, months, days
    
name = input("Enter your name: ")
country = input("Enter your country name: ")
date_of_birth = input("Enter your date of birth (YYYY-MM-DD): ")

person = Person(name, country, date_of_birth)

print("Name:", person.name)
print("Country:", person.country)
print("Date of birth:", person.date_of_birth)
age, months, days = person.calc_age()
print("Age:", age, "years,", months, "months,", days, "days")
