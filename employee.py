"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

from calendar import month


class Employee:
    def __init__(self, name, monthlyWage = 0, hours = 0, hourlyWage = 0, contracts = 0, contractWage = 0, bonus = 0):
        self.name = name
        self.monthlyWage = monthlyWage
        self.hours = hours
        self.hourlyWage = hourlyWage
        self.commisson = contracts * contractWage
        self.bonus = bonus

    def get_pay(self):
        totalPay = self.monthlyWage + (self.hours * self.hourlyWage) + self.commisson + self.bonus
        print(totalPay)
        return totalPay

    def __str__(self):
        return self.name


# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie', monthlyWage = 4000)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie', hours = 100, hourlyWage = 25)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee', monthlyWage = 3000, contracts = 4, contractWage = 220)

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan', hours = 150, hourlyWage = 25, contracts = 3,  contractWage = 220)

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie', monthlyWage = 2000, bonus = 1500)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel', hours = 120, hourlyWage = 30, bonus = 600)
