import random
import time
from datetime import date

# def game():
#     try:
#         print("WELCOME TO GAME")
#         guess_by_computer = random.randint(1,5)
#         guess_by_user = int(input("ENTER THE NUMBER TO GUESS:"))

#         if guess_by_computer == guess_by_user:
#             print("Yahho You Guessed Correct:")
#         else:
#             print("NO No No!! You Guessed Incorrect")
#         print("Computer guesses",guess_by_computer)
#         print("You guesses",guess_by_user)
#     except Exception as e:
#         print("Enter the correct value:",e)
# game()

# def nested():
#     for i in range(1,11):
#         print(i)
#     for j in range(11,20):
#         print(j)
# nested()

# user_pass = {}
# while True:
#     user = input("Your name:")
#     pwd = input("Your password:")

#     if user in user_pass and pwd == user_pass[user]:
#         print("Welcome", user)
#         break
#     else:
#         user_pass[user]=pwd
#         print("registration completed, Please Login")

# complete = False
# user = [['rahul','123']]
# while not complete:
#     username = input("What is the username?")
#     password = input("What is the password?")
#     for n in len(user):
#          if username == user[n][0]:
#               print("Good!")
#               if password == user[n][1]:
#                    print("User has been identified, Welcome",username)
#                    complete = True
#               else:
#                    break
#                    print("Input password again")
#     if not complete:
#         print("Input username again!")


# num = [1,2,3,4,5,6,7,8,9]
# odd = []
# even = []
# for i in num:
#     if i%2 == 0:
#         even.append(i)
#     else:
#         odd.append(i)
# print(odd)
# print(even)

# even =[]
# odd = []
# for i in range(1,10):
#     if i%2 == 0:
#         even.append(i)
#     else:
#         odd.append(i)


# print(even)
# print(odd)

# l = [1,2,3]
# r = l[::-1]
# print("Length of list is:",len(r))
# print(r)



# input_list = [1, 2, 2, 5, 8, 4, 4, 8]
# l1 = []
# count = 0
# for item in input_list:
#     if item not in l1:
#         count += 1
#         l1.append(item)
# print("No of unique items are:", count)



# n = 12321
# n = str(n)
# if n == n[::-1]:
#     print("Yes Palindrone")
# else:
#     print("No Palindorne")

# def comb(L): 
      
#     for i in range(3): 
#         for j in range(3): 
#             for k in range(3):     
#                 # check if the indexes are not 
#                 # same 
#                 if (i!=j and j!=k and i!=k): 
#                     print(L[i], L[j], L[k]) 
# comb([1,2,3])

l = [1,2,3,4,5]
print("Max",max(l))
print("Min",min(l))
    
    
   
































    






































































