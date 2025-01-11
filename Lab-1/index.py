a=20

b=10

if(a<b):
    print("a is greater than b")



elif(b==a):  print("a is greater than b") 



c = a+b
d = 1==0
print(d)






name = 'Pakistan'
print(dir(name))

print(name.find('P'))
message = 'Python is fun'

# check if the message ends with fun
print(message.endswith("fun"))

print(message.startswith("Python"))


text = 'bat ball'

# replace 'ba' with 'ro'
replaced_text = text.replace('ba', 'ro')
print(replaced_text)


text = 'Python is fun'

# split the text from space
print(text.split())








# Temperature conversion from Celsius to Fahrenheit
celsius = float(input("Enter temp in Celsius: "))

# Conversion formula from Celsius to Fahrenheit
fahrenheit = (celsius * 9/5) + 32

# Display the result for Celsius to Fahrenheit
print(f"Temperature in Fahrenheit is: {fahrenheit}")

# Temperature conversion from Fahrenheit to Celsius
fahrenheit = float(input("Enter temp in Fahrenheit: "))

# Conversion formula from Fahrenheit to Celsius
celsius = (fahrenheit - 32) * 5/9

# Display the result for Fahrenheit to Celsius
print(f"Temperature in Celsius is: {celsius}")









# Swapping 4 variables
a, b, c, d = 2, 56, 78, 9

# Display values before swapping
print("Before swapping:")
print(f"a={a}, b={b}, c={c}, d={d}")

# Perform swapping
a, b, c, d = d, c, b, a

# Display values after swapping
print("After swapping:")
print(f"a={a}, b={b}, c={c}, d={d}")
