#Prompts for the hours worked and the hourly rate then displays the gross pay.

hrs = input("Enter Hours: ")
rate = input("Enter Rate: ")
print("Pay: " + str(float(hrs) * float(rate)))