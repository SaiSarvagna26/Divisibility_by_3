A=list(map(int,input().split()))
counter=0
for i in A:          
   if (i!=0 and i%3==0):
      counter+=1
print(counter)
