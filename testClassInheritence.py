#testing class inheritence sytaxes 

class test(object) :
	
	def __init__(self) :
		
		print "I am constructor of class test\n" 
	
	def method(self) :
	
		print "I am method of class Test\n "

class derived(test) :

	def __init__(self) :
	
		print "I am constructor of derived class \n"

	def method(self) :  #trying to override method here

		print "I am method of derived class\n"

	def methodSuper(self) :
		
		#struggling here right now .. 
		#done now ;) 
		super(derived,self).method()


#creating instance variables of classes above 

x=test()
x.method()
y=derived()
y.method()

y.methodSuper()
