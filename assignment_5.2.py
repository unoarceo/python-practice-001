"""
Displays the largest and smallest numbers entered by the user.
Exits when user enters "done".
Displays "Invalid input" when user enters non-numerical values.
Accepts integers only.
"""

def large_test(num_, largest_):
    if largest_ is None :
        largest_ = num_
    elif num > largest_ :
        largest_ = num_
    return largest_

def small_test(num_, smallest_):
    if smallest_ is None :
        smallest_ = num_
    elif num < smallest_ :
        smallest_ = num_
    return smallest_

largest = None
smallest = None

while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    else :
        try :
            num = int(num)
            largest = large_test(num, largest)
            smallest = small_test(num, smallest)
        except :
            print("Invalid input")
            #print(largest, smallest)

print("Maximum is", largest)
print("Minimum is", smallest)