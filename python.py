num=5
count=0
for fa in range(1,num+1):
    if(num%fa==0):
        count+=1
print('prime' if(count==2) else 'not prime')