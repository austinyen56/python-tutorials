"""
Workshop 5 File Handling
Run this python file using an IDE (vscode, pycharm...)
Your output file should appear in the same directory as your python file
"""
import os
import urllib.request

# Opening a file, writing into it, and then closing it
f = open('output.txt', 'w')
f.write("Hello world!")
f.close()

# Alternitively, you can do this
with open("output.txt",'w') as f:
    f.write("Hello world!")
    # Don't need to call close() when using a with statement

# Reading a file and print out the contents
# Will give an error if theres no such file
f = open("outfile.txt", "r")
print(f.read())
f.close()

# If the file is in a different location
# r means raw string; you can also specify encoding methods by adding the encoding arg
f = open(r"C:\Users\Austin\Desktop\三字經.txt", "r",encoding="utf-8")
print(f.read())

# Need to import os to get current directory
x = os.getcwd()
print(x)

# Read the first 3 characters
print(f.read(3))

# Read the first line
print(f.readline())
print(f.readline(4))    # Do it again to read the following line, put an int as arg to read x characters
print(f.readlines())   # Prints out a list of strings
# Using for loops to iterate and print out every character in a file
for i in f:
    print(i)
f.close()

# Removing files
# Requires you to import os; allows you to access/ modify things from your current computer (Kinda like file explorer/ Finder)
os.remove("outfile.txt")
os.rmdir("myfolder") # Removes the whole folder

# Check if file exists, then delete it
if os.path.exists("demofile.txt"):
    print("Im gonna remove demofile.txt")
    os.remove("demofile.txt")
else:
    print("The file does not exist")

# Taking content from a website
# Need to import urllib.request
url = "https://raw.githubusercontent.com/austinyen56/CoronaTracker/main/CAcities.csv"
local_copy = "local.txt"
urllib.request.urlretrieve(url, local_copy) # This function copies the thing the url points at into a local file copy
with open(local_copy, encoding="utf-8") as fh: # Print the file
    print("City, State Initials, State, Latitude, Longtitude, Population")
    for line in fh:
        print(line, end="")
