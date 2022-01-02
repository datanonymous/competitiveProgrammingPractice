
#####
#Bit++
#https://codeforces.com/problemset/problem/282/A
a = int(input())
initialValue = 0
for x in range(a):
    b = str(input())
    if "+" in b:
        initialValue += 1
    else:
        initialValue -= 1
print(initialValue)
#####

#####
#Wrong Subtraction
#https://codeforces.com/problemset/problem/977/A
# a, b = [int(x) for x in input().strip().split()]
# aSeparated = [int(x) for x in str(a)] #use list comprehension to split integer into digits
#
# for i in range(b):
#     if aSeparated[-1] != 0:
#         a = a - 1
#     else:
#         a = a // 10 #integer division vs floating point division
#     aSeparated = [int(x) for x in str(a)]
# print(a)
#####

#####
# #Domino piling
# #https://codeforces.com/problemset/problem/50/A
# a, b = [int(x) for x in input().strip().split()]
# product = a * b
# if product % 2 == 0: #product is even
#     print(int(product/2))
# else:
#     print(int((product-1)/2)) #product is odd
#####

#####
#Next Round
#https://codeforces.com/problemset/problem/158/A
# n, k = [int(x) for x in input().strip().split()]
# numberList = [int(x) for x in input().strip().split()]
# counter = 0
# for i in range(n):
#     if numberList[i] >= numberList[k-1] and numberList[i] != 0:
#         counter = counter + 1
# print(counter)
#####

#####
#Team
#https://codeforces.com/problemset/problem/231/A
# n = int(input())
# k = input().strip().split()
# print(k)
# counter = 0
# for i in range(n):
#     inputNumberList = input().strip().split()
#     numberList = [int(x) for x in inputNumberList]
#     if sum(numberList) >= 2:
#         counter = counter + 1
# print(counter)
#####

#####
#Way too long words
#https://codeforces.com/problemset/problem/71/A
# n = int(input())
# for i in range(n):
#     inputString = str(input())
#     if len(inputString) > 10:
#         print(inputString[0]+str(len(inputString)-2)+inputString[-1])
#     else:
#         print(inputString)
#####

#####
#Watermelon
#https://codeforces.com/problemset/problem/4/A
# n = int(input())
# y=0
# z=0
# for i in range(1, n):
#     if (n-i)%2==0 and i%2==0:
#         y+=1
#     else:
#         z+=1
# if y>=1:
#     print("YES")
# else:
#     print("NO")
#####

#####
#Wrong Subtraction
#https://codeforces.com/problemset/problem/977/A
# https://www.youtube.com/watch?v=xAeiXy8-9Y8
# n, k = [int(x) for x in input().strip().split()]
# print(n)
# print(k)
# for i in range(k):
#     if n%10==0:
#         n = n//10
#     else:
#         n = n - 1
# print(n)
#####

# # This is a sample Python script.
#
# # Press Shift+F10 to execute it or replace it with your code.
# # Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
#
#
# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')
#
# # See PyCharm help at https://www.jetbrains.com/help/pycharm/


