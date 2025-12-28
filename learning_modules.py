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

"""import os

print(os.getcwd()) #to get current working dir
print(os.listdir())  # list files

#if not os.path.exists("ls"): # create folder # if not os.path.exists is to check folder is present or not
#    os.mkdir("text")

#os.rmdir("text") # delete folder
#os.remove("a.txt") # remove files
print(os.environ.get("USERPROFILE")) # get values of environment variable

######################################################################
import sys
print("Script name:", sys.argv[0]) # pass and check command line arguments
print(sys.version)
#sys.exit()
############################################################ """
#import subprocess

""""
import subprocess

r = subprocess.run(["ls", "-l"],capture_output=True,text=True)
result = subprocess.run(["date"], capture_output=True, text=True)
a = subprocess.run(["echo","this is my new coding platform"],capture_output=True)
print(r.stdout)
print(result.stdout)
print(a.stdout)  
#the above code will give only latest command output
subprocess.run("ls | grep py", shell=True)
#shell = true is only for |, >> , && else shell = true should be avoided

# python code for checking disk usage
import subprocess
out = subprocess.run(["df","-h"],capture_output=True,text=True)
x = out.stdout.splitlines()[1].split()[4]
#out.stdout give column wise output to convert to lists
#.splitlines() is used and to take perticular index split() is used
y = int(x.replace("%","")) #converting string output into int
print(y)
if y > 80:
    print("disk usage is more")
else:
    print("disk is working fine")

#####################################################################
#Run command and check success
import subprocess

res = subprocess.run(["ls","-la"], capture_output=True)
if res.returncode == 0:
    print("Success")

######################################################################
 #Run command and save output to file
import subprocess

res = subprocess.run(["ls","-la"], capture_output=True,text=True)
if res.returncode == 0:
    print("Success")

with open("output.txt","w") as f:
    f.write(res.stdout)
print(res.stderr)

#execute multiple commands
commands = [["ls"], ["pwd"], ["date"]]

for cmd in commands:
    result = subprocess.run(cmd,capture_output=True, text=True)
    with open("output.txt","a") as f:
        f.write(result.stdout)

#Timeout handling (VERY IMPORTANT)
import subprocess
try:
    subprocess.run(["sleep", "10"], timeout=3)
except subprocess.TimeoutExpired:
    print("Command timed out")
 #############################################################   
 #for shutil module
import shutil

shutil.copy("a.txt", "b.txt")
shutil.move("b.txt", "backup/")
shutil.rmtree("temp")
########################################################
import time
print("Start")
time.sleep(2)
print("End")
#############################################################
from datetime import datetime

now = datetime.now()
print(now)
print(now.strftime("%Y-%m-%d"))
print(datetime.now().hour)
################################################################
#logging module is used to write log records
import logging

logging.basicConfig(level=logging.INFO)
logging.info("Application started")
logging.error("Something went wrong")
##############################################################
from pathlib import Path

p = Path("test.txt")
print(p.exists())
#################################################################

###################################################################
import requests

response = requests.get("https://api.github.com")
print(response.status_code)
print(response.text)

response.status_code   # HTTP status
response.text          # Response as string
response.json()        # JSON → Python dict
response.headers       # Metadata
"""


