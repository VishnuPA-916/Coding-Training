"1. Student Marks Sorting (Bubble Sort)"
a=[75,90,65,85,70]
n=len(a)
for i in range(n):
    for j in range(n-i-1):
        if a[j]>a[j+1]:
            a[j],a[j+1]=a[j+1],a[j]
print(a)

"2. Product Price Sorting (Bubble Sort)"
a=[1200,500,2500,800]
n=len(a)
for i in range(n):
    for j in range(n-i-1):
        if a[j]>a[j+1]:
            a[j],a[j+1]=a[j+1],a[j]
print(a)

"3. Student Ranking (Selection Sort)"
a=[88,72,95,60,81]
n=len(a)
for i in range(n):
    m=i
    for j in range(i+1,n):
        if a[j]<a[m]:
            m=j
    a[i],a[m]=a[m],a[i]
print(a)

"4. Book ID Sorting (Selection Sort)"
a=[104,101,109,102]
n=len(a)
for i in range(n):
    m=i
    for j in range(i+1,n):
        if a[j]<a[m]:
            m=j
    a[i],a[m]=a[m],a[i]
print(a)

"5. Employee Age Sorting (Selection Sort)"
a=[35,28,42,25,31]
n=len(a)
for i in range(n):
    m=i
    for j in range(i+1,n):
        if a[j]<a[m]:
            m=j
    a[i],a[m]=a[m],a[i]
print(a)

"6. Card Sorting (Insertion Sort)"
a=[7,3,9,1,5]
for i in range(1,len(a)):
    k=a[i]
    j=i-1
    while j>=0 and a[j]>k:
        a[j+1]=a[j]
        j-=1
    a[j+1]=k
print(a)

"7. Entered Marks Sorting (Insertion Sort)"
a=[60,50,70,40]
for i in range(1,len(a)):
    k=a[i]
    j=i-1
    while j>=0 and a[j]>k:
        a[j+1]=a[j]
        j-=1
    a[j+1]=k
print(a)

"8. Contact Number Sorting"
a=[9876,4567,1234,7890]
for i in range(1,len(a)):
    k=a[i]
    j=i-1
    while j>=0 and a[j]>k:
        a[j+1]=a[j]
        j-=1
    a[j+1]=k
print(a)

"9. Student Record Sorting (Merge Sort)"
def m(a):
    if len(a)>1:
        mid=len(a)//2
        l=a[:mid]
        r=a[mid:]
        m(l)
        m(r)
        i=j=k=0
        while i<len(l) and j<len(r):
            if l[i]<r[j]:
                a[k]=l[i]
                i+=1
            else:
                a[k]=r[j]
                j+=1
            k+=1
        while i<len(l):
            a[k]=l[i]
            i+=1
            k+=1
        while j<len(r):
            a[k]=r[j]
            j+=1
            k+=1

a=[55,12,89,34,23,78]
m(a)
print(a)

"10. Customer Account Sorting (Merge Sort)"
def m(a):
    if len(a)>1:
        mid=len(a)//2
        l=a[:mid]
        r=a[mid:]
        m(l)
        m(r)
        i=j=k=0
        while i<len(l) and j<len(r):
            if l[i]<r[j]:
                a[k]=l[i]
                i+=1
            else:
                a[k]=r[j]
                j+=1
            k+=1
        while i<len(l):
            a[k]=l[i]
            i+=1
            k+=1
        while j<len(r):
            a[k]=r[j]
            j+=1
            k+=1

a=[5678,1234,8901,3456]
m(a)
print(a)

"11. Product Search Result Sorting (Quick Sort)"
def q(a):
    if len(a)<=1:
        return a
    p=a[0]
    l=[x for x in a[1:] if x<=p]
    r=[x for x in a[1:] if x>p]
    return q(l)+[p]+q(r)

a=[1000,200,1500,500,800]
print(q(a))

"12. Cricket Score Sorting (Quick Sort)"
def q(a):
    if len(a)<=1:
        return a
    p=a[0]
    l=[x for x in a[1:] if x<=p]
    r=[x for x in a[1:] if x>p]
    return q(l)+[p]+q(r)

a=[45,78,23,90,67]
print(q(a))

"13. Employee Salary Sorting"
def q(a):
    if len(a)<=1:
        return a
    p=a[0]
    l=[x for x in a[1:] if x<=p]
    r=[x for x in a[1:] if x>p]
    return q(l)+[p]+q(r)

a=[45000,30000,60000,25000]
print(q(a))

"14. Railway Ticket Sorting"
def q(a):
    if len(a)<=1:
        return a
    p=a[0]
    l=[x for x in a[1:] if x<=p]
    r=[x for x in a[1:] if x>p]
    return q(l)+[p]+q(r)

a=[567,123,789,345]
print(q(a))

"15. Patient ID Sorting"
def q(a):
    if len(a)<=1:
        return a
    p=a[0]
    l=[x for x in a[1:] if x<=p]
    r=[x for x in a[1:] if x>p]
    return q(l)+[p]+q(r)

a=[205,101,309,150]
print(q(a))

"16. Roll Number Sorting"
def q(a):
    if len(a)<=1:
        return a
    p=a[0]
    l=[x for x in a[1:] if x<=p]
    r=[x for x in a[1:] if x>p]
    return q(l)+[p]+q(r)

a=[25,12,30,18]
print(q(a))

"17. Nearly Sorted Data"
a=[10,20,30,25,40]
for i in range(1,len(a)):
    k=a[i]
    j=i-1
    while j>=0 and a[j]>k:
        a[j+1]=a[j]
        j-=1
    a[j+1]=k
print(a)

"18. Customer ID Merge"
def m(a):
    if len(a)>1:
        mid=len(a)//2
        l=a[:mid]
        r=a[mid:]
        m(l)
        m(r)
        i=j=k=0
        while i<len(l) and j<len(r):
            if l[i]<r[j]:
                a[k]=l[i]
                i+=1
            else:
                a[k]=r[j]
                j+=1
            k+=1
        while i<len(l):
            a[k]=l[i]
            i+=1
            k+=1
        while j<len(r):
            a[k]=r[j]
            j+=1
            k+=1

a=[38,27,43,3,9,82,10]
m(a)
print(a)

"19. Sports Score Sorting"
def q(a):
    if len(a)<=1:
        return a
    p=a[0]
    l=[x for x in a[1:] if x<=p]
    r=[x for x in a[1:] if x>p]
    return q(l)+[p]+q(r)

a=[120,95,150,80,110]
print(q(a))

"20. Large Dataset Sorting"
def q(a):
    if len(a)<=1:
        return a
    p=a[0]
    l=[x for x in a[1:] if x<=p]
    r=[x for x in a[1:] if x>p]
    return q(l)+[p]+q(r)

a=[99,12,45,67,23,89,34]
print(q(a))

