with open("friends.txt","w")as file:
 for i in range(3):
  name=input("enter friend name:")
  file.write(name + "\n")
print("3 names saved successfully")

name = input("enter your name:")
marks=input("enter your marks")
with open("friends.txt","a")as f:
 f.write(f"{name}-{marks}\n")
 print("Student data appended into friends.txt")

filename=input("enter file name")
with open(filename,"r")as f:
 lines=f.readlines()
 print("Total lines=",len(lines))

 search_name=input("enter name to search")
 with open("friends.txt","r")as f:
  names=f.read().splitlines()
  if search_name in names:
   print("Found!!")
  else:
   print("Not Found!")