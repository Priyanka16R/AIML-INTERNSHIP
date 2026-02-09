name=input("Enter your name:")
goal=input("enter your daily goal:")
with open("journal.txt","a")as file:file.write(f"Name:{name},Daily Goal:{goal}\n")
print("entry saved successfully.")