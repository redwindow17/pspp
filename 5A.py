print("Using Sets")
automobile={"engine", "battery", "transmission", "steering", "brakes", "video players","sensors"}
temp=0
keyword=input("Enter the parts of automobile you looking for: ")
for i in automobile:
    if(i==keyword):
        temp=1
        break
if(temp==1):
    print("Component you looking in a car is available")
else:
    print("Sorry, Not available")



