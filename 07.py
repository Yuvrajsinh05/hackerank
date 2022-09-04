# num=int(input("Enter:"))
# print(num)


# List = []
# name = input("Enter your name:")
# for i in List:
#     List.append(name)



# L=[]
# while True:
#   item=input("enter new item :")
#   if item=='':
#     break
#   L.append(int(item))
# print ("List : ",L)


# name:input("Enter Your NAme :")
# marks:int(input("Enter MArks"))

# L=[]

# L.insert(str(name))
# # L.append(int(marks))


# print(L)

Result =[]
scorelist = []
if __name__ == '__main__':
    for _ in range(int(input())):
        name = input()
        score = float(input())
        Result+=[[name,score]]
        scorelist+=[score]
    b=sorted(list(set(scorelist)))[1] 
    for a,c in sorted(Result):
        if c==b:
            print(a)
