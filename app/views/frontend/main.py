from app.models.user import User
from app.models.message import Message
from app.models.city import City
from app import db
from flask import request,render_template,redirect,url_for
from app.views import frontend
from . import frontend




@frontend.route('/', methods=["POST", "GET"])
def Index():
    if request.method == "POST":
        id_data = request.form['id']
        content = request.form['current_content']
        title = request.form['current_title']
        select_message = Message.query.filter_by(id=int(id_data)).first()
        select_message.title = title
        select_message.content = content
        db.session.commit()
    ms = Message.query.all()
    return render_template('index3.html', messages=ms)

@frontend.route('/add', methods=["GET", "POST"])
def Add():
    if request.method == "POST":
        content = request.form['content']
        title = request.form['title']
        add_name = request.form['add_name']
        select_user = User.query.filter_by(name=add_name)  # 先取得在user當中naem='Eric'的User_id
        # 在Message()這張表單新增資料
        create_Eric_Messags = Message(user_id=select_user[0].id, title=title, content=content)
        db.session.add(create_Eric_Messags)  # 建立資料暫存
        db.session.commit()  # 傳送至資料庫
        return redirect(url_for('frontend.Index'))
    return render_template('add.html')



@frontend.route('/delete/<message_id>', methods=['GET', 'POST'])
def delete(message_id):
    # if request.method == "POST":
    select_message = Message.query.filter_by(id=int(message_id)).first()
    # 利用 delete 的方法即可刪除單筆資料
    db.session.delete(select_message)
    # 將之前的操作變更至資料庫中
    db.session.commit()
    return redirect(url_for('frontend.Index'))


@frontend.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        user_name = request.form["user_name"]
        user_city = request.form["city_select"]  # 寫入城市再說
        create_user = User(city_id=user_city, name=user_name)  # User()為要加入入的表單  # 必要條件為id(非必要),city_id(必要),name(必要)
        db.session.add(create_user)  # 建立資料暫存
        db.session.commit()  # 傳送至資料庫
        return render_template('index3.html')
    return render_template('register.html')