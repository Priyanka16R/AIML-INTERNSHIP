def calc_rectangle(length, width):
    area=length*width
    perimeter=2*(length*width)
    return area,perimeter
length=int(input("enter the legth:"))
width=int(input("enter the width:"))
area,perimeter=calc_rectangle(length,width)
print("area:",area)
print("perimeter:",perimeter)