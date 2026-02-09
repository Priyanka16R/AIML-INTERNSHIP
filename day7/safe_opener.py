filename=input("enter the filename to open:")
try:
   with open(filename,"r")as file:
      content=file.read
      print("File content: ")
      print(content)
except FileNotFoundError:
   print("Oops! that file doesn't exist,please check the filename")