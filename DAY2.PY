#6.CHECK IF A NUMBER IS PRIME OR NOT
n=int(input("Enter a number:"))
count=0
for i in range(1,n+1):
    if n%i==0:
        count+=1
print(count)
if count==2:
    print("Given number is a prime")
else:
    print("Given number is not a prime")


#7.FIND THE FACTORIALS OF A NUMBER
m=int(input("Enter a number:"))
factors=[]
for i in range(1,m+1):
    if m%i==0:
        factors.append(i)
print(factors)


#8.Print the Fibonacci series up to n terms
x=int(input("Enter a number:"))
a=0
b=1
for i in range(x):
    print(a)
    a, b=b, a+b


#9.Find the sum of digits of a given number
y=input("Enter a number:")
sum=0
for i in range(len(y)):
    sum+=int(y[i])
print(sum)


#10.Reverse the digits of a given number
p=input("enter a number:")
q=""
for i in p:
    q=i+q
print(q) 

              #OR
r=input("Enter a number:")
rev=""
rev=r[::-1]
print(rev)
