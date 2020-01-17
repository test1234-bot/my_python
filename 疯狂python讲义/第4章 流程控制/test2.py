

for a in range(1, 5):
    for b in range(1, a):
        print(b,'x',a,"=",a*b,",",end=" ")
        print()

print("++++++++++++++")
for i in range(1,10):
    for j in range(1,i):
        print(j,'x',i,"=",i*j,",",end=" ")
    print(i,'x',i,"=",i*i)