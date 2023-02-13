from boggle import Boggle
from flask import Flask, render_template, session, request

from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'

starter_boggle = Boggle()
score = 0

def make_board():
    """make_board() returns list of 5 lists each with 5 characters 
    >>> make_board()
    [['H', 'F', 'N', 'T', 'B'], ['E', 'Z', 'F', 'M', 'Z'], ['N', 'R', 'F', 'H', 'Q'], ['Y', 'E', 'Q', 'O', 'X'], ['E', 'E', 'I', 'I', 'X']]
    """
    board = starter_boggle.make_board()
    return board

def add_score(score, msg, guess):
    '''if guess clears as valid for points add points'''
    if msg == 'ok':
        session['score'] = int(score) + int(len(guess))
        return int(session['score'])

@app.route('/')
def show_home():
    '''renders base bage, index.html'''
    session['score'] = 0
    return render_template('index.html')

@app.route('/boggle', methods=['GET', 'POST'])
def show_boggle_board():
    '''creates boggle board from Boggle class and sets board value to the session, renders boggle template'''

    #  create new board list
    board = make_board()
    # set new board to session for use by other routes
    session['board'] = board
    # render the boggle template
    return render_template('boggle.html')

@app.route('/check', methods=['POST'])
def check_valid_word():
    '''Checks if valid word'''

    # takes guess form value and changes to lower case
    guess = request.form.get('guess').lower()
    # gets board value from session
    board = session['board']
    # checks if guess is valid word via Boggle class method
    is_valid_word = starter_boggle.check_valid_word(board, guess)
    # gets score from session['score'] value
    score = session['score']
    # checks msg to see if OK, when True it takes current score and adds correct guess length to score
    score = add_score(score, is_valid_word, guess)
    # makes variables dictionary to pass to template, if this will work
    return render_template('boggle.html', guess=guess, is_valid_word=is_valid_word, score=score)

@app.route('/reset', methods=["GET"])
def reset_score():
    '''get request to /reset sets the session['score'] =0'''
    session['score'] = 0
    return render_template('boggle.html')


# todo implement this to work, so word can only be guessed once. 
# todo either make a set of words, or remove word from list of words db when correctly guessed. 
# user_words = {w for w in starter_boggle.words}
# def remove_word(guess):
#     '''adds guess to user_guesses'''
#     # user_words.add(guess)
#     starter_boggle.words.remove(guess)
#     return user_words
# todo END TODO 