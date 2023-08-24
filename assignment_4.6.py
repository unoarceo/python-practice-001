"""
Prompts for the hours worked and the hourly rate then displays the gross pay.
Calculates for overtime pay at 1.5x the rate for hours in excess of 40.
"""

def computepay(h, r):
    #excess = h - 40.0
    #grosspay = (40.0 * r) + (excess * r * 1.5)

    if h>40.0:
        return (40.0 * r) + ((h - 40.0) * r * 1.5)
    else :
        return h * r

hrs = input("Enter Hours:")
rate = input("Enter Rate:")
p = computepay(float(hrs), float(rate))

print("Pay", p)