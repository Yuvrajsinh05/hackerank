# save = {}
# n=int(input("How many numbers you want to save \n"))

# for i in range(n):
#     num=input("Enter")
#     save.update(num)

# print(save)    

x = int(input())

dictt = {}

for i in range(x):
    text = input().split()
    dictt[text[0]] = text[1]

while True:
    try:
        inpt = input()
        if inpt in dictt:
            print(inpt+"="+dictt[inpt])
        else:
            print("Not found")
    except EOFError:
        break