""""
#Strings
str1 = "Hello"
str2 = "World"
result = str1 + " " + str2
print(result)

############################################################
text = "Python is awesome"
length = len(text)
print("Length of the string:", length)
############################################################

text = "Python is awesome"
uppercase = text.upper()
lowercase = text.lower()
title = text.title()
capital = text.capitalize()
print("Uppercase:", uppercase)
print("Lowercase:", lowercase)
print("capitalize every 1st letter of word:", title)
print("capitalize :", capital)

##################################################################
text = "Python is awesome"
new_text = text.replace("awesome", "great")
print("Modified text:", new_text)

################################################################
text = "Python is awesome"
words = text.split()
print("Words:", words)
##########################################################
text = "   Some spaces around   "
stripped_text = text.strip()
print("Stripped text:", stripped_text)
##############################################################
text = "Python is awesome"
substring = "is"
if substring in text:
    print(substring, "found in the text")
##################################################################
# Float variables
num1 = 5.0
num2 = 2.5

# Basic Arithmetic
result1 = num1 + num2
print("Addition:", result1)

result2 = num1 - num2
print("Subtraction:", result2)

result3 = num1 * num2
print("Multiplication:", result3)

result4 = num1 / num2
print("Division:", result4)

# Rounding
result5 = round(3.14159265359, 2)  # Rounds to 2 decimal places
print("Rounded:", result5)
###############################################################
# Integer variables
num1 = 10
num2 = 5

# Integer Division
result1 = num1 // num2
print("Integer Division:", result1)

# Modulus (Remainder)
result2 = num1 % num2
print("Modulus (Remainder):", result2)

# Absolute Value
result3 = abs(-7)
print("Absolute Value:", result3)
#############################################################
import re

text = "The quick brown fox"
pattern = r"brown"

search = re.search(pattern, text)
if search:
    print("Pattern found:", search.group())
else:
    print("Pattern not found")
#########################################################
import re

text = "The quick brown fox"
pattern = r"quick"

match = re.match(pattern, text)
if match:
    print("Match found:", match.group())
else:
    print("No match")
#########################################
import re

text = "The quick brown fox jumps over the lazy brown dog"
pattern = r"brown"

replacement = "red"

new_text = re.sub(pattern, replacement, text)
print("Modified text:", new_text)
######################################################
import re

text = "The quick brown fox"
pattern = r"brown"

search = re.search(pattern, text)
if search:
    print("Pattern found:", search.group())
    print("Pattern found:", search)  # Pattern found: <re.Match object; span=(10, 15), match='brown'>
else:
    print("Pattern not found")

####################################################################
import re

text = "apple,banana,orange,grape"
pattern = r","

split_result = re.split(pattern, text)
print("Split result:", split_result)
########################################################################

l1 = [1, 2, 3]
for i in l1[:]:
    l1.append(i*i)

print(l1)
###########################################################
#lists  --> not ordered heterogeneous collection of data types which can be mutable
l2 = [ 1, "b" , 3 , "g" , 5,1,5,1,5,3,"b","a","x"]
l3 = [8,5,4,3,2,0,9,89,99,76,2,3]
l2.append("c")
print(l2)
l2.remove("g")
print(l2)
l2.reverse()
print(l2)
l3.sort()
print(l3)
l2.insert(1,"l") # add l at index 1
print(l2)
l3.sort(reverse=True)
print(l3)
print(l2.extend([7,6]))
print(l2.pop())  #removes last
print(l2.pop(1)) # removes index 1
del l2[0]
print(l2)
#list slicing
print(l2[2:6]) # from 2nd index to 5th index
print(l2[::-1])
print(l2[:]) # copy the list
print(l2[:3]) # from 0th index to 2nd index
print(l2[::]) # copy the list
print(l2.count(5))
squares = [x*x for x in range(5)] #list comprehention
print(squares)
###################################################################
#tuples : ordered heterogeneous collection of data types but it is immutable
x = ( 3 , 7 , 4 ,1 , 3 ,6, 1, 8)
print(x)
print(x.count(1))
print(x[4])
print(x[::])
print(x[1:4])
print(x[::-1])
print(x[6:])
print(sum(x))

###########################################################################
#Dictionaries : key - value pair of data 
emp = {"name": "Shreya", "role": "DevOps"}
emp["salary"] = 50000
emp.pop("salary")
print(emp)
del emp["role"]
print(emp)
emp["role"] = "Senior DevOps"
print(emp)
print(emp["name"])
print(emp.get("age", "23"))
print(emp.keys())
print(emp.values())
print(emp.items()) #items and keys are same
for k, v in emp.items():
    print(k, v)
square = {x: x*x for x in range(5)}
print(square)

###########################################################################
#Set : unordered unique elements mutable
s = {1,2,3,3}

a = {1,2,3}
b = {3,4,5}

print(a | b)   # Union
print(a & b)   # Intersection
print(a - b)   # Difference

squares = {x*x for x in range(5)}
print(squares)

lst = [1,2,2,3]
print(set(lst))

#################################################
#Comprehention 
#list
evens = [x for x in range(10) if x % 2 == 0]
print(evens)

#######################################################
#file operations read and write

with open(r"C:\Users\LENOVO\OneDrive\Desktop\Devops\deveops_training\New folder\example\data.txt", "r") as f:
    content = f.read()
    print(content)

# read file line by line
with open(r"C:\Users\LENOVO\OneDrive\Desktop\Devops\deveops_training\New folder\example\data.txt", "r") as f:
    for line in f:
        print(line.strip())

file_path = "C:/Users/LENOVO/OneDrive/Desktop/Devops/deveops_training/New folder/example/data.txt"
with open(file_path,"r") as f:
    lines = f.readlines()
    print(f.tell())   # current position
    print(f.seek(0))  # move pointer

with open(file_path , "w") as f:
    f.write("Hello World devops\n")

with open(file_path , "a") as f:
    f.write("new line appending to check file operation\n")

#######################################################################################
#JSON pracing 
#json.loads() → JSON STRING to Python
import json

json_data = '{"name":"Shreya","age":25}'
python_data = json.loads(json_data)
print(python_data)
print(type(python_data))

data = {"cloud": "AWS", "level": "beginner"}
#json.dumps() → Python to JSON STRING
json_text = json.dumps(data)
print(json_text)
print(type(json_text))

#json.load() → JSON FILE to Python
with open("sample.json") as f:
    data = json.load(f)

print(data)
print(type(data))

#json.dump() → Python to JSON FILE
#indent=4 → makes JSON readable (VERY IMPORTANT)
data = {
    "project": "DevOps",
    "tools": ["Docker", "K8s"]
}

with open("sample.json","a") as f:
    json.dump(data,f,indent=4)
##########################################################################
"""
#Devops modules 
#Module	What it helps with (Simple)
#os	Talk to operating system
#sys	Talk to Python runtime
#subprocess	Run Linux commands
#shutil	Copy / move files
#time	Wait / sleep
#datetime	Date & time handling
#logging	Proper logs
#json	Read/write JSON
#requests	Call APIs
#pathlib	Modern file paths
#re	Search text patterns
#boto3	Talk to AWS

import os

print(os.getcwd())
print(os.listdir())

if not os.path.exists("text"):
    os.mkdir("text")

os.rmdir("text")

print(os.environ.get("USERPROFILE"))





