mb=int(input())
ff=1
if(mb<=20):
   if(mb==0):
     print("1")
   else:
     for i in range(1,mb+1):
       ff=ff*i
print(ff)       
