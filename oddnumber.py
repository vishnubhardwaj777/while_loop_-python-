number = int(input("enter a number"))
if(number % 2 != 0):
    while(number <= 10):
        print(number)
        number = number + 2
else:
    print("enter number is not odd number")        