class Game():

    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2

    def run_rps(self):
        valid_choices = ["rock", "paper", "scissors"]

        if ((self.player1.choice not in valid_choices) or (self.player2.choice not in valid_choices)):
            return "Invalid choice"
        if self.player1.choice == self.player2.choice:
            return "draw" #change to None to comply with brief - but don't know why?
        if (self.player1.choice == "rock" and (self.player2.choice == "scissors")):
            return self.player1
        elif (self.player1.choice == "paper" and (self.player2.choice == "rock")):
            return self.player1
        elif (self.player1.choice == "scissors" and (self.player2.choice == "paper")):
            return self.player1
        else:
            return self.player2

    def rps_loser(self):
        valid_choices = ["rock", "paper", "scissors"]

        if ((self.player1.choice not in valid_choices) or (self.player2.choice not in valid_choices)):
            return "Invalid choice"
        if self.player1.choice == self.player2.choice:
            return "draw" #change to None to comply with brief - but don't know why?
        if (self.player1.choice == "rock" and (self.player2.choice == "scissors")):
            return self.player2
        elif (self.player1.choice == "paper" and (self.player2.choice == "rock")):
            return self.player2
        elif (self.player1.choice == "scissors" and (self.player2.choice == "paper")):
            return self.player2
        else:
            return self.player1