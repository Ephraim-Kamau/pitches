from flask import render_template,request,redirect,url_for, abort
from . import main
from .forms import ReviewForm,UpdateProfile
from .. import db,photos
from flask_login import login_required, current_user
from ..models import Review, User,Pitch
 


# Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    
    title = 'Home - Welcome to the best Pitches Site'
    return render_template('index.html', title = title)

@main.route('/pickUpLines/pitches')
def pickUpLines():
    '''
    View categories page function that returns the pickUpLines category and its data
    '''

    return render_template('pickUpLines.html')    

@main.route('/product/pitches')
def product():
    '''
    View categories page function that returns the product pitch category and its data
    '''
    
    return render_template('product.html')        

@main.route('/interview/pitches')
def interview():
    '''
    View categories page function that returns the interview pitch category and its data
    '''
    
    return render_template('interview.html')     

@main.route('/promotion/pitches')
def promotion():
    '''
    View categories page function that returns the promotion pitch category and its data
    '''
    
    return render_template('promotion.html')


@main.route('/review/new', methods = ['GET','POST'])
@login_required
def new_review():
     '''
     Function that creates new pitches
     '''
     form = ReviewForm()
    

     if form.validate_on_submit():
         review = form.content.data
         category_id = form.category_id.data

        # Updated review(pitch) instance
         new_review = Review(review_id = review.id,user = current_user)

        # save review (pitch) method
         new_review.save_review()
         return redirect(url_for('.review', id = review.id))

     return render_template('new_review.html', new_review_form = form)     

@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form)

@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))   

@main.route('/user/<uname>')
def profile(uname):
    user=User.query.filter_by(username=uname).first()
    
    if user is None:
        abort()

    
    title=uname

    return render_template("profile/profile.html", user = user,title=title)

@main.route("/pitch/new/review/<int:id>", methods =["GET","POST"])
@login_required
def review(id):
    pitch_id=id
    pitch=Pitches.query.all();
    title="Write a comment"
    form=ReviewForm()
    if form.validate_on_submit():
        title=form.title.data
        comments=form.comments.data

        review=Comments(pitch_id=id, pitch_title=title, comments=comments, user=current_user)

        review.save_comment
        return redirect(url_for('.review', id=pitch_id))

