class Game():

    def rps(self, player1, player2):
        valid_choices = ["Rock", "Paper", "Scissors"]

        if ((player1.choice not in valid_choices) or (player2.choice not in valid_choices)):
            return "Invalid choice"
        if player1.choice == player2.choice:
            return None
        if (player1.choice == "Rock" and (player2.choice == "Scissors")):
            return player1
        elif (player1.choice == "Paper" and (player2.choice == "Rock")):
            return player1
        elif (player1.choice == "Scissors" and (player2.choice == "Paper")):
            return player1
        else:
            return player2