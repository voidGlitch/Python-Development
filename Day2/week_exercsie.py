age  = input("your current age is \n")
age_int = int(age)

year_remaining = 90-age_int
days_remaining = year_remaining * 365
weeks_remaining = year_remaining * 52
months_remining = year_remaining * 12

print(f"you have left {days_remaining} days {weeks_remaining} weeks and {months_remining} months")