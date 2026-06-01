"Question 1: Search Product ID"
n=int(input())
a=[]
for i in range(n):
    a.append(int(input()))
x=int(input())
for i in range(n):
    if a[i]==x:
        print("Found at Index",i)
        break
else:
    print("Product Not Found")
    
    
"Question 2: Find Student Roll Number"
n=int(input())
a=[]
for i in range(n):
    a.append(int(input()))
x=int(input())
for i in range(n):
    if a[i]==x:
        print("Roll Number Found at Index",i)
        break
else:
    print("Roll Number Not Found")
    
    
"Question 3: Search Mobile Number"
n=int(input())
a=[]
for i in range(n):
    a.append(int(input()))
x=int(input())
for i in range(n):
    if a[i]==x:
        print("Number Found at Index",i)
        break
else:
    print("Number Not Found")


"Question 4: Count Occurrences"
n=int(input())
a=[]
for i in range(n):
    a.append(int(input()))
x=int(input())
c=0
for i in a:
    if i==x:
        c+=1
print(c)


"Question 5: First Occurrence"
n=int(input())
a=[]
for i in range(n):
    a.append(int(input()))
x=int(input())
for i in range(n):
    if a[i]==x:
        print(i)
        break
    
    
"Question 6: Last Occurrence"
n=int(input())
a=[]
for i in range(n):
    a.append(int(input()))
x=int(input())
for i in range(n-1,-1,-1):
    if a[i]==x:
        print(i)
        break
    
    
"Question 7: Find Maximum Element"
n=int(input())
a=[]
for i in range(n):
    a.append(int(input()))
m=a[0]
for i in a:
    if i>m:
        m=i
print(m)


"Question 8: Find Minimum Element"
n=int(input())
a=[]
for i in range(n):
    a.append(int(input()))
m=a[0]
for i in a:
    if i<m:
        m=i
print(m)


"Question 9: Check Even Number Exists"
n=int(input())
a=[]
for i in range(n):
    a.append(int(input()))
for i in a:
    if i%2==0:
        print("Even Number Found")
        break
else:
    print("Even Number Not Found")
    
    
"Question 10: Find Index of Largest Element"
n=int(input())
a=[]
for i in range(n):
    a.append(int(input()))
m=max(a)
for i in range(n):
    if a[i]==m:
        print(i)
        break

