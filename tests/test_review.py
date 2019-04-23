from app.models import Review,User
from app import db

def setUp(self):
        self.user_James = User(username = 'James',password = 'potato', email = 'james@ms.com')
        self.new_review = Review(pitch_id=12345,pitch_review='This is a good review',user = self.user_James)

def tearDown(self):
        Review.query.delete()
        User.query.delete()        