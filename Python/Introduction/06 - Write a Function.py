
def is_leap(year):
    leap = False
    
    # Write your logic here
    if(year % 4 == 0 and year != 2100):
        leap = True
    return leap
