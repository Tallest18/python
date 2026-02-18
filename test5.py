thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1

  fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newList = []

for x in fruits:
  if "e" in x:
    newList.append(x)

print(newList)

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist1 = [x for x in fruits if x != "apple"]

print(newlist1)


newlist2 = [x for x in range(10)]

print(newlist2)

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist3 = [x.upper() for x in fruits]

print(newlist3)

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)