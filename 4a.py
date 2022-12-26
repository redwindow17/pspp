print("Using list")
library=["books", "periodicals", "newspapers", "manuscripts", "films", "maps", "prints","documents", "microform", "CDs", "cassettes", "videotapes", "DVDs","Blu-ray Discs", "e-books", "audiobooks", "databases"]

keyword=input("Enter what you need from library: ")
for i in range(0,len(library)):

    if library[i]==keyword:
        temp=1
        break
if(temp==1):
    print("Item you needed from library is available. Visit library to collect it")
else:
     print("Sorry, Not available")
     
