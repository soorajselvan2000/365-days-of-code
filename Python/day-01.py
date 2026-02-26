# #Day 1 - Odd or Even
# print("\nGive me the number\nI will show whether the number is an odd or even\n")

# while True:
#     userInput = input("Enter the number or 'q' for Quit: ")

#     if userInput.lower() == "q":
#         print("\nProgram is ended\nThank You, \nVisit again!!!")
#         break

#     userInput = int(userInput)
#     if(userInput % 2 == 0):
#         print(f"\nThe number {userInput} is an even number")

#     else:
#         print(f"The number {userInput} is an odd number")


# Largest of Three Numbers
print("If you give me 3 numbers I will tell which one is greater")
while True:
    Entry = input("\nAre you read or not\nPut 'Y' or 'N': ")


    if(Entry.lower() == 'n'):
        print('You Choosed to Exit\nThank You\nVisit again!!!')
        break
    elif(Entry.lower() == 'y'):
        input1 = input("Enter the first number: ")
        input2 = input("Enter the second number: ")
        input3 = input("Enter the third number: ")

        if(input1 == '' or input2 == '' or input3 == ''):
            print("\n Please enter all the inputs")

        elif(input1 > input2 and input1 > input3):
            print(f"\nThe {input1} is greater that {input2} & {input3}")

        elif(input2 > input1 and input3 < input2):
            print(f"\nThe {input2} is greater that {input1} & {input3}")

        elif(input3 > input1 and input2 < input3):
            print(f"\nThe {input3} is greater that {input1} & {input2}")

        else:
            print("\nYou entered a repeated number")  
    else:
        print('\nEnter a valid input')