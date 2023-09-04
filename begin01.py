a1,b1,c1=map(int,input().split())
a=max(a1,b1,c1)
c=min(a1,b1,c1)
b=a1+b1+c1-a-c
a1,b1,c1=map(int,input().split())
x=max(a1,b1,c1)
z=min(a1,b1,c1)
y=a1+b1+c1-x-z
if (a==x and b==y and z==c):
    print("Boxes are equal")
elif (a>=x and b>=y and c>=z):
    print("The first box is larger than the second one")
elif (x>=a and y>=b and z>=c):
    print("The first box is smaller than the second one")
else:
    print("Boxes are incomparable")