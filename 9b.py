from collections import Counter
FileName = input("Enter the file name: ")
CntFile = open(FileName, 'r')
print("Number of words in the file :")
print(Counter(CntFile.read().split()))
CntFile.close()
