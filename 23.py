from math import remainder


n=25




n = int(input())

rmd = []

while n > 0:
    rm = n % 2
    n = n//2
    rmd.append(rm)

count,result = 0,0

for i in range(0,len(rmd)):
    if rmd[i] == 0:
        count = 0
    else:
        count +=1
        result = max(result,count)

print(result)



# n = int(input())

# rmd = []

# while n > 0:
#     rm = n % 2

#     n = n//2
#     print(n)
#     rmd.append(rm)


# print(rmd)
