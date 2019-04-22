from flask import render_template
from app import app
from .request  import get_pitches



# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    
    title = 'Home - Welcome to the best Pitches Site'
    return render_template('index.html', title = title)

app.route('/pickUpLines/')
def pickUpLines():
    '''
    View categories page function that returns the pickUpLines category and its data
    '''
    pitches = Pitch.get_pitches('pickUpLines')
    return render_template('pickUpLines.html', pitches = pitches)    

app.route('/product/')
def product():
    '''
    View categories page function that returns the product pitch category and its data
    '''
    pitches = Pitch.get_pitches('product')
    return render_template('product.html', pitches = pitches)        

app.route('/interview/')
def interview():
    '''
    View categories page function that returns the interview pitch category and its data
    '''
    pitches = Pitch.get_pitches('interview')
    return render_template('interview.html', pitches = pitches)     

app.route('/promotion/')
def promotion():
    '''
    View categories page function that returns the promotion pitch category and its data
    '''
    pitches = Pitch.get_pitches('promotion')
    return render_template('promotion.html', pitches = pitches)