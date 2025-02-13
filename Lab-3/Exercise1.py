

#       E X E R C I S E  : 01




#  a Python program to square and cube every number in a given list of integers using Lambda.


NumbersList = [2, 9, 10, 500]

square = list(map(lambda x: x ** 2, NumbersList))
cube = list(map(lambda x: x ** 3, NumbersList))

print("Squared:", square)
print("Cubed:", cube)



# a Python program to find if a given string starts with a given character using Lambda


StartsWith = lambda strValue, character: strValue.startswith(character)

string = "Pakistan"
char = "P"

print(f"Does '{string}' start with '{char}'? {StartsWith(string, char)}")




#  a Python program to extract year, month, date and time using Lambda


from datetime import datetime

# Get current datetime
CurrDateTime = datetime.now()

# Lambda functions to extract year, month, date, and time
get_year = lambda dt: dt.year
get_month = lambda dt: dt.month
get_date = lambda dt: dt.day
get_time = lambda dt: dt.strftime("%H:%M:%S")  # Extracts time in HH:MM:SS format

# Printing the extracted values
print("Year:", get_year(CurrDateTime))
print("Month:", get_month(CurrDateTime))
print("Date:", get_date(CurrDateTime))
print("Time:", get_time(CurrDateTime))
