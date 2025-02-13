

#   F I L E   O P E R A T I O N S



import os

# Creating and Writing to a file
f= open("demofile.txt", "w")
f.write("Woops! I have deleted the content!")
f.close()




# Reading the file content
f= open("demofile.txt", "r")
print(f.read())


# Appending to the file
f = open("demofile.txt", "a")
f.write("Now the file has more content!")
f.close()



# indicates error if file exists otherwise create file

# f= open("mynewfile.txt", "x")




# Reading the file line by line
print("\nReading the file line by line:")
f= open("demofile.txt", "r")
for line in f:
        print(line, end="")

# Checking if file exists
print("\n\nChecking if the file exists:")
if os.path.exists("example.txt"):
    print("The file exists.")
else:
    print("The file does not exist.")

#  Deleting the file
print("\nDeleting the file:")
if os.path.exists("example.txt"):
    os.remove("example.txt")
    print("File deleted successfully.")
else:
    print("The file does not exist.")
