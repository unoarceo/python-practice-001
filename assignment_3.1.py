"""
Prompts for the hours worked and the hourly rate then displays the gross pay.
Calculates for overtime pay at 1.5x the rate for hours in excess of 40.
"""

hrs = input("Enter Hours: ")
h = float(hrs)
rate = input("Enter Rate: ")
r = float(rate)

if h <= 40 :
    pay = h * r
elif h > 40 :
    excess = h - 40
    pay = (float(excess) * r * 1.5) + (40 * r)

print(pay)