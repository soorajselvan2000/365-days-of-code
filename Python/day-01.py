print("\nGive me the number\nI will show whether the number is an odd or even\n")

while True:
    userInput = input("Enter the number or 'q' for Quit: ")

    if userInput.lower() == "q":
        print("\nProgram is ended\nThank You, \nVisit again!!!")
        break

    userInput = int(userInput)
    if(userInput % 2 == 0):
        print(f"\nThe number {userInput} is an even number")

    else:
        print(f"The number {userInput} is an odd number")
