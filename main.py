from collections import defaultdict
n=int(input())
a=list(map(int,input().split()))
l,r=0,0
mx=len(a)
mp=defaultdict(bool)
for i in a:
    mp[i]=True
for i in range(5):
    l=0
    while(l<len(a)):
        rx=l
        while rx<len(a):
            if not mp[a[l]^a[rx]]:
                mp[a[l]^a[rx]]=True
                a+=[a[l]^a[rx]]
            rx+=1
        l+=1
print(a)