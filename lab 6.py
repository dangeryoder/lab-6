# 1st

userInput = int(raw_input())
total = 0
for x in range(5):
    print "enter a number:"
    userInput = int(raw_input())
    total = total + userInput
print total

# 2nd

Userinput = int(raw_input())
totalList = []
for x in range(5):
    print "enter a number:"
    Userinput = int(raw_input())
    totalList.append(Userinput)
print sum(totalList)

# 3rd

total = 1
userinput = int(raw_input())
for x in range(1,userinput+1,1):
    total = total*x
print total

# 4th

x = int(raw_input())
for i in range(1,x+1,1):
     if x % i == 0:
         print (i)
