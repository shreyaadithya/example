print("hello worl!")
text = "hello world"

print(text.count("l"))  # 3
text = "hello world"

file = "script.py"

print(file.startswith("script"))  # True
print(file.endswith(".py"))       # True
#########################################################################
#reverse string 
s = "DevOps"
print(s[::-1])

print("".join(reversed(s)))
#############################################################################
#Remove Special Characters
import re

text = "DevOps@123!"
clean = re.sub(r'[^a-zA-Z]', '', text)
print(clean)
