import random


tries = 5
randomnumber = random.randrange(1,9)
print("Guess the number that is between 1 to 9")
while(tries<=5):
    numberEntered = int(input("Enter a number : "))
    tries = tries - 1
    if(numberEntered == randomnumber):
        print("You are right!")
        break
    elif(tries==0):
        print("You LOSE!")
        break
    elif(numberEntered<randomnumber):
        print("Your number is small : " + str(tries) + " chances left" )
        continue
    elif(numberEntered>randomnumber): 
        print("You number is big : "+ str(tries) + " chances left" )
        continue
    
