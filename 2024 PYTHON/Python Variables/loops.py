
print("**************************GUESS LUCKY NUMBER******************************************\n\n       Progmamme Inside \n\n")
# lucky_number = 5
# guess_count = 1
# guess_limit = 4
# while guess_count < guess_limit:
#     lucky_number=int(input(f"Enter your number {guess_count} Guess: "))
#     guess_count+=1
#     if lucky_number ==5:
#         print("You Won!")
#         break
#     elif lucky_number >10:
#         if guess_limit<guess_limit:
#           print("Select Numbers less than 10")
#         else:
#             print("Error")
#         guess_count = 2
#         lucky_number = 5
#         guess_limit = 4
#         while guess_count < guess_limit:
#             lucky_number=int(input(f"Enter your number {guess_count} Guess: "))
#             guess_count+=1
#             if lucky_number ==5:
#                 print("You Won!")
#                 break
            
#             elif guess_count==guess_limit:
#                 print("Error")
            
#     # elif lucky_number== :
#     #     print("Oops! Something happened. \nTry again.")
#     #     guess_count = 2
#     #     lucky_number = 5
#     #     guess_limit = 4
#     #     while guess_count < guess_limit:
#     #         lucky_number=int(input(f"Enter your number {guess_count} Guess: "))
#     #         guess_count+=1
#     #         if lucky_number ==5:
#     #             print("You Won!")
#     #             break
#     #         else:
#     #             ("Sorry you lost!\nPlease try again!")
# else:
#         print("Sorry you lost!\nPlease try again!")            


print("**************************CAR GAME**('While Loop')****************************************\n\n      programme inside\n    While loop*\n is Used to execute a block of code multiple times\n\n")
def car_game():
    intake = '' 

    while True:
        break
        intake =input("> ").lower()
        started = False
        
        if intake == "start":
            if started:
                print("Car has already started!")
            else:
                started=True
                print("Car started ready to go....")
        elif intake == "stop":
            if not started:
                print("Car has already stopped.")
            else:
                started =False
                print("Car has stopped.")
        elif intake == "help":
            print("Start - to start car\nStop - to stop car\nQuit - to exit")
        elif intake == "quit":
            break
        else:
            print("I don't understand that!")
car_game()
print("************************For Loops*********\n\n\n****************************************Used to iterate through")


total = 0
for item in range(0,10):
    total+=item
print(f"Total:{total}")

print("****************************NESTED LOOOPS**************************************************")


# for i in range(0,4):
#     for j in range(2,6):
#      print(f"{(i, j)}")

# for i in range(0,5):
#     print(" xk")
#     for j in range(0,4):
#         print(" x", end="")
#         for k in range(0,3):
#             print("x", end="")



# def happy_new_year():
#     i=10
#     while i>0:
#         print(i)
#         i-=1
#     print("Happy new year")
# happy_new_year()

# def square_integer(numbers):
#     integer = list()
#     for i in numbers:
#         square = i*i
#         integer.append(square)
#     print(integer)
# square_integer([2,7,3,8,9,34])
    
    
# def fizzbuzz():
#     for num in range(0,101):
#         if num%3==0 and num%5==0:
#             print("fizzbuzz")
#         elif num%3==0:
#             print("fizz")
#         elif num%5==0:
#             print("buzz")
#         else:
#             print(num)
# fizzbuzz()