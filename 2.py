mb=int(input())
ff=0
if(mb<=20):
   if(mb==0):
     print("1")
   else:
     for i in range(0,mb+1):
       ff=ff*i
print(ff)       
