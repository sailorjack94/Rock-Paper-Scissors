from flask import render_template
from app import app
from models.game import Game
from models.player import Player

@app.route('/welcome')
def index():
    return(render_template('index.html'))

@app.route('/<choice1>/<choice2>')
def rps_game(choice1, choice2):
    player1 = Player("Player 1", choice1)
    player2 = Player("Player 2", choice2)
    game = Game(player1, player2)
    win = game.run_rps()
    lose = game.rps_loser()
    # return f'{win.name} wins by playing {win.choice}!'
    return (render_template('result.html', winner = win, title = 'And the winner is...', loser = lose))