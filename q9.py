def generate(a,b):
# a=int(input("enter star:"))
# b=int(input("enter end:"))
    s=[]
    p=[]
    i=a
    while i<a+5:
        s.append(i**2)
        i=i+1
    p.append(s)
    m=[]
    j=b-5
    while j<=b:
        m.append(j**2)
        j=j+1
    p.append(m)
    return p
x=int(input("enter star:"))
y=int(input("enter end:"))
print(generate(x,y))