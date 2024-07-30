import getpass
def setValue(player):
    while True:
        number=getpass.getpass(f"Player {player}, set your 4 digit number: ")
        print()
        if number.isdigit() and len(number) ==4 :
             return number
        else:
             print("Invalid !! Please enter a 4-digit number.")


def hint(number, guess):
    hint= ''
    for i in range(4):
        if number[i]==guess[i]:
            hint+= number[i]
        else:
            hint+= '_'
    return hint

def guess(number, player):
    attempts = 0
    while True:
        attempts +=1
        print(f"Attempts {attempts}: ")
        guess=input(f"Player {player}, enter your guess: ")
        if guess.isdigit() and len(guess)==4:
           if guess==number:
               print("\n Congratulations you guessed the right number !!!")
               return attempts
           else:
                hints=hint(number, guess)
                print("\nHint: ", hints)
        else:
            print("Invalid input. Please enter a 4-digit number.")

def game(player1,player2):

    while True:
        val1=setValue(player1)
        player2_count=guess(val1,player2)
        print(player2_count)

        if player2_count==1:
           print(f"\n{player2} is MASTERMIND")
           break

        val2=setValue(player2)
        player1_count=guess(val2,player1)
        if player1_count < player2_count:
            print(f"\n{player1} is MASTERMIND")
            break
        else:
            print(f"\n{player2} Won")
            break

print("\t\t\tWelcome to Mastermind Game")
print("\t\t\t---- ---")
print()
player1=input("Enter your name : ")
player2=input("Enter your name : ")
game(player1, player2)
print (f"Thank you {player1} and {player2} for playing")