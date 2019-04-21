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