# i = 1
# while i <= 100:
#     print(i)
#     i += 1
  
# print("loops ended")

# i = 100
# while i >= 1:
#     print(i)
#     i -= 1
  
# print("loops ended")



# n= int(input("Enter the Number:"))
# i = 1
# while i <= 10:
#     print(n*i)
#     i +=1
  
# print("loops ended")


# # i = 1
# # while i <= 10:
# #     print(i*i)
# #     i +=1
  
# # print("loops ended")
# i = 0
# set = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 36)
# x= int(input("Enter the number:"))
# while i < len(set):
#     if(set[i] == x):
#         print("found at", i)
#         break
#     else:
#         print("finding..")
#     i+= 1
# print("End of loop")

# num = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
# x = 49
# idx = 0
# for el in num:
#     if (x == el):
#         print ("found at index", idx)
#         break
#     idx += 1
 

# n = int(input("enter number: "))
# for el in range(n,100,n):
#     print(el)

# n = 7
# sum = 0
# for i in range(1,n+1):
#     sum += i
# print ("total sum: ", sum)

n = 7
sum = 0
i = 1
while i <= n:
    sum += i
print("total sum:", sum)
i+= 1
