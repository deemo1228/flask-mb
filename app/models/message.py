from app import db


class Message(db.Model):
    __tablename__ = 'messages'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    title = db.Column(db.String(30), nullable=False)
    content = db.Column(db.String(100), nullable=False)
    def __repr__(self):
        return 'id=%r, title=%r,content=%r' % (self.id, self.title,self.content)