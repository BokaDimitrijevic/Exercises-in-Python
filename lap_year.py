def is_leap_year(year):
    """Given a year, return True if it is a leap year, else return False"""
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        return True
    return False
    
year=int(input("Input a year:"))
print(is_leap_year(year))