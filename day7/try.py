try:
 file= open("filehandling","r")
 print(file.read())
except FileNotFoundError:
 print("File not found, open exixsting file")
finally:
 file.close()

 