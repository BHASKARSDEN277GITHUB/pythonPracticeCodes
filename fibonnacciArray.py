#!/usr/bin/python

prev=1
prev1=1
fArray=[prev1,prev]

print "Enter number of elements"
n=input()

while n>2 :
	a=prev+prev1
	fArray.append(a)
	prev1=prev
	prev=a
	n=n-1

for i in fArray :
	print i,
