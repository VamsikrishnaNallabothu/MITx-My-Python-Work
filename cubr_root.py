#find th cube root of an  given integer
x= int(raw_input("Enter an value to find the cube root: "))
cube_root=0
while(cube_root**3<x):
    cube_root = cube_root+1
if(cube_root**3==x):
    print (str(cube_root)+  +' is the cube root of the given number')
else:
	print ("the given number doesn't has a cube root")
