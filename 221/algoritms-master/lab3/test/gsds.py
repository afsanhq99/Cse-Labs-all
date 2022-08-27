n=int(input())
l=[]
for i in range(n):
    a=list(map(int,input().split()))
    l.append(a)
#to sort the schedules based on the ending time i,e l[1]
l=sorted(l,key=lambda x:x[1])
print(l)
final=[l[0]]
print(final)
#because first element from the sorted schedule is always included
count=1
#to store the last schedule end time
f=l[0][1]
for j in range(len(l)-1):
    if(f<=l[j+1][0]):
        #if greater or equal to end time then included and count increased
        final.append(l[j+1])
        f=l[j+1][1]
        count+=1
print(count)
for j in final:
    print(j)