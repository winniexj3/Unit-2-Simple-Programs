low=0
high=100
print("Please think of a number between 0 and 100!")
x=50
print("Is your secret number "+ str(x) +"?")
ans=input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
while ans=="c":
    print("Game over. Your secret number was:"+x)
    if ans=="h":
        high=x
    x=(high+low)//2.0
    elif ans=="l":
        low=x
    x=(high+low)//2.0
    else :
        print("Sorry, I did not understand your input.")
        x=x

    
        