"""1. Reverse a String Without Slicing"""
s=input()
r=""
for i in s:
    r=i+r
print(r)


"""2. Check Palindrome Without Using Reverse"""
s=input()
f=True
for i in range(len(s)//2):
    if s[i]!=s[len(s)-1-i]:
        f=False
        break
print("Palindrome" if f else "Not Palindrome")


"""3. Count Vowels and Consonants"""
s=input().lower()
v=c=0
for i in s:
    if i.isalpha():
        if i in "aeiou":
            v+=1
        else:
            c+=1
print("Vowels:",v)
print("Consonants:",c)


"""4. Find Duplicate Characters"""
s=input()
d=[]
for i in s:
    if s.count(i)>1 and i not in d:
        d.append(i)
for i in d:
    print(i,end=" ")
    
    
"""5. Remove Special Characters"""
s=input()
r=""
for i in s:
    if i.isalnum() or i==" ":
        r+=i
print(r)