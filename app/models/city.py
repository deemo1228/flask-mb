from app import db

class City(db.Model):
    __tablename__ = 'cities'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), unique=True, nullable=False)
    users = db.relationship('User', backref='city')
    def __init__(self, name=None):
        self.name = name
    def __repr__(self):
        return 'id=%r, city_name=%r' % (self.id, self.name)