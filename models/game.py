class Game():

    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2

    def rps(self):
        valid_choices = ["Rock", "Paper", "Scissors"]

        if ((self.player1.choice not in valid_choices) or (self.player2.choice not in valid_choices)):
            return "Invalid choice"
        if self.player1.choice == self.player2.choice:
            return None
        if (self.player1.choice == "Rock" and (self.player2.choice == "Scissors")):
            return self.player1
        elif (self.player1.choice == "Paper" and (self.player2.choice == "Rock")):
            return self.player1
        elif (self.player1.choice == "Scissors" and (self.player2.choice == "Paper")):
            return self.player1
        else:
            return self.player2