# # import random 
# # x=int(input("range till u want")) 
# # while True: 
# #     c=random.randint(1,x) 
# #     n=c 
# #     user=int(input("entr the number user want")) 
# #     if(user==n): 
# #         print("right guess") 
# #         break; 
# #     else: 
# #         print("better luck next time") 
# #     choice=int(input("1 to continue")) 
# #     if(choice==1): 
# #         continue; 
# #     else:
# #         break;
# # import random

# # print("Welcome to the Guessing Game")

# # s = random.randint(1, 100)

# # while True:
# #     g = int(input("Guess the number (between 1 and 100): "))
    
# #     if (g == s):
# #         print("Congratulations! You guessed the correct number!")
# #         break
# #     elif (g < s):
# #         print("its too low, Try guessing higher.")
# #     else:
# #         print("its too high, Try guessing lower.")
import random
x=int(input("range till u want"))
while True:
    c=random.randint(1,x)
    n=c
    user=int(input("enter the number user want"))
    if(user==n):
        print("right guess")
        break;
    else:
        print("better luck next time")
    choice=int(input("1 to continue"))
    if(choice==1):
        continue;
    else:
        break;
