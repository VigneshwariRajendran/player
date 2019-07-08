dev,thu=map(int,input().split())
for i in range(1,100000+1):
   if(i%dev==0 and i%thu==0):
      print(i)
      break
   
