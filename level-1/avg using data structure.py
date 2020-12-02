print("enter 5 nos to find out sum and average")
count=0
stuff=list()
while count<5:
    var=input("enter the no")
    count=count+1
    stuff.append(float(var))

avg=sum(stuff) / len(stuff)
print("Average:",avg)
print(sum(stuff))