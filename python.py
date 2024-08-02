'''print("hello")
print("welcome")
 print(50)
print(1+2)
print("hello"+','+"world")      
print('h/u')
#print('world'+12)
print('world'*3)
print('world'*23)'''
#arithamatic operation

'''#1, addition
print(2+3)
#2,SUBSTRACTION
print(4-2)
#3,multti
print(3*5)
#4,divition
print(10/2)
#5,floor divition
print(3//2)
#6,modulo
print(4%2)
#7 exponential
print(4**2)#4^2
#8 root
print(4**(1/2)) #root4'''

#boolean operators(<,>,<=,>=,!=,==)
'''print(7>2)
print(7<2)
print(2!=3)
print(7==9)
print()
print('hello'=='hello') #coparison operator'''


#variable ( used for temporary storage,we can reassign values)
'''a=10
print(a)
print(id(a))
a=20
print(a)
print(id(a))
print(a+5)
print(a-10)
x=20
y=70
z=x+y
print("result is",z)
e=10
h=20
g=e*h
print("result is",g)'''
#type function (used identify data type of value stored in variable
'''z=30
print(type(z))
c=hello
print(type(c))'''

#type convertion (convert one data type into another )
'''print(int('2')+int('3'))
print(int(2.3)+int(4.5))
print(float(5)+float(7))''' 

#input function
'''a=int(input("enter your 1st nmbr:"))
b=int(input('enter your 2nd nmbr:'))
c=a+b
d=a*b
print('result is',c,d)'''

'''a=str(input("enter your name:"))
b=int(input("enter your age:"))
c=str(input("enter your place:"))
print ('name is',a,)
print ('age is',b,)
print('place is',c,)'''

#swapping(using third variable)
'''a=10
b=5
temp=a
a=b
print('value of a:',a)
b=temp
print('value of b:',b)

#without using third variable
print('before swapping')
x=10
y=20
print ("value of x:",x)
print('value of y:',y)
print ('after swapping')
x,y=y,x
print('value of x:',x)
print('value of y:',y)'''

# conditional statement
'''
1,if
2,ladder if
3,if else
4,ladder else if
5,elif'''

# syntax
'''if condition:
      statement'''
      

'''if 10<2:
    print('10 is greater')
print('pgm finished')'''
      
# ladder if statement
#syntax
'''if condition:
    statement:
    if condition:
        statement:
        if condition:
            statement'''
'''num=10
if num>2:
    print('hello')
    if num>5:
       print('hi')
       if num==10:
          print('python')'''
          
 #if else
#syntax
'''if condition
    statement
else statement

if 10<2:
    print('hello')
else:
     print('hi')'''

'''x=int(input('enter your 1st nmbr:'))
y=int(input('enter your 2nd nmbr:'))
if x==y:
    print('square')
    
else:
    print('rectangle')'''



'''#logical operators
# and or not

print(5>3 and 5==5)#both are true
print(10>5 or 10!=10)#atleast one true
print(not 3==3)#operator return the opposit boolean value
    
    
#inplace operators

a=10
a+=5
print(a)
b=15
b-=5
print(b)
c=100
c/=5
print(c)
d=4
d//=2
print(d)'''


'''#identity operators
a=10
b=5
c=10

print(id(a))
print(id(b))
print(id(c))

#id()-determained memory address
#is : this operator returns true if two variable reference the same object in memory
#is not : this operator return true if two variable reference different objects in memory
      
print(a is b)      
print(a is c)                                                                                                                                                              
print(a is not c)
print(a is not b)'''



'''name=input('enter your name:')
age=input('enter your age:')
# string format
#format()
#"{}" place holder
print("my name is {} and i'm {} years old ".format(name,age))
print("my name is {} and i'm {} years old ".format(age,name))
      
#f string method
print(f"my name is {name} and i'm {age} years old")'''



#else if ladder
#syntax

'''if condition:
    statement
else:
    if condition:
        statement
    else:
        statement
num =10
if num>12:
    print('hello')
else:
    if num<2:
        print('welcome')
    else:
        if num==10:
            print('python')'''
#check its vowel or not

'''data = input('enter a character:')
vowel="aeiouAEIOU"
if data in vowel:
    print('is vowel')
else:
    print('is not vowel')'''

'''color=input('enter a color:')
if color=="red":
    print('color is red')
else:
    if color=="blue":
        print('color is blue')
    else:
        if color=="green":
            print('color is green')
        else:print('its not RBG color code')'''
#elif
#syntax:
'''if condition:
    statement
elif condition:
    statement
else condition:
    statement

color=input('enter a color:')
if color== "red":
    print('color is red')
elif color=="blue":
    print('color is blue')
elif color == "green":
    print('color is green')
else:
    print('is not RBG color code')'''

'''#greatest number in 3 inputs

a=input('enter first number:')
b=input('enter second number:')
c=input('enter third number:')

if a>b and a>c:
    print('a is greater',a)
elif b>a and b>c:
    print('b is greater',b)
else:
    print('c is greater',c)'''


#loop
#1,while loop
# syntax

'''initstn
while condition(1limit):
    statement
      increment'''

# helo print in 10 times
'''i=1
while i<=10:
    print('helo')
    i+=1
print('finished')'''

# 1 to 10

'''i=1
while i<=10:
    print('i')
    i+= 1

#i=1
while i<=0:
    if i%2==0:
        print(i)
    i+= 1'''

'''#break
while 1==1:
     print("hello")
     break


i=1
while i<=10:
    if i==5:
        break
    print(i)
    i+1

i=1
while i<6:
    print(i)
    if (i==3):
        break
    i+=1

#continue
i=0
while i<6:
    i+=1
    if i==3:
        continue
    print(i)'''







'''i=0
while i<=10:
    i+=1
    if i==2:
        print("skipping 2")
        continue
    if i==5:
        print("hello")
        break
    print(i)




i=10
while i>0:
    if i==5:
        i-+1
        break
    print(i)
    i-=1
print("thankyou")'''







  



        
    
 
            
    
    
    
    
    

      










      
        
            
    
    
    
    
    

      









