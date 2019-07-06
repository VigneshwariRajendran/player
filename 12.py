vig=list(map(int,input().split()))
var=list(map(int,input().split()))
for i in range(0,s[1]):
    var=[var[-1]+var[:-1]]
print(*var,end=' ')
