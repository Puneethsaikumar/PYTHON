#1.REVERSE A STRING WITHOUT BUILT-IN FUN
a=input("enter a string:")
b=""
for i in a:
    b=i+b
print(b)


#2.PALINDROME OR NOT
a=input("enter a string:")
b=""
for i in a:
    b=i+b
print(b)
if (a==b):
    print("given string is a palindrome")
else:
    print("given string is not a palindrome")


#3.NO OF VOWELS AND CONSONANTS IN A STRING
a=input("enter a string:")
v=0
c=0
for i in a:
    if i in ('a','e','i','o','u'):
        v+=1
    else:
        c+=1

print("v:",v)
print("c:",c)


#4.REMOVE SPACES IN A STRING 
a=input("enter a string:")
b=a.replace(" ","")
print(b)


#5.FREQUENCY OF EACH CHARACTER IN A STRING
a=input("enter a string:")
freq={}
for i in a:
    if i in freq:
        freq[i]+=1
    else:
        freq[i]=1

print(freq)