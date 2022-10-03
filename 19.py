# from typing import List





# def Count():
#     add=input("ENTER ANYTHING: \n")

#     list=[]

#     for i in add:
#         list.append(i)
#         wordOne=[]
#         wordTwo=[]
#         for j in range(len(list)):
#             # print([j])
#             if(j%2==0 or j==0):
#                 # print(list[j])
#                 wordOne.append(list[j])
#             else:
#                 # print(list[j])
#                 wordTwo.append(list[j])
        

# Count()    
# print(list)
# print(wordOne)
# print(wordTwo)



# T=int(input())       

# for i in range(0,T):
S=input()
print(S[0::2]+" "+S[1::2])