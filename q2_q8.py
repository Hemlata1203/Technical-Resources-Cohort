#Q8.
n=int(input())
for i in range(1,n+1):
    for j in range(i,i+1):
        print('\t'*(n-i)+'*'+'\t'*(i-1))
