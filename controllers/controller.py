from flask import render_template, request, redirect, url_for
from app import app
from models.game import *
from models.player import *

# Redirect from default landing page to '/welcome' where the game starts.
@app.route('/')
def home():
    return redirect(url_for('index'))

@app.route('/welcome')
def index():
    return(render_template('index.html'))

# Both game methods still playable.

@app.route('/welcome', methods = ['POST'])
def pvp_game():
    new_p1_name = request.form['player1_name']
    new_p1_choice = request.form['player1_choice']
    new_p2_name = request.form['player2_name']
    new_p2_choice = request.form['player2_choice']
    player1 = Player(new_p1_name, new_p1_choice)
    player2 = Player(new_p2_name, new_p2_choice)
    game = Game(player1, player2)
    win = game.run_rps()
    lose = game.rps_loser()
    if (win =='draw' or lose == "draw"):
        return (render_template('draw.html'))

    return(render_template('result.html', winner = win, loser = lose))

@app.route('/<choice1>/<choice2>')
def rps_game(choice1, choice2):
    player1 = Player("Player 1", choice1)
    player2 = Player("Player 2", choice2)
    game = Game(player1, player2)
    win = game.run_rps()
    lose = game.rps_loser()
    if (win =='draw' or lose == "draw"):
        return (render_template('draw.html'))

    return (render_template('result.html', winner = win, title = 'And the winner is...', loser = lose))