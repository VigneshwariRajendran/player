a=int(input())
vr=list(map(str,input()[:a]))
rr=[]
for i in vr:
   if i not in rr:
      rr.append(i)
print(''.join(map(str,rr[::-1])))      
