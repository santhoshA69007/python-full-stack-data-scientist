#convert years to weeks python program
def convert(in_year):
    days_left=32850-(in_year*365)
    year_left=90-in_year
    months_left=year_left*12
    weeks_left=year_left*52
   
    return f"years left on earth for u is {year_left} years {months_left} months ,{weeks_left} weeks and {days_left} days"
in_year=int(input("Enter the number of years: "))
print(convert(in_year))