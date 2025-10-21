import random

class Game:
    def __init__(self):
        self.choice = ['R',"P","S"]
        

    def User_Input(self):
        while True:
            guess = input("Enter your input (R,S,P) only: ").upper()
            if guess not in ['R', "P", "S"]:
                print("Pleaser enter your answer correctly")
            else:
                return guess

    def Computer_choice(self):
        return random.choice(self.choice)

    def condition(self, guess, computer):
        if guess == computer:
            print("it's a draw")
            return None
        elif (guess=="R" and computer=="S") or \
             (guess=="P" and computer=="R") or \
             (guess=="S" and computer=="P"):
            print("You won")
            return True
        else:
            print("You lost")
            return False
    
    def guessed(self,user,computer):
        print(f"Your Guessed {user} and computer guessed {computer}")
        
    def start(self):
        print("Welcom to the Rock Paper Scissors game")
        
        while True:
            guess = self.User_Input()
            cond = self.Computer_choice()

            result = self.condition(guess,cond)

            self.guessed(guess,cond)

            if result is not None:
                break

if __name__ == "__main__":
    g = Game()
    g.start()