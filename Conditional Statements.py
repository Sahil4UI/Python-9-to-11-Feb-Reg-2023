'''
# Largest B/w 2 Numbers
x = int(input("Enter No 1:"))
y = int(input("Enter No 2:"))

if x>y :
    print(f"{x} is largest")
elif x==y:
    print(f"{x} is Equals to {y}")
else:
    print(f"{y} is largest")
'''
'''
#find largest b/w 3 numbers
x = int(input("Enter No 1:"))
y = int(input("Enter No 2:"))
z = int(input("Enter No 3:"))

if x>y and x>z:
    print(f"{x} is largest")
elif y>z:
    print(f"{y} is largest")
else:
    print(f"{z} is largest")


'''
#we have 3 sides, if they form a traingle , detect the type 
# of traingle - equilateral , isoceles , scalene
x = int(input("Enter Side 1:"))
y = int(input("Enter Side 2:"))
z = int(input("Enter Side 3:"))

if x+y>z and y+z>x and z+x>y:
    if x==y and y==z:
        print("Equilateral Traingle")
    elif x==y or y==z or z==x:
        print("Isoceles Traingle")
    else:
        print("Scalene Traingle")
else:
    print("Invalid Sides")