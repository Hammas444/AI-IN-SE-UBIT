# ////////////// Task 1  L I S T ////////////////////



fruits = ['mango','apple','grapes','strawberry','banana']
vegetables = ['tomato','potato','cucumber']
print(fruits)
print(fruits[0])
print(fruits+vegetables)
print(fruits[-2])
print(fruits.pop())
fruits.append('pineapple')
print(fruits)

fruits[-1] = 'watermelon'
print(fruits)
print(fruits[0:3])
print(len(fruits))






ListOfLists = [['Hamees','Babar','Rizwan'],[20,30,32],['H','B','R']]
print(ListOfLists)
print(ListOfLists[0][-1])
print(ListOfLists[2].pop())
print(ListOfLists)
print(dir(fruits))
fruits.sort()
print(fruits.count('mango'))
print(fruits.index('apple'))
print(fruits)
fruits.reverse()
print('Reversed List:',fruits)
fruits.insert(0,'blueberry')
print(fruits)
fruits.append('pomegrenade')
print(fruits)    
fruits.extend(vegetables)
print(fruits)









# ////////////// Task 2  L I S T ////////////////////
# Problem of counting the number of strings where the string length is 2 or more,
# and the first and last character are the same


def count_matching_strings(strings):
    count = 0
    for s in strings:
        if len(s) >= 2 and s[0] == s[-1]:
            count += 1
    return count

# Sample list
sample_list = ['abc', 'xyx', 'aba', '1221']
result = count_matching_strings(sample_list)
print("Expected Result:", result)









#  Write a list comprehension which, from a list, generates a lowercased version of each string that has
# length greater than five.


sample_list2 = ["HELLO", "WORLD", "PYTHON", "PROGRAMMING", "EXAMPLES", "AI"]
print(sample_list2)
print("result:")
for s in sample_list2:
    if(len(s)>5):
        print(s.lower())



# Write a Python program to print a specified list after removing the 0th, 4th and 5th elements
# Sample List : ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow',’Teapink’]
# Expected Output : ['Green', 'White', 'Black']

SampleList = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
SampleList.remove('Red')
SampleList.remove('Pink')
SampleList.remove('Yellow')
print("After Removing: ",SampleList)