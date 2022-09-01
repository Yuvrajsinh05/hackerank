x = int(input())
y = int(input())
z = int(input())
n = int(input())

arr=[x,y,z]
total=x+y+z
a= [[i,j,k] for [i,j,k] in arr if n!=total]