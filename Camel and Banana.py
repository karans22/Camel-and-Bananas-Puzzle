total=int(input('Enter No. of Bananas:'))
dist=int(input('Enter Distance to cover:'))
load_capacity=int(input('Enter load capacity of camel:'))
lose=0
start=total
for i in range(dist):
    while start>0:
        start=start-load_capacity
        if start==1:
            lose=lose-1
        lose=lose+2
    lose=lose-1
    start=total-lose
    if start==0:
        break
print(start)
