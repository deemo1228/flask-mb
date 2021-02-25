from app import db


#定義模型(model)
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), unique=True, nullable=False)
    city_id = db.Column(db.Integer, db.ForeignKey('cities.id'))
    messages = db.relationship('Message', backref='user')
    def __repr__(self):
        return 'id=%r, User_name=%r' % (self.id, self.name)



