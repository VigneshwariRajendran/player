ss=list(input())
for i in range(0,len(ss),2):
  ss[i],ss[i+1]=ss[i+1],ss[i]
print(''.join(ss)) 
