

# 9 #The first line contains the number of students who have subscribed to the Englishnewspaper.
# 123456789 #The second line contains the space separated list of student roll numbers who havesubscribed to the English newspaper.
# 9 #The third line contains the number of students who have subscribed to the Frenchnewspaper.
# 10 1 2 3 11 21 55 6 8 #The fourth line contains the space separated list of student roll numbers who havesubscribed to the French newspaper.

st = int(input("Number of students who have subscribed to the Englishnewspaper: "))
list1 = set(input("Student roll numbers who havesubscribed to the English newspaper: ").split())
st2 = int(input("Number of students who have subscribed to the Frenchnewspaper: "))
list2 = set(input("Student roll numbers who havesubscribed to the French newspaper: ").split())


x = list1 - list2
print(len(x))
