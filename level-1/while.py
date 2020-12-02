print("enter 5 nos to find out sum and average")
count=0
sum=0
while count<5:
    var=input("enter the no")
    count=count+1
    sum = sum +float(var)

avg=sum/5
print("Average:",avg)
print("sum:",sum)