#1
def a():
    return 5
print(a())  # predict to print 5

#2
def a():
    return 5
print(a()+a()) # predict to print 5+5 = 10

#3
def a():
    return 5
    return 10
print(a()) # predict to get 5 because function have one statement ande see first one 

#4
def a():
    return 5
    print(10)
print(a()) #  predict to get 5 because function end with return statement else couldn't reach to it

#5
def a():
    return print(5)
    
x = a()
print(x)  # I haven't return value so cannot reach to function value

#6
#def a(b,c):
    #print(b+c)
#print(a(1,2) + a(2,3)) #  part1 noe and part 2 noe so (+) get an error

#7
def a(b,c):
    return str(b)+str(c) # convert to string
print(a(2,5)) # "2" + "5" so value is 25

#8
#def a():
   # b = 100
   # print(b)
    #if b < 10:
      #  return 5  # else:
      #  return 10
#return 7 # unexprected statement 
#print(a()) # unreacheble code

#9
def a(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3 # unreacaable code 
print(a(2,3)) #  7
print(a(5,3))   # 14
print(a(2,3) + a(5,3))  # 21


#10
def a(b,c):
    return b+c
    return 10  # unreacaable code 
print(a(3,5)) # 8


#11
b = 500
print(b) # 500
def a():
    b = 300
    print(b) # 300
print(b)  # 500
a() # 300
print(b) # 500


#12
b = 500
print(b) # 500
def a():
    b = 300
    print(b)
    return b
print(b) # 500
a() # 300
print(b) # 500

#13
b = 500
print(b) # 500
def a():
    b = 300
    print(b)
    return b
print(b) # 500
b=a() # 300
print(b) #300


#14
def a():
    print(1)
    b()
    print(2)
def b():
    print(3)
a() # 1 , 3 , 2


#15
def a():
    print(1)
    x = b() # 5
    print(x)
    return 10
def b():
    print(3)
    return 5
y = a()
print(y)  # 1, 3 ,5 , 10

























