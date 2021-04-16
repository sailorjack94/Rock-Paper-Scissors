from flask import render_template
from app import app
from models.game import Game
from models.player import Player

@app.route('/')
def index():
    return(render_template('index.html'))

@app.route('/<choice1>/<choice2>')
def rps_game(choice1, choice2):
    player1 = Player("Niall", choice1)
    player2 = Player("Bob", choice2)
    game = Game(player1, player2)
    win = game.run_rps()
    return f'{win.name} wins by playing {win.choice}!'
    