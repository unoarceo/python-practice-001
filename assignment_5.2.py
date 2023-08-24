"""
5.2 Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'. 
Once 'done' is entered, print out the largest and smallest of the numbers. 
If the user enters anything other than a valid number catch it with a try/except and put out an appropriate message and ignore the number. 
Enter 7, 2, bob, 10, and 4 and match the output below.
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