
#string using "", '','''''
a= "i am a good student"
b ='245677'
c=''' Hey an good'''
print(a)
print(b)
print(c)

x = "banana"
y = "orange"
print(x>y)
print(x+y)
print(x>=y)
print(x*3)

S1 = "This is Anne\'s spam"
print(S1)
s2= "3"
s3= "5"
s3= "6"
print(s2+s3)
#indexing strings using the [] operator
S2= "mercy"
letter = S2[4]
print(letter)
letter = S2[-1]
print(letter)
#indexing slicing strings using [] operator
S3 = "Hello world"
print(S3[3:7])
print(S3[2:4])
print(S3[:])
print(S3[:5],S3[1],S3[::2])
print(S3[-1:3])
#printing strings and numbers
S4 ="mercy"
S5= "wamjiku"
S6= ""
print (len(S4), end=" ")
print (len(S5), end=" ")
print (len(S6))
x1= 20
x2= 75
print ('The sum of %d and %d is %d' % (x1,x2, x1+x2))  
x3= 20.33
x4= 75.76
print ('The sum of %f and %f is %f' % (x1,x2, x1+x2))  
print ('The sum of %0.2f and %0.2f is %0.2f' % (x1,x2, x1+x2))
print ('The sum of %.2f and %.2f is %.2f' % (x1,x2, x1+x2))
x1= "python"
x2= "programing"
print ('The sum of %s and %s is %s' % (x1,x2, x1+x2))  
#string methods
r ="hello world"
#len()=length
print(len(r))
print(r.upper())
print(r.lower())
#Replace()
print(r.replace("h" ,"k"))

txt= "mercy is a good student."
#capitalize() 
a= txt.capitalize()
#lower()
b= txt.lower()
#center()
c= txt.center(40)
print (a)
print (b)
print (c)

