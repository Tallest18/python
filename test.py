import sys

print (sys.version)

if 5 > 2:
 print("five is greater two")

 print("Hello World!")
print("Have a good day.")
print("Learning Python is fun!")

z = 6
y = "blessing"
print(z, y)

x = 'awesome'

def myfunc():
    x = 'fantastic'

myfunc()

print('python is' + x)

y = 'awesome'

def myfunc():
    global y
    y = 'fantastic'

myfunc()

print('python is ' + y)