"""1. Armstrong Numbers in a Range"""
s=int(input())
e=int(input())
for n in range(s,e+1):
    x=n
    d=len(str(n))
    t=n
    sm=0
    while t>0:
        r=t%10
        sm+=r**d
        t//=10
    if sm==x:
        print(x,end=" ")
        
        
"""2. Automorphic Number"""
n=int(input())
x=n*n
if str(x).endswith(str(n)):
    print("Automorphic")
else:
    print("Not Automorphic")
    
    
"""3. Happy Number"""
n=int(input())
a=set()
while n!=1 and n not in a:
    a.add(n)
    s=0
    while n>0:
        r=n%10
        s+=r*r
        n//=10
    n=s
print("Happy Number" if n==1 else "Not Happy Number")


"""4. Trapping Rain Water"""
n=int(input())
a=list(map(int,input().split()))
w=0
for i in range(n):
    l=max(a[:i+1])
    r=max(a[i:])
    w+=min(l,r)-a[i]
print(w)


"""5. Minimum Railway Platforms"""
n=int(input())
a=list(map(int,input().split()))
d=list(map(int,input().split()))
a.sort()
d.sort()
i=1
j=0
p=1
ans=1
while i<n and j<n:
    if a[i]<=d[j]:
        p+=1
        ans=max(ans,p)
        i+=1
    else:
        p-=1
        j+=1
print(ans)


"""6. Rotate Array by K Positions"""
n=int(input())
a=list(map(int,input().split()))
k=int(input())
k=k%n
a=a[-k:]+a[:-k]
print(*a)


"""7. Longest Common Prefix"""
n=int(input())
a=[]
for i in range(n):
    a.append(input())
p=a[0]
for s in a[1:]:
    while not s.startswith(p):
        p=p[:-1]
        if p=="":
            break
if p:
    print(p)
else:
    print(-1)
    
    
"""8. Minimum Window Substring"""
s=input()
t=input()
m=""
for i in range(len(s)):
    for j in range(i+1,len(s)+1):
        x=s[i:j]
        ok=True
        for c in t:
            if x.count(c)<t.count(c):
                ok=False
                break
        if ok:
            if m=="" or len(x)<len(m):
                m=x
print(m)


"""9. Electricity Bill"""
u=int(input())
if u<=100:
    b=u*2
elif u<=300:
    b=u*3
else:
    b=u*5
print(b)


"""10. Employee Bonus"""
s=int(input())
r=int(input())
if r>=90:
    b=s*20//100
elif r>=75:
    b=s*10//100
else:
    b=s*5//100
print(b)


