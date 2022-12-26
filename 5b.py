automobile={1:"engine", 2:"battery", 3: "transmission", 4:"steering", 5:"brakes", 6:"video players", 7:"sensors"}
temp=0
keyword=input("Enter the parts of automobile you looking for: ")
for i in range(1,len(automobile)):
    if(automobile[i]==keyword):
        temp=1
        break
if(temp==1):
    print("Component you looking in a car is available")
else:
    print("Sorry, Not available")



