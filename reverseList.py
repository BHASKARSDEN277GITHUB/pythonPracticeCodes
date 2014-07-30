# test code for reversing a list in python


a=[1,2,3,4,5,6,7]

#printing original list 
print "\nPrinting original List\n"
for i in a :

	print i 

b=[] #created empty list

i=6
while i>=0 :
	
	b.append(a[i])
	i=i-1

#printing reversed list
print "\nPrinting reversed List\n"
for i in b :

	print i
