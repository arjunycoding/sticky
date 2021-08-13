from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

ENV = 'dev'

if ENV == 'dev':
    app.debug = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:a.yuvAc*@localhost/sticky'
else:
    app.debug = False
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://qoxgvaniitknjb:2b0618f540cdb4986f43f138545490b469ca379f9cf35f961ad1826fea7cd487@ec2-44-196-250-191.compute-1.amazonaws.com:5432/ddk764gsjtnc6c'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class AccountInfo(db.Model):
    __tablename__ = 'accountInfo'
    email = db.Column(db.String(200), primary_key=True)
    password = db.Column(db.String(200))
    username = db.Column(db.String(200), primary_key=True)

    def __init__(self, email, password, username):
        self.email = email
        self.password = password
        self.username = username

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/signup')
def signup():
    return render_template('signUp.html')

@app.route('/createaccount', methods=['POST'])
def createaccount():
    email = request.form['email']
    password = request.form['password']
    username = request.form['username']
    if email == '' or password == '' or username == '':
        return render_template('signUp.html', message='Please enter requiered fields')
    if db.session.query(AccountInfo).filter(AccountInfo.username == username).count() == 0 and db.session.query(AccountInfo).filter(AccountInfo.email == email).count() == 0:
        data = AccountInfo(email, password, username)
        db.session.add(data)
        db.session.commit()
        return render_template('login.html')
    return render_template('signUp.html', message='Sorry! Your username or email was already taken')


@app.route('/mainpage', methods=['POST'])
def mainpage():
    username = request.form['username']
    password = request.form['password']
    user = AccountInfo.query.filter_by(username=username, password=password).first()
    if user == None:
        return render_template('login.html', message='You have entered the wrong username or password')
    return render_template('index.html')

if __name__ == '__main__':
    app.run()