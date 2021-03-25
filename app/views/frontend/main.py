from app.models.user import User
from app.models.message import Message
from app.models.city import City
from app import db
from flask import request, render_template, redirect, url_for
from app.views import frontend
from . import frontend
from marshmallow import ValidationError
from app.schemas.message import MessageSchema
from app.schemas.message import UpdateSchema
from app.schemas.city import CitySchema


@frontend.route('/', methods=["POST", "GET"])
def Index():
    """首頁"""
    if request.method == "POST":

        form_data = request.form.to_dict()  # {"current_content":"","current_title":"","id":"11"}

        # validate: marshmallow
        update_schema = UpdateSchema()

        try:
            data = update_schema.load(form_data)  # 驗證
        except ValidationError as err:
            return err.messages, 422

        select_message = Message.query.filter_by(id=data['id']).first()
        # 更新內容
        select_message.update_content(title=data['current_title'], content=data['current_content'])

        return redirect(url_for('frontend.Index'))

    ms = Message.query.all()
    return render_template('index33.html', messages=ms)


@frontend.route('/add', methods=["GET", "POST"])
def create_message():
    """Create new message"""
    """
    1. post: receive form data to dict
    2. use form[user_name] to find user_id
    3. validate: marshmallow
    4. message create
    """
    if request.method == "POST":
        form_data = request.form.to_dict()  # {"content":"","title":"","user_name":"deemo"}

        user = User.query.filter_by(name=request.form['user_name']).first()  # 依照使用者輸入的名字，去table:user，找出資料。  # id=2,User_name='deemo'

        # validate: marshmallow
        message_schema = MessageSchema()

        del form_data['user_name']  # 刪除form_data的user_name   # {"content":"","title":""}

        form_data['user_id'] = user.id  # 新增user_id入form   # {"content":"","title":"","user_id":2}

        try:
            data = message_schema.load(form_data)  # 驗證
        except ValidationError as err:
            return err.messages, 404
        # create message
        Message.create(user_id=data['user_id'], title=data['title'], content=data['content'])
        return redirect(url_for('frontend.Index'))
    return render_template('add.html')


@frontend.route('/delete/<message_id>', methods=['GET', 'POST'])
def delete(message_id):
    select_message = Message.query.filter_by(id=int(message_id)).first()
    select_message.delete()
    return redirect(url_for('frontend.Index'))


@frontend.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        form_data = request.form.to_dict()  # {"city_select":"1","user_name":"deemo1234"}

        # validate: marshmallow
        city_schema = CitySchema()

        try:
            data = city_schema.load(form_data)  # 驗證
        except ValidationError as err:
            return err.messages, 422

        create_user = User(city_id=data['city_select'], name=data['user_name'])
        create_user.register()

        return redirect(url_for('frontend.Index'))
    return render_template('register.html')


@frontend.app_errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404