# # Prime Number

# while True:
#     num = (input("Enter the number or type 'e' to exit: "))
#     if( num.lower() == 'e'):
#         print("Exiting.....\nVisit again")
#         break
#     else:
#         num = int(num)
#         if(num <= 1):
#             print("1 is not a prime number")
#         else:
#             for i in range(2, num-1):
#                 if(num % i == 0):
#                     print("Number is not prime")
#                     break
#             else:
#                 print("Number is prime")




# Factorial of a number
while True:
    num = input("Enter the number or type 'e' to exit: ")
    if(num == 'e'):
        print("Exiting...\nVisit again.")
        break
    num = int(num)
    result = 0

    for i in range(1, num+1):
        result = result + i
    print(result)