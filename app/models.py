from . import db

class Pitch:
    '''
    Pitch class to define Pitch objects
    '''
    def __init__(self, id, pitch):
        self.id = id
        self.pitch = pitch


class Reviews:

    all_reviews = []

    def __init__(self,pitch_id, pitch, review):
        self.pitch_id = pitch_id
        self.pitch = pitch
        self.review = review

    def save_review(self):
        Review.all_reviews.append(self)

    @classmethod
    def clear_reviews(cls):
        Review.all_reviews.clear()        

    @classmethod
    def get_reviews(cls,id):

        response = []

        for review in cls.all_reviews:
            if review.pitch_id == id:
                response.append(review)

        return response    

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))

    def __repr__(self):
        return f'User {self.username}'        