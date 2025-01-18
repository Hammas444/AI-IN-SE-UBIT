var = 100
if var == 200:
 print ("1 - Got a true expression value")
 print (var)
elif var == 150:
 print ("2 - Got a true expression value")
 print (var)
elif var == 100:
 print("3 - Got a true expression value")
 print(var)
else:
 print("4 - Got a false expression value")
 print (var)
print ("Good bye!")











# ---------------------Example: 01 --------------------

# Print square root of negative or positive number using if and operators.


a= int(input("Enter a Number and I'll get its square root : "))

if (a>0):
 print("The Number you entered is greater than 0 ,so I can Calculate it!")
 root = a**(1/2)
 print("The square root of %d is %f" % (a,root))

if(a<=0):
 print("I can't calculate square root of a negative number!")

print("Thanks for the input!")







# ---------------------Example: 02 --------------------
# Write conditional statements to print value of 0 to 1 and 1 to 0 and numbers in between



b= int(input("Enter a Number"))


if(b==1):
 b=0

if(b==0):
 b=1

if(b>2 or b<0):
 print("You have entered number between")

print(b)



# ---------------------Example: 03 --------------------


c= int(input("Enter a number between 10-20: "))

if (c>=10 and c<=20):
 print("The condition has been met.")

else:
 print("You did it wrong.")




 # ---------------------Example: 04 --------------------


c= int(input("Enter a number between 10-20 or 30-40: "))

if ((c>=10 and c<=20) or (c>=30 and c<=40)):
 print("The condition has been met.")

else:
 print("You did it wrong.")











 # ---------------------Loops --------------------




 # ---------------------Example: 01-------------------

i=1

while(i<=100):
    print("Karachi Pakistan")
    i=i+1
    



f=100

while(f>=1):
    print("Moscow Russia")
    f=f-1
 




  # ---------------------Example: 02-------------------
# Take collection of number input from user. Print the total positive and negative number.

pcount=0
ncount=0


count= int(input("How many numbers you want? "))
i=1

while(i<=count):
    num=int(input("Enter number: "))
    if(num>0):
        pcount=pcount+1
    else:
        ncount=ncount+1
    i=i+1
print("Positive number count: ",pcount)
print("Negative number count: ",ncount)




  # ---------------------Example: 03-------------------

# Fixed a Letter from a to e and then ask the user to guess that letter until correct letter entered.


value= 'c'

uservalue= input("Guess the letter from a to e: ")
while(uservalue!=value):
    print("Incorrect")
    uservalue= input("Guess the letter from a to e: ")
print("Welcome User")























