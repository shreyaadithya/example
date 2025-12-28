"""
#reverse a string
name = "Arunagiri"
print("the reverse of string is" +" "+ name[::-1])
###########################################################

#remove special charecters
import re

text = "DevOps@123!"
clean = re.sub(r'[^a-zA-Z]', '', text)
print(clean)
################################################
#count the vowels
count =0
s = "aeiouhgyljiytv"
for ch in s:
    if ch in "aeiou":
        count = count+1
    else:
        continue 
print(count)

#####################################################
#to find the duplicates
duplicate = 0
s = "programming"
for ch in set(s):
    if s.count(ch) > 1:
        duplicate = duplicate +1
        print(ch)
    else:
        continue
print(duplicate)

########################################################
#list the duplicates in the list 
l1 = [ 1,2,3,4,5,6,7,8,1,2,3,4,1,2,3]
duplicates = []

for i in l1:
    if l1.count(i) > 1 and i not in duplicates:
        duplicates.append(i)
print(duplicates) 

################################################################
#remove duplicates of list
l2 = [1,2,3,4,5,6,7,1,2,3,4,5,6,7,8,9]
print(list(set(l2)))

##############################################################
#Count character frequency
s = "pythonpython frequency"
freq = {}

for ch in s:
    freq[ch] = freq.get(ch, 0) + 1

print(freq)
################################################################
#sort dictionary by value
d = {"a":3, "b":1, "c":2}
print(dict(sorted(d.items(), key=lambda x: x[1])))

##########################################################
#palindrome
name = "aasha" 
if name == name[::-1]:
    print(name + " "+ "is a palindrome")
else:
    print("it's not a palindrome")

##############################################################
#second largest number in the list
l4 = [ 2, 5 , 7 ,9,0,3,7 ,8,10]
print(l4.remove(max(l4)))
print("the second large number of the list is" + " " + str(max(l4)))

#####################################################################
#merge lwo lists
a = [1,2]
b = [3,4]
print(a + b)

##################################################################
#count the words
s1 = "my country is india i love my motherland"
x = s1.split()
print(len(x))

#count the words another approach 
s = "hello world hello"
words = s.split()

count = {}
for w in words:
    count[w] = count.get(w, 0) + 1

print(count)

#################################################################
#check file exists in that perticular absolute path 
import os

file_path = r"C:/Users/LENOVO/OneDrive/Desktop/Devops/deveops_training/New folder/example/data.txt"

if os.path.exists(file_path):
    with open(file_path, "r") as f:
        print(f.read())
else:
    print("data.txt file not found")

##########################################################################
#Read file and print content
file_path = r"C:/Users/LENOVO/OneDrive/Desktop/Devops/deveops_training/New folder/example/data.txt"
with open(file_path , "r") as f:
    print(f.read())

###############################################################################
#count the number of lines in a file
count = 0
with open(file_path,"r") as f:
    for i in f.readlines():
        count = count+1
print(count)

#########################################################################
#count the number of words in the file
count = 0
with open(file_path, "r") as f:
    for i in f.readlines():
        count = count + len(i.split())
print(count) 

##########################################################################
#count the charecter frequency
fre = {}
with open(file_path, "r") as f:
    for line in f:
        for ch in line:
            fre[ch] = fre.get(ch,0)+1
print(fre)

##########################################################################
# search word in file 
pattern = "new"
with open(file_path,"r") as f:
    for line in f:
        if pattern in line:
            found = True
            print("we hove found the pattern")
            break
        else:
            continue
##########################################################################
#Copy the file content
with open(file_path) as src , open("dest.txt","a") as dst:
    dst.write(src.read())

#########################################################################
#remove empty lines
with open("dest.txt") as f:
    for line in f:
        x = line.strip()
        print(x)
##########################################################################
#read file safely
try:
    with open("open.txt","r") as f:
        print(f.read())
except FileNotFoundError:
    print("file not found")

#########################################################################
# find the longest line
longest = {}
with open("dest.txt","r") as f:
    for line in f:
        if len(line) > len(longest):
            longest = line
    print(longest)
##########################################################################
# print the last N lines of the file
N = 1
with open("dest.txt","r") as f:
    line = f.readlines()
    print(line[-N]) # this will print line
    print(line[-N:]) # this will print as list

##############################################################################
# replace the content in a file 
with open("f1.txt" ,"r") as f:
    content = f.read()

content = content.replace("file" , "sample")

with open("f1.txt","w") as f1:
    f1.write(content)

#####################################################################
# file merging
with open("f1.txt") as s1 , open("f2.txt") as s2 , open("dest.txt","w") as out:
    out.write(s1.read())
    out.write(s2.read())

#####################################################################
# logfile analysis --devops question 
error_count = 0

with open("logfile.txt","r") as f:
    for line in f:
        if "ERROR" in line:
            error_count = error_count +1
print(error_count)

############################################################################
#CSV-like parsing (no library)
with open("data.txt") as f:
    for line in f:
        parts = line.strip().split(",")

        if len(parts) == 2:
            name, age = parts
            print(name, age)
        else:
            print("Skipping invalid line:", line.strip())
################################################################################
#print only unique words in file

words = set()
with open("data.txt","r") as f :
    for line in f:
        for w in line.split():
            words.add(w)
print(words)

##############################################3#####################################
#find duplicate lines
seen = set()
dups = set()
with open("data.txt") as f:
    for line in f:
        if line in seen:
            dups.add(line)
        else:
            seen.add(line)
print(seen)
print(dups)

############################################################
#reverse a file content
with open("data.txt") as f:
    lines = f.readlines()

with open("data.txt", "a") as f:
    f.writelines(lines[::-1])
"""
##################################################################
#
# Method      | Meaning       |
# ----------- | ------------- |
# read()      | Entire file   |
# readline()  | One line      |
# readlines() | List of lines |
###########################################################
#JSON PRACING
#json.loads() → JSON STRING to Python
#json.dumps() → Python to JSON STRING
#json.load() → JSON FILE to Python
#json.dump() → Python to JSON FILE
#indent=4 → makes JSON readable (VERY IMPORTANT)
#data = {
#    "project": "DevOps",
#    "tools": ["Docker", "K8s"]
#}
#with open("sample.json","a") as f:
#    json.dump(data,f,indent=4)

#Read JSON file and print values
import json

with open("sample.json") as f:
    data = json.load(f)

print(data)
print(type(data))

########################################################
#Parse API response (JSON string)
import json

response = '{"status":200,"msg":"success"}'
data = json.loads(response)

print(data["msg"])

######################################################
#Convert dictionary to JSON file
import json

d = {"env": "prod", "region": "ap-south-1"}
with open("new.json","w") as f:
    json.dump(d,f)
print(json.dumps(d, indent=4))
###########################################
#Access nested JSON (VERY IMPORTANT)
data = {
    "emp": {
        "name": "Shreya",
        "skills": ["Linux", "AWS"]
    },
    "student": {
        "name": "Shreya1",
        "skills": ["abc", "xyz"]
    }
}
print(data["emp"]["name"])
print(data["student"]["skills"])

###############################################################
#count keys in json
with open("new.json","r") as f:
    l = json.load(f)
print(len(l))
#################################################################
#loop through json list
data = {
    "servers": [
        {"name": "web1", "ip": "1.1.1.1"},
        {"name": "web2", "ip": "1.1.1.2"}
    ]
}
for i in data["servers"]:
    print(i["name"],i["ip"])

####################################################################
#Modify JSON value and save
with open("new.json") as f:
    data = json.load(f)
print(data)
data["env"] = "prod"

with open("new.json","w") as f:
    json.dump(data,f,indent=4)
#########################################################################
print(data.get("env", "Not Found")) # data.get("key","if not there print this")

################################################################################
json_data = '[1,2,3,4]'
data = json.loads(json_data)

print((data))
print(type(data))
