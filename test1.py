import statistics as s
import os

l1 = [1,2,3,6,8,32,45,67,23,11,11,11,22,43,56,90]

print(s.mean(l1))
print(s.median(l1))
print(s.mode(l1))

print(l1)
print(l1.count(11))
print(l1.sort())
l1.sort()
print(l1)


x = [[2,6],[6,2],[8,2],[5,12]]
print(x[2])

print(
'''
So it works like a multi-line
comment, but it will print out.

You can make kewl designs like this:

==============
|            |
|    BOX     |
|            |
==============
'''
    )

intMe = '55'
intMe = int(intMe)
print(intMe)


curDir = os.getcwd()
print(curDir)
import sys
print(sys.path)
