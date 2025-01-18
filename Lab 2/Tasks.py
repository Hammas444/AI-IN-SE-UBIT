
  # ---------------------LAB EXERCISES-------------------


  # ---------------------Exercise: 01-------------------



# Cabinets and Boxes are objects that are mostly in cubic shape. Make a program that takes 
# inputs like height, width and depth from user and then calculate volume of the cube:
# volume = height ∗ width ∗ depth
# After calculating volume of cube, compare it with following ranges and print the relevant label:
# Volume Range Label
# 1 cm3 – 10 cm3 (Extra Small)
# 11 cm3 – 25 cm3 (Small)
# 26 cm3 – 75 cm3 (Medium)
# 76 cm3 – 100 cm3 (Large)
# 101 cm3 – 250 cm3 (Extra Large)
# 251 cm3 and above (Extra-Extra  Large)





print("\n--- Calculate Volume of a Cube ---")
height = float(input("Enter height (cm): "))
width = float(input("Enter width (cm): "))
depth = float(input("Enter depth (cm): "))

volume = height * width * depth
print(f"Calculated Volume: {volume} cm³")

if 1 <= volume <= 10:
        label = "Extra Small"
elif 11 <= volume <= 25:
        label = "Small"
elif 26 <= volume <= 75:
        label = "Medium"
elif 76 <= volume <= 100:
        label = "Large"
elif 101 <= volume <= 250:
        label = "Extra Large"
elif volume > 250:
        label = "Extra-Extra Large"
else:
        label = "Invalid Volume"

print(f"Volume Label: {label}")







  # ---------------------Exercise: 02-------------------

# In a company ,worker efficiency is determined on the basis of the time required for a worker 
# to complete a particular job.If the time taken by the worker is between 2-3 hours then the worker 
# is said to be highly efficient. If the time required by the worker is between 3-4hours,then the worker 
# is ordered to improve speed. If the time taken is between 4-5 hours ,the worker is given training to 
# improve his speed ,and if the time taken by the worker is more than 5 hours ,then the worker haas 
# to leave the company, If the time taken by the worker is input through the keyboard,find the 
# efficiency of the worker.



print("\n--- Worker Efficiency ---")
time_taken = float(input("Enter time taken by the worker (hours): "))

if 2 <= time_taken <= 3:
        print("The worker is highly efficient.")
elif 3 < time_taken <= 4:
        print("The worker is ordered to improve speed.")
elif 4 < time_taken <= 5:
        print("The worker is given training to improve speed.")
elif time_taken > 5:
        print("The worker has to leave the company.")
else:
        print("Invalid time entered.")





  # ---------------------Exercise: 03-------------------

# The program must prompt the user for a username and password. The program should 
# compare the password given by the user to a known password. If the password matches, the 
# program should display “Welcome!” If it doesn’t match, the program should display “I don’t 
# know you.
# Note: the password should not be case sensitive and it’s value is abc$123 or ABC$123




# Simplified Login System
print("\n--- Login System ---")
username = input("Enter username: ")  # Prompt for username
password = input("Enter password: ")  # Prompt for password

# Check if the entered password matches (case-insensitive)
if password.lower() in ["abc$123".lower(), "ABC$123".lower()]:
    print(f"Welcome, {username}!")  # Success message
else:
    print("I don’t know you.")  # Failure message









# ---------------------Exercise: 04-------------------

#(i) What Would Python Print?

n = 3
while n >= 0:
    n -= 1
    print(n)


# (ii): What Would Python Print?

# n = 4
# while n > 0:
#     n += 1
#     print(n)









# ---------------------Exercise: 05-------------------

# Make a program that lists the countries in the set


clist = ['Canada', 'USA', 'Mexico', 'Australia']

for country in clist:
    print(country)





# 1. Create a loop that counts from 0 to 100

for i in range(101):  # Range generates numbers from 0 to 100
    print(i)



# 2. Make a multiplication table using a loop

num = int(input("Enter a number for multiplication table: "))
for i in range(1, 11):  # Multiplying from 1 to 10
    print(f"{num} x {i} = {num * i}")




# 3. Output the numbers 1 to 10 backwards using a loop

for i in range(10, 0, -1):  # Start at 10, stop before 0, step -1
    print(i)



# 4. Create a loop that counts all even numbers to 10

for i in range(0, 11, 2):  # Start at 0, go up to 10, step by 2
    print(i)



# 5. Create a loop that sums the numbers from 100 to 200

total = 0
for i in range(100, 201):  # Loop from 100 to 200 (inclusive)
    total += i
print(f"Sum of numbers from 100 to 200: {total}")





# ---------------------Exercise: 06-------------------


 # 1. Make a program that lists the countries in the set below using a while loop.
# clist = 
# ["Canada","USA","Mexico"]

clist = ["Canada", "USA", "Mexico"]

i = 0
while i < len(clist):  # Loop until the end of the list
    print(clist[i])
    i += 1  # Increment the index



# 2. What’s the difference between a while loop and a for loop?

# | Feature	 |             WHILE LOOP	                                           
# | Purpose	 |Repeats as long as a condition is true.	               
# | Condition|Uses a condition that is evaluated before each iteration.
# | Control	 |Requires explicit control (e.g., updating a variable).
# | Use Case |Best for loops with unknown iteration count (e.g.,user input or dynamic conditions).



# | Feature	 |              FOR LOOP
# | Purpose	 |Iterates over a sequence (e.g., list, range, string).
# | Condition|Automatically stops when the sequence is exhausted.
# | Control	 |Handles the iteration automatically.
# | Use Case |Best for loops with a known range or collection.






# 3. Can you sum numbers in a while loop?

n = 1
total = 0
while n <= 10:  # Sum numbers from 1 to 10
    total += n
    n += 1
print(f"Sum: {total}")
# Output: Sum: 55


# 4. Can a for loop be used inside a while loop?

n = 0
while n < 3:  # Outer while loop
    print(f"While loop iteration: {n}")
    for i in range(1, 4):  # Inner for loop
        print(f"  For loop iteration: {i}")
    n += 1

