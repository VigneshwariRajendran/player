cx,vb=map(str,input().split())
if(len(cx)!=len(vb)):
  print("no")
else:
  x=[cx.count(i) for i in cx]
  b=[vb.count(i) for i in vb]
if(x==b):
  print("yes")
else:
  print("no")
  
