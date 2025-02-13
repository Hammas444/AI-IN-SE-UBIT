import CustomModule



# C U S T O M   M O D U L E

CustomModule.greeting("Bill Gates")


a= CustomModule.person1["name"]
print(a)









# A R R A Y ' S    B A S I C S 


# Creating an array using a list
numbers = [1, 2, 3, 4, 5]

# Accessing elements
print(numbers[0])  # Output: 1

# Modifying elements
numbers[2] = 10
print(numbers)  # Output: [1, 2, 10, 4, 5]

# Appending new elements
numbers.append(6)
print(numbers)  # Output: [1, 2, 10, 4, 5, 6]

# Removing an element
numbers.remove(4)
print(numbers)  # Output: [1, 2, 10, 5, 6]

# Length of the array
print(len(numbers))  # Output: 5


Cars = ["Kia","Toyota", "Ford","Honda", "Suzuki"]



for x in Cars:
 print(x)










# L A M B D A


# Lambda function that adds 10 to a number
add_ten = lambda x: x + 10
print(add_ten(5))  # Output: 15



# Lambda function that adds two numbers
add_numbers = lambda x, y: x + y
print(add_numbers(3, 4))  # Output: 7




# Lambda function that returns 'Even' or 'Odd' based on the input number
is_even = lambda x: 'Even' if x % 2 == 0 else 'Odd'
print(is_even(10))  # Output: Even
print(is_even(7))   # Output: Odd




# Using lambda with map to square each number in a list
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x ** 2, numbers))
print(squared_numbers)  # Output: [1, 4, 9, 16, 25]



# Using lambda with filter to get even numbers from a list
numbers = [1, 2, 3, 4, 5, 6]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # Output: [2, 4, 6]



