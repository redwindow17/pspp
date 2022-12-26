print("Using tuples")
car=["engine","battery","transmission","steering", "brakes","videoplayers", "sensors"]

keyword=input("Enter what you need from library: ")
for i in range(0,len(car)):

    if car[i]==keyword:
        temp=1
        break
if(temp==1):
    print("Item you needed from library is available. Visit library to collect it")
else:
     print("Sorry, Not available")
     
