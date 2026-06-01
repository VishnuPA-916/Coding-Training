"""1. Spy Number"""
n=int(input())
s=0
p=1
t=n
while t>0:
    d=t%10
    s+=d
    p*=d
    t//=10
print("Spy Number" if s==p else "Not Spy Number")


"""2. Neon Number"""
n=int(input())
x=n*n
s=0
while x>0:
    s+=x%10
    x//=10
print("Neon Number" if s==n else "Not Neon Number")


"""3. Peterson Number"""
n=int(input())
t=n
s=0
while t>0:
    d=t%10
    f=1
    for i in range(1,d+1):
        f*=i
    s+=f
    t//=10
print("Peterson Number" if s==n else "Not Peterson Number")


"""4. Twisted Prime Number"""
n=int(input())
def prime(x):
    if x<2:
        return False
    for i in range(2,int(x**0.5)+1):
        if x%i==0:
            return False
    return True
r=0
t=n
while t>0:
    r=r*10+t%10
    t//=10
print("Twisted Prime" if prime(n) and prime(r) else "Not Twisted Prime")


"""5. Emirp Number"""
n=int(input())
def prime(x):
    if x<2:
        return False
    for i in range(2,int(x**0.5)+1):
        if x%i==0:
            return False
    return True
r=0
t=n
while t>0:
    r=r*10+t%10
    t//=10
print("Emirp Number" if prime(n) and prime(r) and n!=r else "Not Emirp Number")


"""6. Duck Number"""
n=input()
print("Duck Number" if '0' in n[1:] else "Not Duck Number")


"""7. ISBN Number"""
n=input()
s=0
for i in range(len(n)):
    s+=(i+1)*int(n[i])
print("Valid ISBN" if s%11==0 else "Invalid ISBN")


"""8. Maximum Binary Gap"""
n=int(input())
b=bin(n)[2:]
p=-1
m=0
for i in range(len(b)):
    if b[i]=='1':
        if p!=-1:
            m=max(m,i-p)
        p=i
print(m)


"""9. Digital Root"""
n=int(input())
while n>9:
    s=0
    while n>0:
        s+=n%10
        n//=10
    n=s
print(n)

"""
10. Circular Prime"""
n=input()
def prime(x):
    if x<2:
        return False
    for i in range(2,int(x**0.5)+1):
        if x%i==0:
            return False
    return True
f=True
for i in range(len(n)):
    r=n[i:]+n[:i]
    if not prime(int(r)):
        f=False
        break
print("Circular Prime" if f else "Not Circular Prime")

