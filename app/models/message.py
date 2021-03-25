from app import db


class Message(db.Model):
    __tablename__ = 'messages'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    title = db.Column(db.String(30), nullable=False)
    content = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return 'id=%r, title=%r,content=%r' % (self.id, self.title, self.content)

    def update_content(self, title: str, content: str) -> None:
        self.title = title
        self.content = content
        db.session.add(self)
        db.session.commit()

    @classmethod
    def create(cls, user_id, title, content):
        """建立訊息"""
        message = Message(user_id=user_id,
                          title=title,
                          content=content)
        db.session.add(message)
        db.session.commit()

    def delete(self) -> None:
        """delete message"""
        db.session.delete(self)
        db.session.commit()


